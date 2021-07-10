fn main()
{
  use std::io::stdin;
  let s = stdin();
  let mut n= String::new();
  s.read_line(&mut n).unwrap();
  let n: i64 = 
    n
    .trim()
    .parse()
    .unwrap();
  println!("{}", n);
  println!("{}", n);
  for _ in 0..n-1 {
    let mut l = String::new();
    s.read_line(&mut l).unwrap();
    let l: Vec<i64> = 
      l
      .trim()
      .split_whitespace()
      .map(|x| {
        x.parse().unwrap()
      }).collect();
    println!(
      "{:?}",
      l,
    );
  }

  
}


