pub fn read<T: std::str::FromStr>() -> T {
    use std::io::Read;
    std::io::stdin()
        .lock()
        .by_ref()
        .bytes()
        .map(|c| c.unwrap() as char)
        .skip_while(|c| c.is_whitespace())
        .take_while(|c| !c.is_whitespace())
        .collect::<String>()
        .parse::<T>()
        .ok()
        .unwrap()
}

pub mod multiplicative_inverse {
    //! extension of std::ops

    pub trait MulInv {
        type Output;
        fn mul_inv(self) -> Self::Output;
    }
}

pub mod pocket_modular {

    pub mod modulus {
        pub trait StaticGet {
            fn get() -> u32;
        }

        #[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
        pub struct Mod1_000_000_007;
        impl StaticGet for Mod1_000_000_007 {
            fn get() -> u32 { 1_000_000_007 }
        }

        #[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
        pub struct Mod998_244_353;
        impl StaticGet for Mod998_244_353 {
            fn get() -> u32 { 998_244_353 }
        }

        #[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
        pub struct StaticMod;

        use std::sync::atomic::{AtomicU32, Ordering::SeqCst};
        impl StaticMod {
            fn cell() -> &'static AtomicU32 {
                static CELL: AtomicU32 = AtomicU32::new(0);
                &CELL
            }

            pub fn set(value: u32) { Self::cell().store(value, SeqCst); }
        }

        impl StaticGet for StaticMod {
            fn get() -> u32 { Self::cell().load(SeqCst) }
        }
    }

    #[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
    pub struct Modint<M>(
        pub u32,
        std::marker::PhantomData<M>,
    );

    use std::ops::*;

    use modulus::StaticGet;

    use crate::multiplicative_inverse::MulInv;

    impl<M: StaticGet> Modint<M> {
        pub fn modulus() -> u32 { M::get() }

        pub fn new(mut v: u32) -> Self {
            if v >= M::get() {
                v %= M::get();
            }
            Self(v, std::marker::PhantomData)
        }
    }

    impl<M: StaticGet> Add for Modint<M> {
        type Output = Self;

        fn add(mut self, rhs: Self) -> Self {
            self.0 += rhs.0;
            if self.0 >= M::get() {
                self.0 -= M::get()
            }
            self
        }
    }

    impl<M: StaticGet> Neg for Modint<M> {
        type Output = Self;

        fn neg(mut self) -> Self {
            if self.0 != 0 {
                self.0 = M::get() - self.0
            }
            self
        }
    }

    impl<M: StaticGet> Mul for Modint<M> {
        type Output = Self;

        fn mul(mut self, rhs: Self) -> Self {
            let mut v = self.0 as u64;
            v *= rhs.0 as u64;
            let m = M::get() as u64;
            if v >= m {
                v %= m;
            }
            self.0 = v as u32;
            self
        }
    }

    impl<M: StaticGet> MulInv for Modint<M> {
        type Output = Self;

        fn mul_inv(mut self) -> Self {
            use std::mem::swap;
            let (mut a, mut b) = (self.0 as i64, M::get() as i64);
            let (mut x00, mut x01) = (1, 0);
            while b != 0 {
                x00 -= a / b * x01;
                a %= b;
                swap(&mut a, &mut b);
                swap(&mut x00, &mut x01);
            }
            assert_eq!(a, 1);
            if x00 < 0 {
                x00 += M::get() as i64;
            }
            debug_assert!(0 <= x00 && x00 < M::get() as i64);
            self.0 = x00 as u32;
            self
        }
    }

    impl<M: StaticGet> Sub for Modint<M> {
        type Output = Self;

        fn sub(self, rhs: Self) -> Self { self + -rhs }
    }

    impl<M: StaticGet> Div for Modint<M> {
        type Output = Self;

        fn div(self, rhs: Self) -> Self { self * rhs.mul_inv() }
    }

    impl<M: StaticGet> AddAssign for Modint<M>
    where
        Self: Copy,
    {
        fn add_assign(&mut self, rhs: Self) { *self = *self + rhs; }
    }

    impl<M: StaticGet> SubAssign for Modint<M>
    where
        Self: Copy,
    {
        fn sub_assign(&mut self, rhs: Self) { *self += -rhs; }
    }

    impl<M: StaticGet> MulAssign for Modint<M>
    where
        Self: Copy,
    {
        fn mul_assign(&mut self, rhs: Self) { *self = *self * rhs; }
    }

    impl<M: StaticGet> DivAssign for Modint<M>
    where
        Self: Copy,
    {
        fn div_assign(&mut self, rhs: Self) { *self *= *self * rhs.mul_inv(); }
    }

    impl<M: StaticGet> From<i64> for Modint<M> {
        fn from(mut v: i64) -> Self {
            let m = M::get() as i64;
            if v < -m || m <= v {
                v %= m;
            }
            if v < 0 {
                v += m;
            }
            Self::new(v as u32)
        }
    }

    impl<M: StaticGet> From<u64> for Modint<M> {
        fn from(mut v: u64) -> Self {
            let m = M::get() as u64;
            if v >= m {
                v %= m;
            }
            Self::new(v as u32)
        }
    }
}

pub mod pocket_combination {
    use crate::multiplicative_inverse::MulInv;
    /// factorial, inverse_factorial, inverse
    pub fn make_tables<T>(size: usize) -> (Vec<T>, Vec<T>, Vec<T>)
    where
        T: From<u64> + Clone + std::ops::Mul<Output = T> + MulInv<Output = T>,
    {
        let mut fact: Vec<T> = (0..size).map(|i| (i as u64).into()).collect();
        fact[0] = 1.into();
        for i in 1..size {
            fact[i] = fact[i - 1].clone() * fact[i].clone();
        }
        let mut ifact: Vec<T> =
            (1..size + 1).map(|i| (i as u64).into()).collect();
        ifact[size - 1] = fact[size - 1].clone().mul_inv();
        for i in 0..size - 1 {
            ifact[i] = ifact[i].clone() * ifact[i + 1].clone();
        }
        let mut inv: Vec<T> = vec![0.into(); size];
        for i in 0..size - 1 {
            inv[i + 1] = fact[i].clone() * ifact[i + 1].clone();
        }
        (fact, ifact, inv)
    }

    pub struct Combination<T> {
        fact: Vec<T>,
        ifact: Vec<T>,
    }

    impl<T> Combination<T>
    where
        T: From<u64> + Clone + std::ops::Mul<Output = T> + MulInv<Output = T>,
    {
        pub fn new(size: usize) -> Self {
            let (fact, ifact, ..) = make_tables(size);
            Self { fact, ifact }
        }

        pub fn npk(&self, n: usize, k: usize) -> T {
            if k < n {
                0.into()
            } else {
                self.fact[n].clone() * self.ifact[n - k].clone()
            }
        }

        pub fn nck(&self, n: usize, k: usize) -> T {
            self.npk(n, k) * self.ifact[k].clone()
        }

        pub fn nhk(&self, n: usize, k: usize) -> T {
            if n == 0 { 0.into() } else { self.nck(n + k - 1, k) }
        }
    }
}

pub mod static_matrix_trait {
    pub trait Shape {
        fn shape() -> (usize, usize);
    }

    pub trait Len {
        fn len() -> usize;
    }

    impl<T: Shape> Len for T {
        fn len() -> usize {
            let (h, w) = Self::shape();
            h * w
        }
    }

    pub trait ElementType {
        type T;
    }
}

pub mod square_matrix_trait {
    pub trait Size {
        fn size() -> usize;
    }
}

pub mod dynamic_matrix_trait {
    pub trait Shape {
        fn shape(&self) -> (usize, usize);
    }
}

pub mod static_matrix {
    use crate::static_matrix_trait::{ElementType, Len, Shape};

    pub struct Matrix<P: ElementType>(Vec<P::T>);

    impl<P: ElementType> Matrix<P> {
        pub fn new<F>(default: F) -> Self
        where
            F: Fn() -> P::T,
            P: Len,
        {
            Self((0..P::len()).map(|_| default()).collect())
        }
    }

    impl<P> Default for Matrix<P>
    where
        P::T: Default,
        P: ElementType + Len,
    {
        fn default() -> Self { Self::new(|| P::T::default()) }
    }

    use std::ops::*;
    impl<P> Index<(usize, usize)> for Matrix<P>
    where
        P: ElementType + Shape,
    {
        type Output = P::T;

        fn index(&self, index: (usize, usize)) -> &Self::Output {
            let (i, j) = index;
            &self.0[i * P::shape().0 + j]
        }
    }

    impl<P> IndexMut<(usize, usize)> for Matrix<P>
    where
        P: ElementType + Shape,
    {
        fn index_mut(&mut self, index: (usize, usize)) -> &mut Self::Output {
            let (i, j) = index;
            &mut self.0[i * P::shape().0 + j]
        }
    }
}

pub mod static_matrix_impl_mul {

    use std::ops::*;

    use crate::{
        square_matrix_trait::Size,
        static_matrix::Matrix,
        static_matrix_trait::{ElementType, Shape},
    };

    /// T should be semiring.
    impl<P> Mul for Matrix<P>
    where
        P: ElementType + Size + Shape,
        P::T: Mul<Output = P::T> + AddAssign + Copy + From<i32>,
        Self: IndexMut<(usize, usize), Output = P::T>,
    {
        type Output = Self;

        fn mul(self, rhs: Self) -> Self::Output {
            let n = P::size();
            let mut res = Self::new(|| 0.into());
            for i in 0..n {
                for j in 0..n {
                    for k in 0..n {
                        res[(i, j)] += self[(i, k)] * rhs[(k, j)];
                    }
                }
            }
            res
        }
    }
}

fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());

    use pocket_modular::*;

    use crate::multiplicative_inverse::*;
    // type Mint = Modint<modulus::Mod998_244_353>;
    // type Mint = Modint<modulus::Mod1_000_000_007>;
    type Mint = Modint<modulus::StaticMod>;
    modulus::StaticMod::set(1_000_000_007);

    let mut a = Mint::new(100);
    a = Mint::new(2).mul_inv();
    println!("{:?}", a.0);

    use crate::{
        square_matrix_trait::Size,
        static_matrix_trait::{ElementType, Shape},
    };

    pub struct MatrixPropI6422;

    impl Size for MatrixPropI6422 {
        fn size() -> usize { 2 }
    }

    impl Shape for MatrixPropI6422 {
        fn shape() -> (usize, usize) { (Self::size(), Self::size()) }
    }

    impl ElementType for MatrixPropI6422 {
        type T = i64;
    }
}

// TODO:
// boyermoore
// rabin karp
