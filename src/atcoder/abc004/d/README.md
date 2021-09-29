# [AtCoder ABC004 D - マーブル](https://atcoder.jp/contests/abc004/tasks/abc004_4)


# keywords 
- DP
- state compression



# summary
- $dp_{i, j} :=$ minimum procedures to put total of $j$ count of marbles in range $(-500, i]$
- initialize
  - $dp_{*, *} := \inf$
  - $dp_{-500, 0} = 0$
- transition
  - $dp_{i, j} := \min{(dp_{i - 1, j}, dp_{i - 1, j - 1} + |i - x_{j}|)}$
  - where $x_j = \begin{cases} -100 & (j \le R) \\ 0 & (j \le R + G) \\ 100 & \text{otherwise} \end{cases}$
- answer = $dp_{500, R + G + B}$
  

# code 
## sol_0, sol_2
- numpy

## sol_1
- python


# similar
