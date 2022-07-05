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

use std::ops::*;
type G<T> = Vec<Vec<T>>;

pub fn floyd_warshall<T, F>(adj_mat: G<T>, f: F) -> G<T>
where
    G<T>: IndexMut<usize, Output = [T]>,
    T: Clone,
    F: Fn(T, T, T) -> T,
{
    let mut g = adj_mat;
    let n = g.len();
    for k in 0..n {
        for i in 0..n {
            for j in 0..n {
                g[i][j] = f(
                    g[i][j].clone(),
                    g[i][k].clone(),
                    g[k][j].clone(),
                );
            }
        }
    }
    g
}

fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
}
