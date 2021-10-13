# [AtCoder ALPC J - Segment Tree](https://atcoder.jp/contests/practice2/tasks/practice2_j)



# keywords 
- segment tree
- binary search on segment tree
- max right
- set point get range query.
- update point get range minimum query.


# summary
- query 1: update point value.
- query 2: get range minimum value.
- query 3: get first index $i$ such as $ok(\prod_{j=l}^{i - 1}{A_j}) \land \neg ok(\prod_{j=l}^{i}{A_j})$
  - $ok(x) := x \lt v_q$


# code 
## sol_0
- numba (JIT)


# similar
- [AtCoder ABC014 D - 閉路](https://atcoder.jp/contests/abc014/tasks/abc014_4)