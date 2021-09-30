# [AtCoder ABC010  D - 浮気予防](https://atcoder.jp/contests/abc010/tasks/abc010_4)


# keywords 
- minimum cut
- maximum flow 
- dinic
- ford-fulkerson
- edmonds-karp
- max-flow min-cut theorem

# summary
- add virtual sink $n$ to graph
- for each target girls $p_i$, add edge $(p_i, n)$
- calculate max-flow $(0, n)$


# code 
## sol_0
- scipy

## sol_1
- networkx

## sol_2
- python
- dinic 


## sol_3
- numba (JIT)
- dinic

## sol_4
- numba (JIT)
- ford fulkerson


## sol_5
- numba (JIT)
- edmonds-karp


# similar 