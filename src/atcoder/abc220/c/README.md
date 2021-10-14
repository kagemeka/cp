# [AtCoder ABC220 C - Long Sequence](https://atcoder.jp/contests/abc220/tasks/abc220_c)


# keywords
- cumsum
- binary search
- greedy
- math


# summary 
- $S_i := \sum_{j=0}^{i}A_j$
- find $i$ such that 
  - $X = qS_{N - 1} + r (0 \le r \lt S_{N - 1})$
  - $S_i \gt r$
- answer = $Nq + i + 1$

# code 
## sol_0
- numba (JIT)



# similar 
