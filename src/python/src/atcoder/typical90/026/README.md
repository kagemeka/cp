# [AtCoder Typical90 026 - Independent Set on a Tree（★4）](https://atcoder.jp/contests/typical90/tasks/typical90_z)


# keywords
- tree
- bipartite graph
- graph coloring
- maximal independent set 
- tree DFS (euler tour)
- tree BFS


# summary
- consider coloring each node black or white with BFS, so that any two ajacent nodes are not colored with same color.
- at least one of count of black nodes or that of white nodes is more than or equal to $\frac{N}{2}$


# code 
## sol_0
- numba (JIT)
- tree bfs

## sol_1
- numba (JIT)
- euler tour 


# references 
- [wiki en maximal independent set](https://en.wikipedia.org/wiki/Maximal_independent_set)



# similar 
- [AtCoder EDPC P - Independent Set](https://atcoder.jp/contests/dp/tasks/dp_p)
- [AtCoder ABC036 D - 塗り絵](https://atcoder.jp/contests/abc036/tasks/abc036_d)
