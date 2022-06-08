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

    // let n: usize = reader.read()?;
    // let a: usize = reader.read()?;
    // let b: usize = reader.read()?;

    // let primes = sieve_of_sundaram(n as u32 + 1);
    // let primes = sieve_of_eratosthenes(n + 1);
    // let primes = sieve_of_eratosthenes(n + 1);
    // let primes = linear_prime_sieve(n + 1).1;

    // let pi = primes.len();
    // let mut res = vec![];
    // let mut i = b;
    // while i < pi {
    //     res.push(primes[i]);
    //     i += a;
    // }
    // write_all!(writer, pi, res.len());
    // write_vec!(writer, res);

    // let mut prime_gen = prime_generator(0, n as u64 + 1);

    // let mut res = vec![];
    // let mut i = 0;
    // while let Some(p) = prime_gen.next() {
    //     if i % a == b {
    //         res.push(p);
    //     }
    //     i += 1;
    // }

    // write_all!(writer, i, res.len());
    // write_vec!(writer, res);

    let a: u64 = reader.read()?;
    let b: u64 = reader.read()?;
    let range_sieve = RangeSieveOfEratosthenes::new(b + 1);
    writeln!(
        writer,
        "{}",
        range_sieve.find_prime_numbers(a, b + 1).len()
    )?;

    writer.flush()?;
    Ok(())
}



pub fn sieve_of_eratosthenes(sieve_size: usize) -> Vec<u32> {
    let mut primes = Vec::with_capacity(sieve_size >> 1);
    if sieve_size > 2 {
        primes.push(2);
    }
    let mut is_prime = vec![true; sieve_size >> 1];
    for i in (3..sieve_size).step_by(2) {
        if !is_prime[i >> 1] {
            continue;
        }
        primes.push(i as u32);
        for j in (i * i >> 1..sieve_size >> 1).step_by(i) {
            is_prime[j] = false;
        }
    }
    primes
}

/// compute least prime factor table and prime numbers list.
pub fn linear_prime_sieve(size: usize) -> (Vec<Option<u32>>, Vec<u32>) {
    let mut lpf = vec![None; size];
    let mut prime_numbers = Vec::with_capacity(size);
    for i in 2..size {
        if lpf[i].is_none() {
            lpf[i] = Some(i as u32);
            prime_numbers.push(i as u32);
        }
        for &p in &prime_numbers {
            if p > lpf[i].unwrap() || p as usize * i >= size {
                break;
            }
            debug_assert!(lpf[p as usize * i].is_none());
            lpf[p as usize * i] = Some(p);
        }
    }
    (lpf, prime_numbers)
}

pub fn sieve_of_sundaram(less_than: u32) -> Vec<u32> {
    let mut prime_numbers = vec![];
    if less_than <= 2 {
        return prime_numbers;
    }
    prime_numbers.push(2);
    let size = (less_than >> 1) as usize;
    let mut is_prime = vec![true; size];
    for i in 1..size {
        if is_prime[i] {
            prime_numbers.push(((i as u32) << 1) | 1);
        }
        for j in (i * (i + 1) << 1..size).step_by((i << 1) | 1) {
            is_prime[j] = false;
        }
    }
    prime_numbers
}

pub struct SieveOfEratosthenesLowMemoryPrimeGenerator {
    iter: std::vec::IntoIter<u64>,
    range_sieve: RangeSieveOfEratosthenes,
    ranges: std::vec::IntoIter<(u64, u64)>,
}

impl SieveOfEratosthenesLowMemoryPrimeGenerator {
    /// [lo, hi)
    pub fn new(mut lo: u64, mut hi: u64) -> Self {
        if lo < 2 {
            lo = 2;
        }
        if hi < 2 {
            hi = 2;
        }
        let mut ranges = vec![];
        let range_size = (floor_sqrt(hi) as usize) << 4; // 2 or 3?
        // because range sieve has only odd numbers internally,
        // the size is sqrt / 2.
        // so we can check more than twice the range at once.
        // four times is best in test.
        for i in (lo..hi).step_by(range_size) {
            ranges.push((
                i,
                std::cmp::min(hi, i + range_size as u64),
            ));
        }

        Self {
            iter: vec![].into_iter(),
            range_sieve: RangeSieveOfEratosthenes::new(hi as u64),
            ranges: ranges.into_iter(),
        }
    }
}

impl Iterator for SieveOfEratosthenesLowMemoryPrimeGenerator {
    type Item = u64;

    fn next(&mut self) -> Option<Self::Item> {
        if let Some(p) = self.iter.next() {
            return Some(p);
        }
        while let Some((lo, hi)) = self.ranges.next() {
            self.iter = self.range_sieve.find_prime_numbers(lo, hi).into_iter();
            if let Some(p) = self.iter.next() {
                return Some(p);
            }
        }
        None
    }
}

pub fn prime_generator(
    lo: u64,
    hi: u64,
) -> SieveOfEratosthenesLowMemoryPrimeGenerator {
    SieveOfEratosthenesLowMemoryPrimeGenerator::new(lo, hi)
}

pub fn floor_sqrt(n: u64) -> u64 { int_sqrt_binary_search(n) }

pub fn int_sqrt_binary_search(n: u64) -> u64 {
    let mut lo = 0;
    let mut hi = 1 << 32;
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

pub struct RangeSieveOfEratosthenes {
    primes: Vec<u64>,
    less_than: u64,
}

impl RangeSieveOfEratosthenes {
    pub fn new(less_than: u64) -> Self {
        Self {
            primes: find_prime_numbers(floor_sqrt(less_than) as u32 + 1)
                .into_iter()
                .map(|p| p as u64)
                .collect(),
            less_than,
        }
    }

    /// find prime numbers in [lo, hi).
    /// time: O((hi - lo)\log{\log{less_than}})
    /// space: O(hi - lo)
    pub fn find_prime_numbers(&self, mut lo: u64, hi: u64) -> Vec<u64> {
        assert!(lo <= hi && hi <= self.less_than);
        if hi <= 2 {
            return vec![];
        }
        if lo < 2 {
            lo = 2;
        }
        debug_assert!(2 <= lo && lo < hi);
        let mut res = vec![];
        if lo & 1 == 0 {
            if lo == 2 {
                res.push(2);
            }
            lo += 1;
        }
        if lo == hi {
            return res;
        }
        // initially, only odd numbers are in sieve.
        // be careful of indices.
        let size = ((hi - lo + 1) >> 1) as usize;
        let mut is_prime = vec![true; size];
        for &p in self.primes.iter().skip(1) {
            let mut from = p * p;
            if from >= hi {
                break;
            }
            from = std::cmp::max(from, (lo + p - 1) / p * p);
            if from & 1 == 0 {
                from += p;
            }
            debug_assert!(from & 1 == 1);
            for j in (((from - lo) >> 1) as usize..size).step_by(p as usize) {
                is_prime[j] = false;
            }
        }
        res.extend(
            is_prime.into_iter().enumerate().filter_map(|(i, is_prime)| {
                if is_prime { Some(lo + (i << 1) as u64) } else { None }
            }),
        );
        res
    }
}

pub fn find_prime_numbers(less_than: u32) -> Vec<u32> {
    sieve_of_eratosthenes(less_than as usize)
}
