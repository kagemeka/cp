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

// def path_based(
//     g: typing.List[typing.List[int]],
// ) -> typing.List[typing.List[int]]:
//     n = len(g)
//     st = []
//     st_low = []
//     state = [0] * n
//     scc = []
//     st_dfs = list(range(n))[::-1]
//     while st_dfs:
//         u = st_dfs.pop()
//         if u < 0:
//             i = state[~u] - 1
//             if st_low[-1] != i + 1:
//                 continue
//             scc.append(st[i:])
//             del st[i:]
//             st_low.pop()
//             for v in scc[-1]:
//                 state[v] = -1
//         elif state[u] > 0:
//             while st_low[-1] > state[u]:
//                 st_low.pop()
//         elif state[u] == 0:
//             st.append(u)
//             st_low.append(len(st))
//             state[u] = st_low[-1]
//             st_dfs.append(~u)
//             st_dfs.extend(g[u])
//     return scc[::-1]

pub fn path_based(adj_list: Vec<Vec<usize>>) -> Vec<Vec<usize>> {
    let g = adj_list;
    let n = g.len();
    let mut st = vec![];
    let mut st_low = vec![];
    let mut state = vec![0; n];
    let mut scc = vec![];
    let mut st_dfs: Vec<isize> = (0..n as isize).rev().collect();
    while let Some(u) = st_dfs.pop() {
        if u < 0 {
            let i = state[!u as usize] - 2;
            if *st_low.last().unwrap() != i {
                continue;
            }
            scc.push(st[i..].to_vec());
        }
    }

    scc
}

fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
}
