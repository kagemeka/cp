# [N - Slimes](https://atcoder.jp/contests/dp/tasks/dp_n)



# keywords
- Range DP
  - fix values from small to large range.
- cumsum
- brute force
- divide and conquer
- dp[l][r] = min(dp[l, m] + dp[m, r]) + s[r] - s[l] (for m in [l + 1, r))
  - dp[l][r] = 0 (when r - l == 1)
  - dp[l][r] := undefined or inf (when r <= l)
  - where s is 1 indexed cumulative summation.


## sol_0
- DFS 
- TLE
- pypy


## sol_1
- DFS
- numba (JIT)


## sol_2
- DFS
- numba (AOT)
- runtime error



## sol_3
- BFS


## sol_4
- BFS
- numba (JIT)


## sol_5
- BFS 
- numba (AOT)


## sol_6
- numpy
- dp_left[left_index, width]
- dp_right[right_index, width]
