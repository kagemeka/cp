# [AtCoder Typical90 028 - Cluttered Paper（★4）](https://atcoder.jp/contests/typical90/tasks/typical90_ab)


# keywords 
- 2D cumulative sum
- 2D fast zeta transform
  - 2D imos method
- inclusive exclusive theory


# summary
- add $1$ to (left, down)
- add $-1$ to (left, right + 1)
- add $-1$ to (down, up + 1)
- add $1$ to (right + 1, up + 1)
- be careful of that query are simiopen interval $[l, r), [d, u)$

# code 
## sol_0
- numpy 


# similar 
- [AtCoder ABC014 C - AtColor](https://atcoder.jp/contests/abc014/tasks/abc014_3)
