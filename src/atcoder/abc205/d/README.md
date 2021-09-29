# [AtCoder ABC205 D - Kth Excluded](https://atcoder.jp/contests/abc205/tasks/abc205_d)




# keywords 
- binary search



# summary 
- call target values as good values.
- let $A_0 = 0$
- $b_i :=$ means the first good value more than $A_i$ is $b_i$ th good value.
- let $j := \text{bisect-right}(b, k_i) - 1$
  - answer := $A_j + 1 + k_i - b_j$


# code 
## sol_0
- numba (JIT)
