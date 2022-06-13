pub struct ReadWrapper<R> {
    reader: R,
    tokens: Vec<String>,
}

impl<R> ReadWrapper<R> {
    pub fn new(reader: R) -> Self { Self { reader, tokens: vec![] } }
}

impl<R: std::io::BufRead> ReadWrapper<R> {
    pub fn read<T: std::str::FromStr>(
        &mut self,
    ) -> Result<T, <T as std::str::FromStr>::Err> {
        while self.tokens.is_empty() {
            let mut buf = String::new();
            self.reader.read_line(&mut buf).unwrap();
            self.tokens =
                buf.split_whitespace().map(str::to_string).rev().collect();
        }
        self.tokens.pop().unwrap().parse::<T>()
    }
}

pub fn locked_stdin_reader() -> ReadWrapper<std::io::StdinLock<'static>> {
    let stdin = Box::leak(Box::new(std::io::stdin()));
    ReadWrapper::new(stdin.lock())
}

pub fn locked_stdout_buf_writer()
-> std::io::BufWriter<std::io::StdoutLock<'static>> {
    let stdout = Box::leak(Box::new(std::io::stdout()));
    std::io::BufWriter::new(stdout.lock())
}

/// reference
/// https://users.rust-lang.org/t/show-value-only-in-debug-mode/43686/3
#[macro_export]
#[allow(unused_macros)]
macro_rules! debug {
    ($($x:tt)*) => {
        {
            // default in debug mode
            #[cfg(debug_assertions)]
            {
                std::dbg!($($x)*)
            }

            // default in release mode
            #[cfg(not(debug_assertions))]
            {
                ($($x)*)
            }
        }
    }
}

#[macro_export]
#[allow(unused_macros)]
macro_rules! write_vec {
    ($writer:ident, $values:expr) => {
        write_vec!($writer, $values, sep: ' ');
    };

    ($writer:ident, $values:expr,sep: $sep:expr) => {
        let n = $values.len();
        if n == 0 {
            writeln!($writer).unwrap();
        } else {
            for i in 0..n - 1 {
                write!(
                    $writer,
                    "{}{}",
                    $values[i], $sep
                )
                .unwrap();
            }
            writeln!($writer, "{}", $values[n - 1]).unwrap();
        }
    };
}

#[macro_export]
#[allow(unused_macros)]
macro_rules! write_all {
    ($writer:ident) => {
        writeln!($writer).unwrap();
    };

    ($writer:ident, $v:expr) => {
        writeln!($writer, "{}", $v).unwrap();
    };

    ($writer:ident, $v:expr, $($values:expr),+) => {
        write!($writer, "{} ", $v).unwrap();
        write_all!($writer, $($values),*);
    };
}

#[macro_export]
#[allow(unused_macros)]
macro_rules! read_vec {
    ($reader:ident, $type:ty, $n:expr) => {
        (0..$n)
            .map(|_| $reader.read::<$type>())
            .collect::<Result<Vec<_>, _>>()
            .unwrap()
    };
}

// TODO: main
// #[allow(warnings)]
fn main() -> Result<(), Box<dyn std::error::Error>> {
    use std::io::Write;
    let mut reader = locked_stdin_reader();
    let mut writer = locked_stdout_buf_writer();

    let n: u64 = reader.read()?;
    // let count = prime_pi_fast(n);
    // let count = prime_pi_fast_half(n);
    let count = prime_pi_fast_optimized(n);

    writeln!(writer, "{}", count)?;
    writeln!(
        writer,
        "{}",
        prime_pi_approx_ln(n as u128)
    )?;
    writer.flush()?;
    Ok(())
}
// u128 prime_pi_approx_ln(u128 n) {
//   if (n < 2) return 0;
//   f128 nf = n;
//   return nf / logf128(nf) * 1.1;
// }

/// mainly used for initializing prime_numbers vec with capacity.
pub fn prime_pi_approx_ln(n: u128) -> u128 {
    if n < 2 {
        return 0;
    }
    return n * 3 / bit_length_128(n) as u128 >> 1;
    // suppose pi(x) ~= [x / ln(x)] * 1.1
    // = [x / log_2(x) * (log_2(x) / ln(x))] * 1.1
    // = [x / log_2(x) * ln(2)^{-1}] * 1.1
    // ~= [x / log_2(x) * 1.4427] * 1.1
    // ~= x * 3 / log_2(x) / 2
}

pub fn bit_length_128(n: u128) -> u8 {
    (0u128.leading_zeros() - n.leading_zeros()) as u8
}

/// O(N^{3/4}) with constant time optimization.
/// insipired by O(N^{3/4}/log{N}) implementation.
pub fn prime_pi_fast_half(n: u64) -> u64 {
    if n < 2 {
        return 0;
    }
    if n == 2 {
        return 1;
    }
    let sqrt = floor_sqrt(n) as usize;
    let n = n as usize;
    let size = (sqrt + 1) >> 1;
    let half = |j: usize| (j - 1) >> 1;

    let mut small = (0..size).collect::<Vec<_>>();
    let mut large =
        (0..size).map(|i| half(n / (i << 1 | 1))).collect::<Vec<_>>();

    for i in (3..=sqrt).step_by(2) {
        let i_half = half(i);
        if small[i_half] == small[i_half - 1] {
            continue;
        }
        let pi = small[i_half - 1];
        let mut border = sqrt / i;
        if border & 1 == 0 {
            border -= 1;
        }
        let n_i = n / i;
        for k in (1..=border).step_by(2) {
            large[half(k)] -= large[half(k * i)] - pi;
        }
        for k in (border + 2..=sqrt.min(n_i / i)).step_by(2) {
            large[half(k)] -= small[half(n_i / k)] - pi;
        }
        for k in (i..=border).rev().step_by(2) {
            let sub = small[half(k)] - pi;
            small[half(k * i)..]
                .iter_mut()
                .take(half(i) + 1)
                .for_each(|j| *j -= sub);
        }
    }
    large[0] as u64 + 1
}

/// Compute \pi(n)
/// O(N^{3/4}/log{N})
/// reference
/// - https://judge.yosupo.jp/submission/61553
pub fn prime_pi_fast_optimized(n: u64) -> u64 {
    if n < 2 {
        return 0;
    }
    if n == 2 {
        return 1;
    }
    let half = |i: usize| (i - 1) >> 1;
    let sqrt = floor_sqrt(n) as usize;
    let n = n as usize;
    let mut size = (sqrt + 1) >> 1;
    // for memory saving. do not have space for even numbers.
    let mut small: Vec<usize> = (0..size).collect();
    // j=1, 3, 5, 7, ..., k=0, 1, 2, 3
    // -> unsieved count less than or equal to j is (j - 1) >> 1 = k.
    let mut large: Vec<usize> =
        (0..size).map(|i| half(n / (i << 1 | 1))).collect();
    // (j - 1) >> 1 = k <-> (k << 1 | 1) = j
    let mut unsieved_nums: Vec<usize> = (0..size).map(|i| i << 1 | 1).collect();
    // 1initially, 1, 3, 5, ... (odd at most sqrt(n))
    // unsieved_nums[..size] are odd integers which are still unsieved.
    // (size will be updated in each iteration)
    // unsieved_nums[size..] are no longer used.
    let mut checked_or_sieved = vec![false; size];
    // 1, 2 -> 0, 3, 4 -> 1, ... (because even numbers are skipped.)
    let mut pi = 0;
    for i in (3..=sqrt).step_by(2) {
        if checked_or_sieved[half(i)] {
            // sieved
            continue;
        }
        let i2 = i * i;
        if i2 * i2 > n {
            break;
        }
        checked_or_sieved[half(i)] = true; // checked
        for j in (i2..=sqrt).step_by(i << 1) {
            checked_or_sieved[half(j)] = true;
        }
        // update large and unsieved_nums
        let mut ptr = 0;
        for k in 0..size {
            let j = unsieved_nums[k];
            if checked_or_sieved[half(j)] {
                continue;
            }
            let border = j * i;
            large[ptr] = large[k]
                - if border <= sqrt {
                    large[small[border >> 1] - pi]
                } else {
                    small[half(n / border)]
                }
                + pi;
            unsieved_nums[ptr] = j;
            ptr += 1;
        }
        size = ptr;
        let mut j = half(sqrt);
        let mut k = sqrt / i - 1 | 1;
        while k >= i {
            let c = small[k >> 1] - pi;
            let e = k * i >> 1;
            while j >= e {
                small[j] -= c;
                j -= 1;
            }
            k -= 2;
        }
        pi += 1;
    }
    // be careful of overflow.
    large[0] += if pi > 0 {
        size + ((pi - 1) << 1)
    } else {
        // -1 << 1 == -2
        size.saturating_sub(2)
        // if size == 1,
        // (size + ((pi - 1) << 1)) * (size - 1) >> 1 == 0
        // regardless of `size + ((pi - 1) << 1)`
    } * (size - 1)
        >> 1;
    for k in 1..size {
        large[0] -= large[k];
    }
    for k in 1..size {
        let q = unsieved_nums[k];
        let n_q = n / q;
        let e = small[half(n_q / q)] - pi;
        if e < k + 1 {
            break;
        }
        let mut t = 0;
        for l in k + 1..=e {
            t += small[half(n_q / unsieved_nums[l])];
        }
        large[0] += t - (e - k) * (pi + k - 1);
    }

    large[0] as u64 + 1
}

/// O(N^{3/4})
pub fn prime_pi_fast(n: u64) -> u64 {
    if n < 2 {
        return 0;
    }
    let sqrt = floor_sqrt(n) as usize;
    let n = n as usize;

    // consider sieve of Eratosthenes' transitions.
    // S(j, p) := number of trues in [2, j] after sieving with prime p.
    let mut small = vec![0; sqrt + 1]; // small[j] = S(j, p)
    let mut large = vec![0; sqrt + 1];
    // large[k] := S([n/k]=j, p)
    // large[0] is undefined.
    for i in 1..=sqrt {
        small[i] = i - 1;
        large[i] = n / i - 1;
    }

    for i in 2..=sqrt {
        if small[i] == small[i - 1] {
            continue;
            // i is not prime.
        }
        // we want update S(j, i) such that j >= i * i.
        // for j > sqrt(n), update large[inv] such that j = [N/inv].
        // for j <= sqrt(n), update small[j].
        let pi = small[i - 1]; // S(p - 1, p - 1) = pi(p - 1).

        // compute S(j, i) -= S(j/i, i - 1) - pi

        // for large
        // large[n/j] -= large[n/(j/i)] - pi = large[(n/j)i] - pi
        // large[k] -= large[ki] - pi
        // because j = [N/k] >= i*i, k <= [N/(i*i)]
        // be careful of updating in forward order because of in-place.
        let border = sqrt / i;
        let n_i = n / i; // cache
        for k in 1..=border {
            large[k] -= large[k * i] - pi;
        }
        for k in border + 1..=sqrt.min(n_i / i) {
            large[k] -= small[n_i / k] - pi;
        }

        // for small
        // just small[j] -= small[j/i] - pi (i*i <= j <= sqrt)
        // be careful of updating in reverse order because of in-place.
        // for optimization, use multiplication instead of division
        // by computing giving dp instead of receiving.
        // small[j=[k*i, sqrt]] -= small[k] - pi (i <= k <= sqrt/i)
        for k in (i..=border).rev() {
            let sub = small[k] - pi;
            small[(k * i)..].iter_mut().take(i).for_each(|j| *j -= sub);
        }
    }
    large[1] as u64
}

pub fn int_sqrt_binary_search(n: u64) -> u64 {
    let mut lo = 0;
    let mut hi = std::cmp::min(n + 1, 1 << 32);
    while hi - lo > 1 {
        let x = (lo + hi) >> 1;
        if x * x <= n {
            lo = x;
        } else {
            hi = x;
        }
    }
    lo
}

pub fn floor_sqrt(n: u64) -> u64 { int_sqrt_binary_search(n) }
