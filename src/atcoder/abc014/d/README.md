# [AtCoder ABC014 D - 閉路](https://atcoder.jp/contests/abc014/tasks/abc014_4)


# keywords
- LCA (Lowest Common Ancestor)


# summary
- for each query,
  - print $\text{LCA}(u, v) + 1$


# code 
## sol_0, sol_1
- python
- doubling 


## sol_2
- numba (JIT)
- doubling


## sol_3
- numba (JIT)
- euler-tour + Range Minimum Query with segment tree.
- binary search

## sol_4
- numba (JIT)
- euler-tour + Range Minimum Query with sparse table.


## sol_5
- numba (JIT)
- euler-tour + Range Minimum Query with segment tree.
- naively define monoid $S := (depth, node)$ 


## sol_6
- numba (JIT)
- euler-tour + union-find (tarjan's offline algorithm)


# similar
- [AtCoder ALPC J - Segment Tree](https://atcoder.jp/contests/practice2/tasks/practice2_j)