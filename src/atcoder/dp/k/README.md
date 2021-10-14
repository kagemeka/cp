# [K - Stones](https://atcoder.jp/contests/dp/tasks/dp_k)



# keywords 
- Game Theory
- DAG 



## sol_0
- DFS 
- dp[x] = any(dp[x - i]) (for i in a, if x - i >= 0)


## sol_1
- BFS
- give dp[x] to dp[x + i] from small x step by step.
- standard


## sol_2
- BFS
- numba (JIT)


## sol_3
- BFS
- numba (AOT)


## sol_4
- BFS 
- numpy + numba (JIT)


## sol_5
- BFS
- numpy + numba (AOT)
