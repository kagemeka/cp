# [AtCoder Typical Algorithm F - 最小全域木問題](https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_f)




# keywords 
- MST (Minimum Spanning Tree)
- Kruskal 
- Prim
- Boruvka


# summary 



# code 
## sol_0
- scipy.sparse.csgraph.minimum_spanning_tree 
- kruskal

## sol_1
- numba (JIT)
- kruskal
- $O(E\log{V})$


## sol_2
- numba (JIT)
- prim (sparse)
- $O(E\log{V})$


## sol_3
- numba (JIT)
- prim (dense)
- $O(V^2)$
- RE


## sol_4
- numba (JIT)
- kruskal 
- $O(E\log{E} + V^2)$
- TLE



# similar 
