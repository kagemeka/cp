# [G - Longest Path](https://atcoder.jp/contests/dp/tasks/dp_g)


# keywords 
- DAG (Directed Acyclic Graph)
- DAG -> DP (it could be calculated with DFS)
- topological sort



## sol_0
- DFS 
- dp[u] = max(dp[v]) + 1 (edges[u][v], if v exists)
- dp[u] = 0 (if v not exists) 
- memolization


## sol_1
- BFS (from terminal)
- dp[v] = max(dp[u]) + 1 (edges[u][v] if v exists)
- dp[v] = 0 (if v not exists)


## sol_2
- BFS
- numba (JIT)


## sol_3
- BFS
- numba (AOT)


## tips
- it can also be solve by reversing all edges because the graph is DAG.
- In Numba, recursive closure cannot be understood.