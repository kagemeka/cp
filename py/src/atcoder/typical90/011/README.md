# [AtCoder Typical90 011 - Gravy Jobs（★6）](https://atcoder.jp/contests/typical90/tasks/typical90_k)



# keywords 
- range scheduling problem
- sort by end in ascending order.
- DP


# summary
- sort $D, C, S$ by $D$ in ascending order.
- let $dp_{i, j} :=$ maximum score by doing some jobs from $1, 2, ...i$ and the day in which the last job finised is $j$
- initialize $dp_{*, *} = 0$
- transision
  - $\forall{C_i \le k \le D_i}$
    - $dp_{i, k} = \max{(dp_{i - 1, k}, dp_{i - 1, k - C_i} + S_i)}$



# code 
## sol_0
- numba (JIT)
- efficient memory space 


# similar 


