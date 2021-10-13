# [AtCoder ABC023 D - 射撃王](https://atcoder.jp/contests/abc023/tasks/abc023_d)


# keywords 
- binary search maximum border


# summary
- fix max border $H$.
- $\forall{i}$
  - if shot balloon $i$ at $t_i$, $h_i + t_is_i \le H \leftrightarrow t_i \le \frac{H - h_i}{s_i} \leftrightarrow t_i = \lfloor\frac{H - h_i}{s_i}\rfloor$
  - thus calculate $t_i := \lfloor\frac{H - h_i}{s_i}\rfloor$
- sort $t$
- $\forall{i}$
  - check $t_i \le i$
  

# code 
## sol_0
- numpy 


## sol_1
- numba (JIT) 

# similar 
