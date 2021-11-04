pub struct Scanner<R: std::io::Read> {
    reader: R,
}

impl<R: std::io::Read> Scanner<R> {
    /// let stdin = std::io::stdin();
    /// let mut sc = Scanner::new(stdin.lock());
    pub fn new(reader: R) -> Self { Self { reader: reader } }

    pub fn scan<T: std::str::FromStr>(&mut self) -> T {
        use std::io::Read;
        self.reader.by_ref().bytes().map(|c| c.unwrap() as char)
        .skip_while(|c| c.is_whitespace())
        .take_while(|c| !c.is_whitespace())
        .collect::<String>().parse::<T>().ok().unwrap()
    }
}


// #[allow(warnings)]
fn main() {
    use std::io::Write;
    let stdin = std::io::stdin();
    let mut sc = Scanner::new(std::io::BufReader::new(stdin.lock()));
    let stdout = std::io::stdout();
    let out = &mut std::io::BufWriter::new(stdout.lock());  


    let s: String = sc.scan();
    let a = s.chars().map(|i| i as usize).collect::<Vec<usize>>();
    let sa = sa_is(&a);
    for i in 0..a.len() {
        write!(out, "{}", sa[i]).unwrap();
        write!(out, "{}", if i < a.len() - 1 { ' ' } else { '\n' }).unwrap();
    }
}


pub fn sa_is(a: &Vec<usize>) -> Vec<usize> {
    assert!(a.len() > 0);
    let mn = *a.iter().min().unwrap();
    let mut a = a.iter().map(|x| x - mn + 1).collect::<Vec<usize>>();
    a.push(0);
    let n = a.len();
    let m = a.iter().max().unwrap() + 1;
    let mut is_s = vec![true; n];
    let mut is_lms = vec![false; n];
    let mut lms = Vec::with_capacity(n);
    for i in (1..n).rev() {
        is_s[i - 1] = if a[i - 1] == a[i] { is_s[i] } else { a[i - 1] < a[i] };
        is_lms[i] = !is_s[i - 1] && is_s[i];
        if is_lms[i] { lms.push(i); }
    }
    lms.reverse();
    let mut bucket = vec![0usize; m];
    for &x in a.iter() { bucket[x] += 1; }

    let induce = |lms: &Vec<usize>| -> Vec<usize> {
        let mut sa = vec![n; n];
        let mut sa_idx = bucket.clone();
        
        for i in 0..m - 1 { sa_idx[i + 1] += sa_idx[i]; }
        for &i in lms.iter().rev() { 
            sa_idx[a[i]] -= 1;
            sa[sa_idx[a[i]]] = i;
        }

        sa_idx = bucket.clone();
        let mut s = 0usize;
        for i in 0..m { sa_idx[i] += s; std::mem::swap(&mut s, &mut sa_idx[i]); }
        for i in 0..n {
            if sa[i] == n || sa[i] == 0 { continue; } 
            let i = sa[i] - 1;
            if !is_s[i] { sa[sa_idx[a[i]]] = i; sa_idx[a[i]] += 1; }
        }
        
        sa_idx = bucket.clone();
        for i in 0..m - 1 { sa_idx[i + 1] += sa_idx[i]; }
        for i in (0..n).rev() {
            if sa[i] == n || sa[i] == 0 { continue; }
            let i = sa[i] - 1;
            if is_s[i] { sa_idx[a[i]] -= 1; sa[sa_idx[a[i]]] = i; }
        }
        sa
    };

    let sa = induce(&lms);
    let mut lms_idx = Vec::with_capacity(n);
    let mut rank = vec![n; n];
    for &i in sa.iter() { if is_lms[i] { lms_idx.push(i); }; }
    let l = lms_idx.len();
    let mut r = 0usize;
    rank[n - 1] = r;
    for i in 0..l - 1 {
        let j = lms_idx[i];
        let k = lms_idx[i + 1];
        for d in 0..n {
            let j_is_lms = is_lms[j + d];
            let k_is_lms = is_lms[k + d];
            if a[j + d] != a[k + d] || j_is_lms ^ k_is_lms { r += 1; break; }
            if d > 0 && j_is_lms | k_is_lms { break; }
        } 
        rank[k] = r;
    }
    rank = rank.into_iter().filter(|&x| x != n).collect();
    let mut lms_order: Vec<usize> = Vec::new();
    if r == l - 1 { 
        lms_order.resize(l, n);
        for i in 0..l { lms_order[rank[i]] = i; }
    } else {
        lms_order = sa_is(&rank);
    }
    lms = lms_order.iter().map(|&i| lms[i]).collect();
    let sa = induce(&lms);
    sa[1..].to_vec()
} 

