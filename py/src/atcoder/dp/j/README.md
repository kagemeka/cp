# [J - Sushi](https://atcoder.jp/contests/dp/tasks/dp_j)


# keywords 
- dp[i][j][k]
  - i is the count of dishes 3 sushi on it.
  - j is the count of dishes 2 sushi on it.
  - k is the count of dishes 1 sushi on it.
  - the expected value to make i = j = k = 0 from here.

  - dp[i][j][k] = 
      dp[i][j][k] * (n - i - j - k) / n
      + i / n * dp[i - 1][j + 1][k] (if i > 0)
      + j / n * dp[i][j - 1][k + 1] (if j > 0)
      + k / n * dp[i][j][k - 1] (if k > 0)
  - dp[i][j][k] = 
      n / (i + j + k)
      + i / (i + j + k) * dp[i - 1][j + 1][k] (if i > 0)
      + j / (i + j + k) * dp[i][j - 1][k + 1] (if j > 0)
      + k / (i + j + k) * dp[i][j][k - 1] (if k > 0)

- compress state 
- state loop


## sol_0
- DFS
- TLE if use lru_cache 
  - instead, prepare 3D cache table.


## sol_1
- DFS
- numba (JIT)


## sol_2
- DFS 
- numba (AOT)


## sol_3
- BFS
- pypy


## sol_4
- BFS
- numba (AOT)