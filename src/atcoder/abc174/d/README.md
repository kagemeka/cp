# [AtCoder ABC174 D - Alter Altar](https://atcoder.jp/contests/abc174/tasks/abc174_d)


# keywords
- greedy 
- bruteforce
- consider final situation 


# summary 
## solution 1
- consider final situation
  it's must be 'RR...RRWW...WW' because of constraints
- we want move R to left and W to right as possible.
- it's enough to swap left most W and right most R greedly until there not exist $i, j, i < j, c_i = W \land c_j = R$ to satisfy above condiation.


## solution 2
- brute force final situation
- if final situation is fixed, it's easy to calculate minimum times of operations.
- at first, final situation is 'RRR...RR'
- second, it is 'WRR...RR'
- third, it is 'WWR...RR'
- ...
- last, it is 'WWW...WW'


# code
## sol_0, sol_1
- numba (JIT)
- solution 1

## sol_2
- numba (JIT)
- solution 2

# similar 
