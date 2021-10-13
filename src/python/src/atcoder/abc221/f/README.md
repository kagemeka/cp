# [AtCoder ABC221 F - Diameter set](https://atcoder.jp/contests/abc221/tasks/abc221_f)


# keywords 
- tree
- diamiter
- consider different cases.
- euler tour
- tree BFS
- modular 


# summary
## solution 1 Naive
- consider finding the core of given tree and count up nodes such that distance from the core equals the tree radius.
- it's needed to consider either of two cases.
  - tree diamiter is an odd value.
    - there is two tree cores.
    - for each subtree, count up nodes such that depth is $\text{radius} = \lfloor\frac{\text{diameter}}{2}\rfloor$ 
  - tree diamiter is an even value.


## solution 2 ingenious preprocessing
- In solution 1, it's needed to consider different cases.
- now, at first we add a mid node against each original edge.
- by doing so, diameter must be an even value.
- therefore, it's enough to consider only one case.



# code 
## sol_0
- numba (JIT)
- solution 2


# similar 
