# [AtCoder ABC214 F - Substrings](https://atcoder.jp/contests/abc214/tasks/abc214_f)


# keywords 
- string
- dp 
- count up the number of distinct substrings.



# summary 
## $O(NM)$
- $M$ is the number of kinds of characters.
- let $dp_{i} :=$ number of distinct substings which last character is $S_i$
- if it's allowed to use $S_{i - 1}$, $dp_i = \sum_{j = \text{prev}_{S_i}}^{i - 1} dp_j$
- in this problem, it's not allowd to use $S_{i - 1}$
- thus, $dp_i = \sum_{j = \text{prev}_{S_i} - 1}^{i - 2} dp_j$
- answer $= \sum{dp}$
- time complexity is $O(NM)$.
  - for each character, total DP transition is at most $O(N)$
  - that is, for each character, 
    total time complexity to calculate each $\sum_{j = \text{prev}_{S_i} - 1}^{i - 2} dp_j$ 
    is $O(N)$
- be careful of subscript index.

## $O(N)$
- almost same as $O(NM)$ solution but storing cummulative sum.
- $\forall{i}, \sum_{j = \text{prev}_{S_i} - 1}^{i - 2} dp_j$ can be calculated with $O(1)$ by storing cummulative sum of $dp$ and $\text{prev}_{S_i}$
- let $dp_{i} :=$ number of distinct substrings which last character is any of $S_0..S_i$.
- $dp_i = dp_{i - 1} + \sum_{j = \text{prev}_{S_i} - 1}^{i - 2}{dp_j}$
  $= \sum_{j = \text{prev}_{S_i} - 1}^{i - 1}{dp_j}$
- answer $= dp_{|S|}$


# code 
## sol_0, sol_1
- numba (JIT)
- $O(N)$


## sol_2
- numba (JIT)
- $O(NM)$ where $M$ is the number of kinds of characters.



# similar 
- [AtCoder ABC216 F - Max Sum Counting](https://atcoder.jp/contests/abc216/tasks/abc216_f)