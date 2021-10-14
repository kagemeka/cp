# [D - Sum of Maximum Weights](https://atcoder.jp/contests/abc214/tasks/abc214_d)



# keywords 
- Union Find(Disjoint Set)
- Graph 
- Tree 
- Forest
- count up


# Summary
- let c_i := the number of paths in which the greatest weight is the weight of $edge_i$
- $\sum_{i = 1}^{n - 1}\sum_{j = i + 1}^{n} f(i, j)$
  $= \sum_{i = 1}^{n - 1}{w_i \times c_i}$

- at first, I consider this might be calculated with Tree DP anyway. but it was so hard.
- next, looked at the heaviest edge in the current graph,
  - let this edge as $edge_i$
  - if the number of vertices on the side of $u_i$ and that on the side of $v_i$ are known,
    let each of them $cu_i$, and $cv_i$, and then $c_i$ is calculated as follow 
  - $c_i = cu_i \times cv_i$
- thus, by adding edges in order of their weights with UnionFind, the answer can be calculated easily. 
- it's ok that there exist multiple edges with the same weights.


## sol_0
- union by size 



## sol_1
- union by rank 


## sol_2
- parent and size at same
- numba (JIT)


## sol_3
- parent and size at same 
- numba (AOT)




# similar