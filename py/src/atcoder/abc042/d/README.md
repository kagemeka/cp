# [AtCoder ABC042 D - いろはちゃんとマス目 ](https://atcoder.jp/contests/abc042/tasks/arc058_b)


# keywords 
- count up 
- grid 
- modular 
- count complementary events 
- mutually exclusive
- choose
- binomial 


# summary 
- count all mutually exclusive cases.
- all moves are as following.
  - $(1, 1) \rightarrow (H - A, B + 1) \rightarrow (H - A + 1, B + 1) \rightarrow (H, W)$
  - $(1, 1) \rightarrow (H - A, B + 2) \rightarrow (H - A + 1, B + 2) \rightarrow (H, W)$
  - ...
  - $(1, 1) \rightarrow (H - A, W) \rightarrow (H - A + 1, W) \rightarrow (H, W)$


# code 
## sol_0
- numba (JIT)


# similar 
