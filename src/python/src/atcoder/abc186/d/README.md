# [AtCoder ABC186 D - Sum of difference](https://atcoder.jp/contests/abc186/tasks/abc186_d)


# keywords 
- math 
- sort 
- cumsum



# summary 
- sort $A$
- let $s := \text{cumsum}(A)$
- answer = $\sum_{i=2}^{N} (i - 1)A_i - S_{i - 1}$