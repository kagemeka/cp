# [F - Dist Max 2](https://atcoder.jp/contests/abc215/tasks/abc215_f)



# keywords 
- `minimum of maximum` or `maximum of minimum` -> binary search
- brute force
- greedy
- scanline algorithm
- cummulative minimum/maximum
- shakutori method
- binary search



# summary
- let $d := \max_{i, j}({\min{(|x_i - x_j|, |y_i - y_j|)})}$ 
- sort x, y by x
- precalc cummax, cummin of y.
- binary search $d$
  - $\max_{i, j}({\min{(|x_i - x_j|, |y_i - y_j|)})} \ge d$
  $\leftrightarrow \exists{i, j}\ \min{(|x_i - x_j|, |y_i - y_j|)} \ge d$
  - furthermore, if fix $j$ and filter $i$ so that $x_j - x_i \ge d$, 
    this is equivalent to $\exists{i, j}\ x_j - x_i \ge d, |y_i - y_j| \ge d$
    - this is calculated with $O(N)$ time complexity 
      by precalc cummin/cummax of y and using shakutori method,
      because it's enough to check $cummax_{y_j}$ or $cummin_{y_j}$ when $i$ is fixed.
    - also, we can use binary search instead of shakutori method, 
      with $O(N\log{N})$ time complexity
      


## sol_0
- $O(N\log{N}\log{\max{d}})$
- bisection
- pypy


## sol_1
- $O(N(\log{N} + \log{\max{d}}))$
- shakutori method
- pypy



## sol_2
- $O(N\log{N}\log{\max{d}})$
- bisection
- numba (JIT)


## sol_3
- $O(N(\log{N} + \log{\max{d}}))$
- shakutori method
- numba (JIT)


## sol_4
- $O(N\log{N}\log{\max{d}})$
- bisection
- numpy



# similar
- [ABC149 E - Handshake](https://atcoder.jp/contests/abc149/tasks/abc149_e)