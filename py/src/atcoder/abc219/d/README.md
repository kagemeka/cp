# [AtCoder ABC219 D - Strange Lunchbox](https://atcoder.jp/contests/abc219/tasks/abc219_d)


# keywords
- DP
- mincost if achievable otherwise -1


# summary 
- $dp_{i, j, k} :=$ minimumcost to achieve $(j, k)$ by using any of $\{1, 2, ... i\}$
- $dp_{i, \min{(j + A_i, X)}, \min{(k + B_i, Y)}} := 
  \min{(dp_{i - 1, j, k} + 1, dp_{i - 1, \min{(j + A_i, X)}, \min{(k + B_i, Y)}})}$


# code 
## sol_0
- numba (JIT)


# similar 