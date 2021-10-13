# [AtCoder ABC153 F - Silver Fox vs Monster](https://atcoder.jp/contests/abc153/tasks/abc153_f)



# keywords 
- Greedy 
- sort by coordinates
- Range Set Point Get Query (Range Add Point Get)
- imos method 
- fenwick tree
- segment tree 
- cumsum 
- shakutori method 
- binary search 


# summary 
- sort X, H by X
- from left to right, bomb [l, r)if the $\text{monster}_l\text{'s HP} \gt 0$ greedly.
- r can be updated in $O(N)$ by using shakutori method 
- bomb [l, r) can be calculated lazily by using imos method, segment tree, or fenwick tree.


# code 
## sol_0
- numba (JIT)
- imos method 
- shakutori method 
- cumsum 
- $O(N)$

## sol_1
- numba (JIT)
- fenwick tree
- shakutori method 
- cumsum 
- $O(N\log{N})$



# similar 