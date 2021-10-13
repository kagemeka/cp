# [AtCoder ABC013 C - 節制](https://atcoder.jp/contests/abc013/tasks/abc013_3)


# keywords 
- math
- inequality
- brute-force


# summary 
- consider constraints
  - $H + Bx + Dy - (N - x - y)E \gt 0 \leftrightarrow$
    $y \gt \frac{NE - H - (B + E)x}{D + E}$
  - $0 \le x, y, x + y \le N$
  - minimize $Ax + Cy$
- if we fix $x (0 \le x \le N)$, calculating $y$ is easy.
- be careful of the case $y \lt 0$ or $N \lt y$
  - if $N \lt y$, there is no pair $(x, y)$ satisfying all constraints.
  - if $y \lt 0$, the pair $(x, 0)$ satisfies the condition.


# code 
## sol_0
- numpy

## sol_1
- numba (JIT)


# similar 