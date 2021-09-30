# 


# keywords 
- Shortest Dist 
- Floyd Warshall 



# summary
- calc shortest dist for all to all with Floyd Warshall
- answer = $\min_i{\max_j{dist_{i, j}}}$



# code 
## sol_0
- python



## sol_1, sol_2
- scipy.sparse.csgraph.floyd_warshall


## sol_3
- scipy.sparse.csgraph.shortest_path


## sol_4
- python
- TLE 


## sol_5
- pypy


## sol_6
- numba (JIT)
- sparse graph


## sol_7, sol_8, sol_9, sol_10
- numba (JIT)
- dense graph


# similar 