# [Weekly Contest 256](https://leetcode.com/contest/weekly-contest-256)

# [LeetCode 1987. Number of Unique Good Subsequences](https://leetcode.com/problems/number-of-unique-good-subsequences/)



# keywords
- dp
- inline DP
- count up
- greedy



# summary
- $O(N)$
- $dp_{i, d} :=$ counts when end with $d$
  - where it's checkd until $i$
- $$dp_{i, d} =
  \begin{dcases}
  dp_{i - 1, d} + dp_{i - 1, d\oplus 1} & \text{if } b_i = d\\
  dp_{i - 1, d} & \text{otherwise}
  \end{dcases}\\
  dp_{i, d} = dp_{i, d} + 1 \text{ if } d = 1
  $$
- it's ok to transit with inline DP technique.
