# [AtCoder ABC220 F - Distance Sums 2](https://atcoder.jp/contests/abc220/tasks/abc220_f)


# keywords
- DFS
- tree
- Euler Tour
- tree DP

# summary 
- let $A_i := \sum_{j=0}^{N - 1} d_{i, j}$
- $d_{i, i} := 0$
- at first calc $A_0$ with tree DFS $O(N)$
- for each node $u$, let $p := \text{parent}(u)$ and if A_p has been calculated correctly,
  - let $A\prime_{p} = A_p - A\prime_u - \text{size}(u)$
  - $A_u = A\prime_{u} + A\prime_{p} + (N - \text{size}(u)) = A_p - N - 2\text{size}(u)$
    - where $\text{size}(u) :=$ size of subtree $u$
  - for each node $A_u$ can be calculated with $O(1)$


# code 
## sol_0
- numba (JIT)


# similar 
