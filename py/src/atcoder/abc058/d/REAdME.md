# [AtCoder ABC058 D - 井井井](https://atcoder.jp/contests/abc058/tasks/arc071_b)


# keywords 
- math 
- sumation


# summary 
$$
\text{answer} = \sum_{i=0}^{N-2}\sum_{j=i+1}^{N-1}\sum_{k=0}^{M-2}\sum_{l=k+1}^{M-1}(y_j - y_i)(x_l - x_k) \\
= \sum_{i=0}^{N-2}\sum_{j=i+1}^{N-1}(y_j - y_i)\sum_{k=0}^{M-2}\sum_{l=k+1}^{M-1}(x_l - x_k) \\
= S_yS_x
$$
$$
S_y = \sum_{i=0}^{N-2}\sum_{j=i+1}^{N-1}(y_j - y_i) \\
= \sum_{i=0}^{N-2}\sum_{j=i+1}^{N-1}y_j - \sum_{i=0}^{N-2}\sum_{j=i+1}^{N-1}y_i \\
= \sum_{j=1}^{N-1}y_j\sum_{i=0}^{j-1} - \sum_{i=0}^{N-2}y_i\sum_{j=i+1}^{N-1} \\
= \sum_{j=1}^{N-1}y_jj - \sum_{i=0}^{N-2}y_i(N - 1 - i) \\
= \sum_{i=0}^{N-2}{y_{i + 1}(i + 1) - y_i(N - 1 - i)}
$$
- $S_y = \sum_{i=0}^{N-2}{y_{i + 1}(i + 1) - y_i(N - 1 - i)}$
- $S_x = \sum_{i=0}^{M-2}{x_{i + 1}(i + 1) - x_i(M - 1 - i)}$
- answer = $S_yS_x$

# code 
## sol_0
- numba (JIT)



# similar 
