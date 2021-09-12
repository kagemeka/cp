# [AtCoder ABC218 G - Game on Tree 2](https://atcoder.jp/contests/abc218/tasks/abc218_g)



# keywords
- fenwick tree
- segment tree
- binary trie
- binary search tree
- self balancing binary search tree
- multiset
- median 
- find k-th smallest element (online)
- array compression
- euler_tour



# summary
- if it's possible to calculate each median of numbers on the path from the root to a leaf fast. this problem can be solved easily by using Tree DP technique.
- in this situation, it's ok if there exists a data structure satisfying following functions.
  - add a value $x$ to multiset $S$
  - delete a value $x$ from $S$
  - calculate median of $S$ (calculate k-th smallest element of $S$)
- there are a lot of data strucutre implementing these functions.
  - fenwick tree
  - segment tree
  - multiset
    - multiset can be implemented by using self balancing binary tree
  - binary trie
  - ...
- to calculate median of from root to each node is total of $O(N\log{N})$.
- after calculating each median of leaves, calculate game result with Tree DP (dfs).


# code 
## sol_0
- numba (JIT)
- fenwick tree 
- binary search
- fenwick $\text{get}(i) = \sum_{j \le i} \text{count}(j)$



# similar 

