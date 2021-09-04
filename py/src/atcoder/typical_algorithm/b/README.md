# [AtCoder Typical Algorithm B - 区間スケジューリング問題](https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_b)


# keywords 
- interval scheduling problem 
- greedy



# summary 
- sort L, R by R
- if current task is done, decide next task from candidates as the completion date of it is earlest.
- $O(N\log{N})$


# code 
## sol_0
- numba (JIT)
