# [Biweekly Contest 59](https://leetcode.com/contest/biweekly-contest-59)


# [1975. Maximum Matrix Sum](https://leetcode.com/problems/maximum-matrix-sum/)




# keywords
- math
- theoretical value


# summary
- oddness of the sum of counts of negative values and positive values is always keeped.
- any two cell signs can be reversed without changing other cell signs.
- if the number of negative values is odd at beginning,
  - ans := $\sum_{i, j} |cell_{i, j}| - 2\times\min_{i, j}{|cell_{i, j}|}$
- else
  - ans := $\sum_{i, j} |cell_{i, j}|$ simply.
