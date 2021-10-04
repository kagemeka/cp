# [AtCoder ABC143 E - Travel by Car](https://atcoder.jp/contests/abc143/tasks/abc143_e)


# keywords 
- DP
- floyd warshall
- create another graph from shortest dist matrix of original graph.


# summary
- at first, compute all to all shortest dist with Floyd-Warshall algorithms
- create a new graph from the shortest dist matrix.
  - if $\text{dist}_{i, j} \le L$, add edge $i$ to $j$ with cost $1$.
- apply second floyd-warshall to the graph.


# code 
## sol_0
- numba (JIT)
- dijkstra 
- TLE


## sol_1
- numba (JIT)
- floyd_warshall
- AC


# similar