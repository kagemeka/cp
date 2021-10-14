# [D - Knapsack 1](https://atcoder.jp/contests/dp/tasks/dp_d)


# keywords 
- typical knapsack problem
- dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i]
  - dp[0][j] = 0