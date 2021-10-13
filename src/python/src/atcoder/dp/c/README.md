# [C - Vacation](https://atcoder.jp/contests/dp/tasks/dp_c)


# keywords
- dp[i][j] = max(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) + a[i][j]


