# [AtCoder Typical90 008 - AtCounter（★4）](https://atcoder.jp/contests/typical90/tasks/typical90_h)


# keywords 
- string 
- DP
- count up
- modular 



# summary
- $dp_{i, j} :=$ count such that last letter is $j$ by using only any of $\{S_1, S_2, ..., S_{i}\}$
- initialize $dp_{*, *} = 0, dp_{0, '\$'} = 1$
- transition
  - $dp_{i, *} = dp_{i - 1, *}
  - $dp_{i, 'a'} = dp_{i, 'a'} + dp_{i - 1, '\$'}$ (if $S_i$ = 'a')
  - $dp_{i, 't'} = dp_{i, 't'} + dp_{i - 1, 'a'}$ (if $S_i$ = 't')
  - $dp_{i, 'c'} = dp_{i, 'c'} + dp_{i - 1, 't'}$ (if $S_i$ = 'c')
  - ...
  - $dp_{i, 'r'} = dp_{i, 'r'} + dp_{i - 1, 'e'}$ (if $S_i$ = 'r')



# code 
## sol_0
- python
- default dict 


# similar 
- [AtCoder ABC211 C - chokudai](https://atcoder.jp/contests/abc211/tasks/abc211_c)