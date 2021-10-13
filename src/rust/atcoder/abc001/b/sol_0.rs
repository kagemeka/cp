use std::


#[allow(unused_imports)]
use std::{
  cmp::{min, max},
  io::{BufWriter, stdin, stdout, Write},
};


#[derive(Default)]
struct Scanner {
  buffer: Vec<String>,
}

impl Scanner {
  fn next<T: std::str::FromStr>(&mut self) -> T {
    loop {
      if let Some(token) = 
      self.buffer.pop() {
        return {token.parse().unwrap()};
      }
      let mut input = String::new();
      stdin().read_line(&mut input).unwrap();
      self.buffer = input
        .split_whitespace().rev()
        .map(String::from)
        .collect();
    }
  }
}


fn solve() {
}


fn main() {
  let mut sc = Scanner::default();
  let out = &mut BufWriter::new(std::io::stdout());

}