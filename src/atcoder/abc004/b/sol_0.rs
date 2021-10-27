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

/// ```
/// let mut sc: Scanner = Scanner::default();
/// let a: i32 = sc.scan::<i32>();
/// ```
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

use std::vec::*;
// #[allow(warnings)]
fn main() {
    let n = 4usize;
    let mut board: Vec<Vec<char>> = vec![vec!['a'; n]; n];
    for i in 0..n {
        for j in 0..n {
            board[i][j] = scan();
        }
    }
    board.reverse();
    for i in 0..n {
        println!("{}", board[i].iter().rev().map(|c| c.to_string()).collect::<Vec<_>>().join(" "));
    }
}
