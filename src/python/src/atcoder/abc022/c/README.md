# [AtCoder ABC022 C - Blue Bird](https://atcoder.jp/contests/abc022/tasks/abc022_c)


# keywords 
- floyd washall
- prohibited edges.
- shoretest path


# summary 
- remove node $0$ and do floyd washall
- answer = $\min_{1 \le i \lt j \le N - 1} dist_{0, i} + dist_{i, j} + dist_{j, 0}$

# code 
## sol_0
- numba (JIT)

# similar 


