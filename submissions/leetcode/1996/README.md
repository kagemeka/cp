# [Weekly Contest 257](https://leetcode.com/contest/weekly-contest-257)

# [LeetCode 1996. The Number of Weak Characters in the Game](https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/)


# keywords
- DP
- sort
- binary search
- greedy
- cummulatie maximum


# summary
## solution 1
- let $a$ = attack, $d$ = defence
- sort $a, d$ by $a$ in descending order at first and $d$ in ascending order at second.
- in this situation,
  - $a$ is monotonous increase.
  - if $a_i = a_j$, $d_i, d_j$ is monotounus increase for $i, j$.
- $\forall{i}, $ let $j$ is the minimum index such that $a_j > a_i$.
- answer $= \sum_i{d_i \lt \max_{k \ge j}d_k}$ ($d_{N + 1} := 0$)

## solution 2
- let $a$ = attack, $d$ = defence
- sort $a, d$ by $a$ in ascending order at first and $d$ in ascending order at second.
- in this situation,
  - $a$ is monotonous decrease.
  - if $a_i = a_j$, $d_i, d_j$ is monotounus increase for $i, j$.
- answer $= \sum_i{d_i \lt \max_{j \lt i}d_j}$ ($d_0 := 0$)


# code
## sol_0
- solution 1


# similar
