# [AtCoder ABC220 D - FG operation](https://atcoder.jp/contests/abc220/tasks/abc220_d)


# keywords
- DP 
- greedy

# summary 
- $dp_{i, j} :=$ number of cases such that remainder is $j$ by operating $A_0..A_i$
- $dp_{*, *} = 0$
- $dp_{0, A_0} = 1$
- transition
  - $dp_{i, j + A_i} := dp_{i, j + A_i} + dp_{i - 1, j}$
  - $dp_{i, j \times A_i} := dp_{i, j \times A_i} + dp_{i - 1, j}$


- be careful of considering $\mod 10$

# code 
## sol_0
- numba (JIT) 

# similar 
