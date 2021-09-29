# [AtCoder ABC041 D - 徒競走](https://atcoder.jp/contests/abc041/tasks/abc041_d)


# keywords 
- bits DP 
- brute force 
- greedy
- permutations DP -> check whether it's possible to replace with bits DP.
  - Set info (+ last bit)


# summary 
- $O(2^NN)$
- $dp_S =$ number of topological sorting of a set $S$ 
- $dp_\phi = 1$
- $dp_S = \sum_{v \in S}{
  \begin{cases}
  dp_{S - v} & \text{if } \forall{w \in {S - v}}\ w \text{ is not necessarily after } v \\
  0 & \text{otherwise} \\
  \end{cases}
  }$
- ans = $dp_{\{0, 1, ..., N - 1\}}$


# code 
## sol_0, sol_1
- numba (JIT)


# similar 
