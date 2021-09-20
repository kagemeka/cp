# [AtCode Typical90 021 - Come Back in One Piece（★5）](https://atcoder.jp/contests/typical90/tasks/typical90_u)


# keywords
- strongly connected components
- DAG
- DFS (reverse DFS)


# summary
- compute Strongly Connected Components
- answer = $\sum_{\text{scc}}{|scc|\choose{2}}$


# code 
## sol_0
- scipy.sparse.csgraph.connected_components


## sol_1
- numba (JIT)
- non-recursive


# similar 
- [AtCoder Practice2 G - SCC](https://atcoder.jp/contests/practice2/tasks/practice2_g)
