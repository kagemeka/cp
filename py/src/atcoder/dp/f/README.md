# [F - LCS](https://atcoder.jp/contests/dp/tasks/dp_f)


# keywords
- Longest Common SubSequence
- dp[i][j] = max(
    dp[i - 1][j],
    dp[i][j - 1],
    dp[i - 1][j - 1] (if dp[i][j] = dp[i - 1][j - 1]),
  )
- retrieve DP transition
  - memorize previous state (TLE in this case.)
  - In this problem, it can be retrieved after dp transition finised.



## sol_0
- pypy

## sol_1
- pypy
- class

## sol_2
- numpy
- class

## sol_3
- numba