# [AtCoder ABC216 F - Max Sum Counting](https://atcoder.jp/contests/abc216/tasks/abc216_f)



# keywords 
- DP 
- Subset Sum Problem 
- count up
- greedy



# summary 
- count up patterns for each $i$ such that $A_i = \max_{j \in S}{A_j}$ and $A_i \ge \sum_{j \in S}B_j$, with DP.
- sort A and B by A.
- define a DP
  $dp_{i, j} :=$ the number of patterns that is, $\sum_S{(\sum_{k \in S}B_k = j)}$ where S denotes each subset such that $\forall{k \in S}, A_k \le A_i$
- then, answer = $\sum_{i=1}^{n} \sum_{j=0}^{A_i - B_i} dp_{i - 1, j}$


# sol_0
- numba (JIT)


## sol_1, sol_2, sol_3
- numba (JIT)
- with less memory space complexity


## sol_4
- numpy
- with less memory space complexity



# similar
- [AtCoder ABC214 F - Substrings](https://atcoder.jp/contests/abc214/tasks/abc214_f)
