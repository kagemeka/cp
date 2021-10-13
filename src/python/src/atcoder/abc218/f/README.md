# [AtCoder ABC218 F - Blocked Roads](https://atcoder.jp/contests/abc218/tasks/abc218_f)



# keywords
- shrotest path
- Dijkstra
- BFS


# summary 
- Do dijkstra or bfs to calculate dist and predecessors against original graph.
- $\forall{\text{edge}}$ 
  - if the edge was not used in shortest path, answer will not changed.
  - otherwize, remove the edge, then compute shortest dist. 
- total complexity is $O(N(N + M))$, because the number of edges used in shortest path is at most $O(N)$, and $O(N + M)$ per BFS


# code 
## sol_0
- numba (JIT)
- BFS


## sol_1
- numba (JIT)
- Dijkstra


