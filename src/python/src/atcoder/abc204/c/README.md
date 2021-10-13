# [AtCoder ABC204 C - Tour](https://atcoder.jp/contests/abc204/tasks/abc204_c)



# keywords 
- BFS, DFS ($O(V + E)$)
- brute-force
- sparse graph 


# summary
- $E \le \min(2000, V(V - 1))$ 
- BFS from each Node
- $O(V(E + V))$


# code 
## sol_0
- numba (JIT)
- BFS

## sol_1
- scipy.sparse.csgraph.breadth_first_tree


## sol_2
- scipy.sparse.csgraph.depth_first_tree


# similar