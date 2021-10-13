# [AtCoder ABC221 E - LEQ](https://atcoder.jp/contests/abc221/tasks/abc221_e)


# keywords 
- fix left or right
- query on range
- segment tree
- fenwick tree
- sqrt decomposition


# summary
- if there is a pair $i, j, A_i \le A_j, i \lt j$ denoting the indices of left most value and right most value of a sequence.

- if $i, j$ is selected and the pair satisfy the constraints, the sequence still be good even how we select the sandwiched elements.
- $\therefore 2^{j - i - 1}$ patterns exist.
$$
\therefore \text{answer} := \sum_{i=0}^{N - 2}\sum_{j=i + 1}^{N - 1}
\begin{cases}
0 & (A_i > A_j) \\
2^{j - i - 1} & \text{otherwise}
\end{cases} \\
= \sum_{j=1}^{N - 1}\sum_{i=0}^{j - 1}
\begin{cases}
0 & (A_i > A_j) \\
2^{j - i - 1} & \text{otherwise}
\end{cases} \\
= \sum_{j=1}^{N - 1}\sum_{0 \le i \lt j, A_i \le A_j}{2^{j - i - 1}} \\
= \sum_{j=1}^{N - 1}2^j\sum_{0 \le i \lt j, A_i \le A_j}{2^{-(i + 1)}} 
$$

- $\sum_{0 \le i \lt j, A_i \le A_j}{2^{-(i + 1)}}$ can be calculated $O(\log{N})$ for each $j$ by using fenwick tree, segment tree and so on.

# code 
## sol_0
- numba (JIT)
- fenwick tree


## sol_1
- numba (JIT)
- segment tree



# similar 
