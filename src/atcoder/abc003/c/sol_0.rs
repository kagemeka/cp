
pub fn readline() -> String {
    let mut buf: String = String::new();
    std::io::stdin().read_line(&mut buf).unwrap();
    buf
}

pub fn read_int() -> i64 {
    readline().trim().parse::<i64>().unwrap()
}


#[derive(Default)]
pub struct Scanner {
    buffer: Vec<String>,
}

/// example
/// let mut scanner: Scanner = Scanner::default();
/// let a: i32 = scanner.next::<i32>();
impl Scanner {
    pub fn scan<T: std::str::FromStr>(&mut self) -> T 
    where 
        <T as std::str::FromStr>::Err: std::fmt::Debug,
    {
        loop {
            if let Some(token) = self.buffer.pop() {
                return token.parse::<T>().unwrap();
            }
            self.buffer = 
                readline()   
                .trim()
                .split_whitespace().rev()
                .map(String::from)
                .collect();
        }
    }

    pub fn i32(&mut self) -> i32 {
        self.scan::<i32>()
    }

    pub fn string(&mut self) -> String {
        self.scan::<String>()
    }
}


pub fn scan<T: ::std::str::FromStr>() -> T {
    use std::io::Read;
    std::io::stdin().lock().bytes().map(|c|c.unwrap()as char)
    .skip_while(|c|c.is_whitespace())
    .take_while(|c|!c.is_whitespace())
    .collect::<String>().parse::<T>().ok().unwrap()
}


use std::io::Write;
/// let out = &mut std::io::BufWriter::new(std::io::stdout());


// #[allow(warnings)]
fn main() {
    let mut sc = Scanner::default();
    let n = sc.i32();
    let k = sc.i32();
    let mut r = vec![0; n as usize];
    for i in 0..n as usize {
        r[i] = sc.i32();
    }
    let mut rate: f32 = 0f32;
    r.sort();
    for i in (n - k) as usize..n as usize {
        rate = (rate + r[i] as f32) / 2.0;
    }
    println!("{:.16}", rate);
}