# [B - Electric Board](https://atcoder.jp/contests/arc119/tasks/arc119_b)



# keywords 
- string 
- S -> T (possible ? minimum count of operations : -1)
- math 
- greedy



# summary
- consider move each 0 left or right or stay.
- let $f_S(i) := S_i = 0 \land \text{count of } 0 \in \{S_0, S_1, ... S_i\}$
- if $f_S(i) \lt f_T(i), S_i$ should move left
- if $f_S(i) = f_T(i), S_i$ should stay
- if $f_S(i) \gt f_T(i), S_i$ should move right
- this is denoted as below
  - $ll..lsrr..rsl...$ or $rr..rsll..lsrr...$
  - each $l$, $s$, $r$ means that $S_i$ should move left, stay, or move right ($S_i = 0$)
- if $S_i$ should move left, at first, move the leftmost $S_i$ in continuous $l$.
- if $S_i$ should move right, at first, move the rightmost $S_i$ in continuous $r$.
- this is optimal movements.



# code 
## sol_0
- numba (JIT)

