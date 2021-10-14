# [AtCoder ABC206 D - KAIBUNsyo](https://atcoder.jp/contests/abc206/tasks/abc206_d)




# keywords 
- connected components
- UnionFind (DisjointSet)
- labeling with DFS or BFS


# summary 
- connect $A_i, A_{N + 1 - i}$
  - UnionFind
    - unite online
  - DFS
    - add edge $A_i \leftrightarrow A_{N + 1 - i}$
    - calc labels at last 
  - BFS
    - add edge $A_i \leftrightarrow A_{N + 1 - i}$
    - calc labels at last 
- answer = (kind of values) - (number of connected components)
- if $A_i$ are large or if use DFS or BFS, do compress array at first. 



# code 
## sol_0
- numba (JIT)
- union find 


## sol_1



# similar 
