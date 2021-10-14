# [AtCoder ABC156 E - Roaming](https://atcoder.jp/contests/abc156/tasks/abc156_e)



# keywords
- combinatorics
- $N\choose{k}$
- $_NH_k$
- count up 
- modular 



# summary 
- consider final state.
- if $k \ge n - 1$, it should satisfy all the states.
- so consider $i \le \min(k, n - 1)$
- $\forall{i \le \min(k, n - 1)}$, 
  - choose $i$ people from N,
  - move them to any of $N - i$ rooms except choosen $i$ rooms.
  


# code 
## sol_0
- numba (JIT)
- all states $-$ complementary states

## sol_1
- numba (JIT)
- count up directly.



# similar 
