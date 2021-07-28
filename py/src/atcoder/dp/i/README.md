# [I - Coins](https://atcoder.jp/contests/dp/tasks/dp_i)



# keywords
- probability
- dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] * p[i]
- ans = sum(dp[n][j]) (for j | j > n - j <-> 2 * j > n)



## sol_0
dp[i][j] := more the or equal to j coins face up out of first i coins.


## sol_1
dp[i][j] := just j coins face up ouf of first i coins.