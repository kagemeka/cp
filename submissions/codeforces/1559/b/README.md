# [B. Mocha and Red and Blue](https://codeforces.com/contest/1559/problem/B)




# keyword
- DP
- retrieve DP transition



# summary
- $dp_{i, j} :=$ minimum imperfectnelss by i in case that square i is painted color j
  - where j = 0 if the color is blue and j = 1 if the color is red.
- initially, $dp_{i, j} = \inf, dp_{0, j} = 0$
- $dp_{i, j} = min(dp_{i - 1, j} + 1, dp_{i - 1, j \oplus 1})$. if $s_i \neq j$
