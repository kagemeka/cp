

fn main() {
    let a: usize = 1; 
    a.next_power_of_two();
    a.next_power_of_two();
    a.next_power_of_two();
  
    let b = [1, 2, 3];
    b.len();
    let c: u64 = 2;
    println!("{}", (c - 2).next_power_of_two());
    a.next_power_of_two();
  
    let a: Option<i32> = Some(5);
    // a.is_some();
    
    let mut s: String = String::from("abc");
    let s1 = s;
    s = s1;
    // let a = &&s;
    println!("{}", s1);
    println!("{}", s);
    
}