# [L - Deque](https://atcoder.jp/contests/dp/tasks/dp_l)




# keywords 
- Game Theory
- Range DP
- dp[l][r] := max(
    dp[l + 1][r] + a[l],
    dp[l][r - 1] + a[r - 1],
  ) (if (n - (r - l)) & 1 == 0 [l, r))
- dp[l][r] := min(
    dp[l + 1][r] - a[l],
    dp[l][r - 1] - a[r - 1],
  ) (if (n - (r - l)) & 1 == 1 [l, r))


## sol_0, sol_1
- DFS
- TLE
- pypy


## sol_2
- DFS
- numba (JIT)

## sol_3
- DFS
- numba (AOT)
- Runtime Error?


## sol_4
- BFS
- pypy 


## sol_5
- BFS
- numba (JIT)


## sol_6
- BFS
- numba (AOT)