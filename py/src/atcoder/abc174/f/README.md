# [AtCoder ABC174 F - Range Set Query](https://atcoder.jp/contests/abc174/tasks/abc174_f)


# keywords 
- fenwick tree
- segment tree
- range -> 2d plotting (left -> x-axis, right -> y-axis)
- scanning algorithm 
- count up
- complement (set theory)



# summary
- for each query, 
  - count up the number of duplicates in range $[l, r]$.
  - answer = $r - l + 1 - \text{number of duplicates}$
- for each $i$, compute previous occurence j of $c_i$
  - if not exist, $j = -1$
- number of duplicates in range $[l, r]$ is $\sum{l \le j \land i \le r}$
- sort $c$ by $j$ in descending
- sort query by $l$ in descending
- prepare fenwick tree.
- for each query,
  - $\forall{j \ge l}, \text{increment } i \text{ on fenwick tree}$
  - answer = $\text{fenwick get}(r)$
- using segment tree is also fine.


# editorial
- [youtube](https://www.youtube.com/watch?v=h0MGG8rxrYc)


# code 
## sol_0
- numba (JIT)
- fenwick tree
