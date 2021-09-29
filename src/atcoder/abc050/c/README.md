# [AtCoder ABC050 C - Lining Up](https://atcoder.jp/contests/abc050/tasks/arc066_a)



# keywords 
- math 
- bincount 


# summary 
- check satisfy the condition below
  - if $N$ is odd. $\forall{2 \le 2k \le N - 1}, \text{bin}(2k) = 2 \land \text{bin}(0) = 1$
  - otherwise, $\forall{1 \le 2k - 1 \le N - 1}, \text{bin}(2k) = 2$
- it's satisfied, answer = $2^{\lfloor\displaystyle{\frac{N}{2}}\rfloor}$


# code 
## sol_0
- numba (JIT)

# similar 

