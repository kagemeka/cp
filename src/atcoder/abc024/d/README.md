# [AtCoder ABC024 D - 動的計画法](https://atcoder.jp/contests/abc024/tasks/abc024_d)


# keywords 
- math 
- equation


# summary
$$
A := \displaystyle{(r + c)\choose{c}} = \displaystyle{\frac{(r + c)!}{r!c!}} \\
B := \displaystyle{(r + c + 1)\choose{r}} = \displaystyle{\frac{(r + c + 1)!}{r!(c + 1)!}} \\
C := \displaystyle{(r + c + 1)\choose{c}} = \displaystyle{\frac{(r + c + 1)!}{(r + 1)!c!}} \\
\therefore
r = \displaystyle{\frac{yz - xz}{x(y + z) - yz}}, 
c = \displaystyle{\frac{yz - xy}{x(y + z) - yz}}
$$



# code 
## sol_0, sol_1
- python
- Mint


## sol_1
- numba (JIT)



# similar 
