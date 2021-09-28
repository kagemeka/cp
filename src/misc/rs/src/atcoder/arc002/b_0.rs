// use std::io;


fn main()
{
  // let mut s = io::stdin();

  // let mut st = String::new();
  // s.read_to_string(&mut st).unwrap();
  // println!(
  //   "{}",
  //   st,
  // );
  let s = IO::readline();
  println!(
    "{}",
    s,
  );
  let b = s.split_whitespace().next().is_none();
  println!(
    "{:?}",
    b,
  );
  let a: Vec<&str> = s.split_whitespace().collect();
  println!(
    "{:?}",
    a,
  );
}


// fn read_int() -> i64 {
//   let n = readline();
//   let n: i64 = n.trim().parse()
//     .expect("");
//   n
// }


// fn readline() -> String {
//   use std::io;
//   let s = io::stdin();
//   let mut buf = String::new();
//   s.read_line(&mut buf)
//     .expect("");
//   buf
// }



struct IO;


impl IO
{
  pub fn readline()
  -> String
  {
    use std::io::{
      stdin,
      Read,
    };
    let mut s = stdin();
    let mut buf = 
      String::new();
    s
    .read_to_string(&mut buf)
    .unwrap(); 
    buf
    .trim()
    .to_string()
  }  
} 


use std::str::SplitWhitespace;

pub struct Reader<'a>
{
  pub buf: Box<SplitWhitespace<'a>>
}




impl Reader<'_>
{
  pub fn new() -> Reader<'static>
  {
    use std::io::{
      stdin,
      Read,
    };
    let mut s = stdin();
    let mut buf = 
      String::new();
    s
    .read_to_string(&mut buf)
    .unwrap();
    let buf = buf
    .trim()
    .to_string();
    let a = buf.split_whitespace();
    Reader {
      buf: Box(a)
    }
  }
}
    