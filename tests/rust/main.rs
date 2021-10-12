// use std::alloc;


fn main() {
  let a: usize = 1; 
  a.next_power_of_two();
  a.next_power_of_two();

  let b = [1, 2, 3];
  b.len();
  let c: u64 = 2;
  println!("{}", (c - 2).next_power_of_two());
  a.next_power_of_two();

}