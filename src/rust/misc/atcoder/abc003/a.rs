#[allow(unused_imports)]
use std::{
  cmp::{min, max},
  io::{
    BufWriter,
    stdin,
    stdout,
    Write
  },
};


#[derive(Default)]
struct Scanner {
  buffer: Vec<String>,
}

impl Scanner {
  fn scan<T: std::str::FromStr>(
    &mut self,
  ) -> T {
    loop {
      if let Some(token) = 
      self.buffer.pop() {
        return {
          token.parse().ok()
          .expect("Failed parse")
        };
      }
      let mut input = String::new();
      stdin().read_line(
        &mut input,
      ).expect("Failed read");
      self.buffer = input
        .split_whitespace().rev()
        .map(String::from)
        .collect();
    }
  }
}


fn solve() {
  let writer = &mut BufWriter::new(
    stdout());
}

fn main() {
  let mut sc = Scanner::default();
  let n: u32 = sc.scan();
  solve(n);
}