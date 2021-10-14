# [AtCoder ARC122 A - Many Formulae](https://atcoder.jp/contests/arc122/tasks/arc122_a)




# keywords 
- DP
- count up 
- fibonacci 
- combinations
  - mathematic independence  
- modular



# summary 
## solution 1
- $dp_{i, 0} :=$ answer for $A_1, A_2, ... A_i$ (last sign is negative)
- $dp_{i, 1} :=$ answer for $A_1, A_2, ... A_i$ (last sign is positive)
- precalc fibonacci sequence $f, f_0 = 0, f_1 = 1$
- $dp_{0, j} = 0$
- transition
  - $dp_{i, 0} = dp_{i - 1, 1} - f_{i - 1}a_i$
  - $dp_{i, 1} = dp_{i - 1, 0} + dp_{i - 1, 1} + f_ia_i$
- answer = $dp_{N, 0} + dp_{N, 1}$

## solution 2
- $dp_{i, 0} :=$ number of sequences producted from $i$ '+-', and last sign is '-'.
- $dp_{i, 1} :=$ number of sequences producted from $i$ '+-', and last sign is '+'.
- $dp_{0, 1} := 1, dp_{0, 0} := 0$
- let $sdp_{i} := dp_{i, 0} + dp_{i, 1}$
- answer = $A_1sdp_{N - 1} + \sum_{i=2}^{N}{(A_isdp_{i - 2}sdp_{N - i} - A_idp_{i - 2, 1}dp_{N  - i, 1})}$



# code 
## sol_0
- numba (JIT)
- solution 1
- DP
- fibonacci 


## sol_1
- numba (JIT)
- solution 2
- DP
- count up
- independence 


# similar 
