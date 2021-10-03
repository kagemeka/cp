# [AtCoder ABC017 D - サプリメント](https://atcoder.jp/contests/abc017/tasks/abc017_4)


# keywords 
- DP
- shakutori method
- count up
- modular


# summary 
- let $dp_i :=$ patterns to eat candy $1..i$
- answer $= dp_N$
- initialize
  - $dp_0 := 1$
- transition
  - consider that from which to which he can eat the previous day.
  - $dp_i := \sum_{j=\text{prev}_{f_i}}^{i - 1}{dp_j}$



# code 
## sol_0
- python 


## sol_1
- numba (JIT)


# similar 
- [AtCoder ABC214 F - Substrings](https://atcoder.jp/contests/abc214/tasks/abc214_f)