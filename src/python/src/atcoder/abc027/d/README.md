# [AtCoder ABC027 D - ロボット](https://atcoder.jp/contests/abc027/tasks/abc027_d)


# keywords
- greedy


# summary
- focus on a certain M position.
  - if the count of '+' appearing in righter indices than its is more than that of '-', robot should move positive direction.
  - $\because$ otherwize, it does not happen that final point becomes larger by moving to negative direction.
- but it's needed to consider that the robot must be at $0$ at last.
- thus, define point of each M is the count of '+' $-$ the count of '-' in right indices.
- and decide whether each robot should move positive or negative greedly by sorting points.


# code 
## sol_0
- python


## sol_1
- numba (JIT)


# similar
