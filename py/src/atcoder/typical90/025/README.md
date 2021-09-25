# [AtCoder Typical90 025 - Digit Product Equation（★7）](https://atcoder.jp/contests/typical90/tasks/typical90_y)


# keywords 
- brute force 
- enumerate minority


# summary 
- enumerate $f(x)$
- number of $f(x)$ is count of repeated combinations.
  - that is at most $_{10}H_{11} = _{20}C_{11} = 167960$ patterns
- there is only one $x$ corresponding to $f(x)$ even if there exists such a $x$.
  - $\because x - f(x) = B \leftrightarrow x = f(x) + B$
- $x := fx + B$
- $\forall{x}$
  - check $1 \le x \le N \land x - f(x) = B$

# code 

## sol_0, sol_2 
- numba (JIT)
- enumerate fx with BFS and np.unique 

## sol_1
- numpy
- enumerate fx with BFS and np.unique


# similar 
