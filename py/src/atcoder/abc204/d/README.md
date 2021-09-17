# [AtCoder ABC204 D - Cooking](https://atcoder.jp/contests/abc204/tasks/abc204_d)



# keywords 
- DP 


# summary
- $dp_{i, j} :=$ can we make any group g from $\{1, 2, ..., i\}$ such that $\sum_{i \in g}T_i = j$ 
- compute minimum $j$ such that $dp_{N, j} = ok \land j \ge \displaystyle{\lceil{\frac{\sum{T}}{2}}\rceil}$


# code 
## sol_0
- numpy
- dp


# summary 