# [AtCoder ABC047 C - 一次元リバーシ](https://atcoder.jp/contests/abc047/tasks/arc063_a)


# keywords 
- greedy


# summary
$$
\text{answer} = \sum_{i=1}^{N - 1}
\begin{cases}
1 & (S_i \neq S_{i + 1}) \\
0 & \text{otherwise}
\end{cases}
$$
- $\because$ we can reverse at most one consecutive same color sequence per operation.

# code 
## sol_0
- python 


# similar