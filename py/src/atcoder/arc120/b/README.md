# [AtCoder ARC120 B - Uniformly Distributed](https://atcoder.jp/contests/arc120/tasks/arc120_b)




# keywords 
- bruteforce
- greedy
- count up 
- modular



# summary
- $\forall{p \in \{2, ... H + W\}}$
  - $\forall{i, j, i + j = p, 1 \le i \le H, 1 \le j \le W}$ $S_{i, j}$ all must be same.
  - let $ans = 1$
  - if $S_{i, j}$ all are '.', $ans = ans \times 2$
  - else if  $\exist{i_1, j_1, i_2, j_2} S_{i_i, j_1} = R \land S_{i_2, j_2} = B$, $ans = ans \times 0$
  - otherwise do nothing.


# code 
## sol_0
- numba (JIT)



# similar 