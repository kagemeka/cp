# [AtCoder ABC185 E - Sequence Matching](https://atcoder.jp/contests/abc185/tasks/abc185_e)




# keywords 
- LCS (Longest Common Subsequence)
- DP 


# summary
- let $dp_{i, j} =$ minimum cost for $A_1...A_i$ and $B_1...B_j$
- answer = $dp_{N, M}$
- $dp_{i, j} = \min{(dp_{i - 1, j} + 1, dp{i, j - 1} + 1, dp_{i, j} + (A_{i - 1} \ne B_{j - 1}))}$


# editorial
- [youtube](https://www.youtube.com/watch?v=xPum1B6dmfk)


# code 
## sol_0
- numba (JIT)


# similar 
- [AtCoder EDPC F - LCS](https://atcoder.jp/contests/dp/tasks/dp_f)
