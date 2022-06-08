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

    // let a = (0..n)
    //     .map(|_| reader.read::<u64>().unwrap())
    //     .collect::<Vec<_>>();

    // let bases = (0..5).map(|_| static_xorshift_64()).collect::<Vec<_>>();
    // let tester = FermatTestFixedBases::new(bases);
    // for x in a {
    //     writeln!(
    //         writer,
    //         "{}",
    //         if tester.is_prime(x) { "Yes" } else { "No" }
    //     )?;
    // }
    writer.flush()?;
    Ok(())
}

pub struct ModularArithemetic<M>(std::marker::PhantomData<M>);

impl<M: Modulus> ModularArithemetic<M> {
    pub fn add(mut x: u32, rhs: u32) -> u32 {
        x += rhs;
        if x >= M::modulus() {
            x -= M::modulus();
        }
        x
    }

    pub fn neg(x: u32) -> u32 { if x == 0 { 0 } else { M::modulus() - x } }

    pub fn sub(x: u32, rhs: u32) -> u32 { Self::add(x, Self::neg(rhs)) }

    pub fn mul(x: u32, rhs: u32) -> u32 {
        (x as u64 * rhs as u64 % M::modulus() as u64) as u32
    }

    pub fn invert

    // impl<M: Modulus> std::ops::DivAssign<Self> for Modular<M> {
    //     fn div_assign(&mut self, rhs: Self) { *self *= rhs.invert().unwrap();
    // } }
    // impl<M: Modulus> std::ops::Div<Self> for Modular<M> {
    //     type Output = Self;

    //     fn div(mut self, rhs: Self) -> Self::Output {
    //         self /= rhs;
    //         self
    //     }
    // }

    // impl<M: Modulus> Modular<M> {
    //     /// unlike extgcd, the caller cannot eunsure the inverse exist.
    //     /// with additional constant run time cost before calling this
    // function.     /// so if the inverse element does not exit,
    //     /// handle execption inside the method, and return Result<T, E>
    //     pub fn invert(self) -> Result<Self, &'static str> {
    //         if self.value() == 0 {
    //             // user does not call extgcd directly,
    //             // so return err instead of panic.
    //             return Err("0 is not invertible");
    //         }
    //         Ok(modular_inverse_extgcd(
    //             M::modulus() as u64,
    //             self.value() as u64,
    //         )?
    //         .into())
    //     }
    // }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct Modular<M> {
    phantom: std::marker::PhantomData<M>,
    value: u32,
}

impl<M> std::fmt::Display for Modular<M> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.value)
    }
}

impl<M> Modular<M> {
    // new version, cannot compile AtCoder yet.
    // pub const fn value(&self) -> u32 { self.value }

    pub fn value(&self) -> u32 { self.value }
}

impl<M: Modulus> Modular<M> {
    pub fn new(mut value: u32) -> Self {
        if value >= M::modulus() {
            value %= M::modulus();
        }
        Self {
            phantom: std::marker::PhantomData,
            value,
        }
    }

    pub fn modulus() -> u32 { M::modulus() }
}

impl<M: Modulus> From<u64> for Modular<M> {
    fn from(mut value: u64) -> Self {
        let m = M::modulus() as u64;
        if value >= m {
            value %= m;
        }
        Self::new(value as u32)
    }
}
impl<M: Modulus> From<i64> for Modular<M> {
    fn from(mut value: i64) -> Self {
        let m = M::modulus() as i64;
        if value < -m || value >= m {
            value %= m;
        }
        if value < 0 {
            value += m;
        }
        Self::new(value as u32)
    }
}

impl<M: Modulus> std::ops::AddAssign<Self> for Modular<M> {
    fn add_assign(&mut self, rhs: Self) {
        let mut value = self.value as u64 + rhs.value as u64;
        let m = M::modulus() as u64;
        if value >= m {
            value -= m;
        }
        self.value = value as u32;
    }
}

impl<M: Modulus> std::ops::Add<Self> for Modular<M> {
    type Output = Self;

    fn add(mut self, rhs: Self) -> Self::Output {
        self += rhs;
        self
    }
}

impl<M: Modulus> std::ops::Neg for Modular<M> {
    type Output = Self;

    fn neg(mut self) -> Self::Output {
        self.value = M::modulus() - self.value;
        self
    }
}

impl<M: Modulus> std::ops::SubAssign<Self> for Modular<M> {
    fn sub_assign(&mut self, rhs: Self) { *self += -rhs; }
}

impl<M: Modulus> std::ops::Sub<Self> for Modular<M> {
    type Output = Self;

    fn sub(mut self, rhs: Self) -> Self {
        self -= rhs;
        self
    }
}

impl<M: Modulus> std::ops::MulAssign<Self> for Modular<M> {
    fn mul_assign(&mut self, rhs: Self) {
        let mut value = self.value as u64 * rhs.value as u64;
        let m = M::modulus() as u64;
        if value >= m {
            value %= m;
        }
        self.value = value as u32;
    }
}

impl<M: Modulus> std::ops::Mul<Self> for Modular<M> {
    type Output = Self;

    fn mul(mut self, rhs: Self) -> Self {
        self *= rhs;
        self
    }
}

impl<M: Modulus> std::ops::DivAssign<Self> for Modular<M> {
    fn div_assign(&mut self, rhs: Self) { *self *= rhs.invert().unwrap(); }
}
impl<M: Modulus> std::ops::Div<Self> for Modular<M> {
    type Output = Self;

    fn div(mut self, rhs: Self) -> Self::Output {
        self /= rhs;
        self
    }
}

impl<M: Modulus> Modular<M> {
    /// unlike extgcd, the caller cannot eunsure the inverse exist.
    /// with additional constant run time cost before calling this function.
    /// so if the inverse element does not exit,
    /// handle execption inside the method, and return Result<T, E>
    pub fn invert(self) -> Result<Self, &'static str> {
        if self.value() == 0 {
            // user does not call extgcd directly,
            // so return err instead of panic.
            return Err("0 is not invertible");
        }
        Ok(modular_inverse_extgcd(
            M::modulus() as u64,
            self.value() as u64,
        )?
        .into())
    }
}

macro_rules! define_static_modulus {
    ($typename:ident, $value:expr) => {
        #[derive(Debug, Copy, Clone, PartialEq, Eq, PartialOrd, Ord, Hash)]
        pub struct $typename;

        impl Modulus for $typename {
            fn modulus() -> u32 { $value }
        }
    };
}

define_static_modulus!(Mod998_244_353, 998_244_353);
define_static_modulus!(Mod1_000_000_007, 1_000_000_007);

pub trait Modulus {
    fn modulus() -> u32;
}

/// compute g := \gcd(modulus, n),
/// and modular inverse of n/g in Z_{modulus/g}.
/// we convert parameters to i64 internally.
/// so be careful not to pass modulus > 2^63 because it overflows.
/// it's `trivial` that inverse of 0 is undefined, so if n = 0, it panics.
pub fn euclidean_mod_gcd_inv(modulus: u64, n: u64) -> (u64, u64) {
    assert!(0 < n && n < modulus);
    let (mut a, mut b) = (n as i64, modulus as i64);
    let (mut x00, mut x01) = (1, 0);
    while b != 0 {
        // (x00, x01) = (x01, x00 - a / b * x01);
        // (a, b) = (b, a % b);

        x00 -= a / b * x01;
        std::mem::swap(&mut x00, &mut x01);
        a %= b;
        std::mem::swap(&mut a, &mut b);
    }
    let gcd = a as u64;
    let u = (modulus / gcd) as i64;
    if x00 < 0 {
        x00 += u;
    }
    debug_assert!(0 <= x00 && x00 < u);
    (gcd, x00 as u64)
}

pub fn modular_inverse_extgcd(
    modulus: u64,
    element: u64,
) -> Result<u64, &'static str> {
    let (gcd, inv) = euclidean_mod_gcd_inv(modulus, element);
    if gcd == 1 {
        Ok(inv)
    } else {
        Err("modulus and element are not coprime")
    }
}
