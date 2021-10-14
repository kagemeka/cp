# [E - Knapsack 2](https://atcoder.jp/contests/dp/tasks/dp_e)


# keywords
- dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - v[i]] + w[i]
  - dp[0][j] = inf, dp[0][0] = 0