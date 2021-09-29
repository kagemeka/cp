# [AtCoder ABC219 E - Moat](https://atcoder.jp/contests/abc219/tasks/abc219_e)


# keywords
- count up
- 2d grid -> 1d nodes
- bits brute-force
- connectivity
- connected components 
- union find
- dfs 
- exception



# summary 
- to search all moat patterns is too hard.
- instead, fix nodes and check whether there exist a moat pattern that satisfy the constraints.
- express nodes as bits (at most $2^{16}$)
- for each nodes pattern, check 
  - all target towns are contained in the nodes.
  - all the nodes are connected.
  - there not exist closed node which is not selected. (remove exception)

  


# code 
## sol_0
- numba (JIT)


# similar 