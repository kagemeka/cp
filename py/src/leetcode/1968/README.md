# [1968. Array With Elements Not Equal to Average of Neighbors](https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/)



# [Weekly Contest 254](https://leetcode.com/contest/weekly-contest-254)



# keywords 
- greedy



# summary
- sort nums to satisfy the following condition.
  - let a := sorted array.
  - $\forall{i} \in{\{i | 1 \le i \lt n - 1\}}$, 
    $a_{i - 1}, a_{i + 1} < a_{i}$ or $a_{i - 1}, a_{i + 1} > a_{i}$
  