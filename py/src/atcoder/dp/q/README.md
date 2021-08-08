# [Q - Flowers](https://atcoder.jp/contests/dp/tasks/dp_q)


# keywords
- point update, RMQ(Range Maximum Query)
- Fenwick Tree (BIT)
- Segment Tree
- value compression (coordinate compression)


## sol_0
- BIT (Fenwick Tree)
- $(Z, max)$ is Monoid but Ring, so $Max(0, i)$ is fine but $Max(l, r)$ NG
  - $Max^{-1}(0, i)$ cannot be defined.
  - in this case, it's enough to calculate only $Max(0, i)$.
- sort indices by height, and update the results by the order of heights.
- standard/pypy


## sol_1
- Fenwick 
- abstract Fenwick Tree
- sort indices by height


## sol_2 
- Fenwick Tree 
- numba (JIT)
- sort indices by height


## sol_3
- Fenwick Tree
- numba (AOT)
- sort indices by height


## sol_4 
- Fenwick Tree 
- numba (AOT)


## sol_5
- Fenwick Tree 
- numba (AOT)
- implement fw_f