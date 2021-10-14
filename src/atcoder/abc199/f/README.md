# [AtCoder ABC199 F - Graph Smoothing](https://atcoder.jp/contests/abc199/tasks/abc199_f)

# keywords 
- matrix doubling 
- modular 
- probability
- expectation


# summary
- by doing an operation, how each node's value is changed?
- $A_{i, j} = g_{j, 0}A_{i - 1, 0} + g_{j, 1}A_{i - 1, 1} + ... + g_{j, N - 1}A_{i - 1, N}$
- these polynomial equation can be expressed as matrix at onece.
  - because $g_{j, k}$ should always same.
- $$
  \begin{bmatrix}A_{i, 0} \\ A_{i, 1} \\ ... \\ A_{i, N - 1}\end{bmatrix}
  = \begin{bmatrix}
    g_{0, 0} & g_{0, 1} & ... & g_{0, N - 1} \\
    g_{1, 0} & g_{1, 1} & ... & g_{1, N - 1} \\
    ... & ... & ... & ... \\
    g_{N - 1, 0} & g_{N - 1, 1} & ... & g_{N - 1, N - 1} \\
    \end{bmatrix}
    \cdot
    \begin{bmatrix}
    A_{i - 1, 0} \\ A_{i - 1, 1} \\ ... \\ A_{i - 1, N - 1}
    \end{bmatrix}
  $$
- that is $A_i = GA_{i - 1}$
- G is constant matrix, thus $G^k$ can be calculated with complexity $O(N^3\log{k})$. 



# code 
## sol_0, sol_1
- numpy


## sol_2
- numba (JIT)



# similar
- [AtCoder ABC013 D - 阿弥陀](https://atcoder.jp/contests/abc013/tasks/abc013_4)