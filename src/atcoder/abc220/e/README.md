# [AtCoder ABC220 E - Distance on Large Perfect Binary Tree](https://atcoder.jp/contests/abc220/tasks/abc220_e)


# keywords
- tree
- complete binary tree
- count up 
- DP
- modular
- combinatorics


# summary 
- considering calculate answer for each subtree
- $N$ is too big to calc all the subtree's answer.
- then, consider calcutating answer for each depth $\because N \le 10^6$
- ret $A_i :=$ answer for depth $i$ subtree. ($0 \le i \le N - 1$) 
- if $A_{i + 1}$ has been calculated,  
  - $A_{i} = 2A_{i + 1} + \sum_{d=0}^{N - 1 - i} f(d)$
    - where $f(d) :=$ number of combinations such that 
      - choose one of nodes depth $= d$ from left childs
      - choose one of nodes depth $= D - d$ 
  - because of symmetricity of ($d, D - d$),
    - $0 \le D - d \le N - 1 - i \leftrightarrow d \le D \land d \ge D - N + 1 + i$
  - $\therefore\ A_{i} = 2A_{i + 1} + \sum_{d=\max{(0, D - N + 1 + i)}}^{\min{(D, N - 1 - i)}} f(d)$
  - $\sum_{d=\max{(0, D - N + 1 + i)}}^{\min{(D, N - 1 - i)}} f(d)$ can be calculated with $O(1)$ by preprocessing cumulative sum ($O(N)$).


- at last, print $2A_0$ (include reverse paths)


# code 
## sol_0
- python


## sol_1
- numba (JIT)

# similar 
