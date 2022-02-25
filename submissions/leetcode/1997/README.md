# [Weekly Contest 257](https://leetcode.com/contest/weekly-contest-257)

# [LeetCode 1997. First Day Where You Have Been in All the Rooms](https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/)


# keywords
- DP
- DFS



# summary
- $O(N)$
- let $dp_i$ = label of the first day at which you visit $room_i$
  - in this situation, this must be odd times.
- transition
  - $$dp_i = \begin{cases}
    dp_{i - 1} + 2 + (dp_{i - 1} - dp_{\text{next}_{i - 1}}) & \text{if next}_{i - 1} = i - 1 \\
    dp_{i - 1} + 2 & \text{otherwise} \\
    \end{cases}$$
- answer = $dp_{N - 1}$

# code
## sol_0
- DFS



# similar
