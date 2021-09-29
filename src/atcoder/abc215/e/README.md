# [E - Chain Contestant](https://atcoder.jp/contests/abc215/tasks/abc215_e)




# keywords 
- bit DP 
- similar to Traveling Salesperson problem.
- permutations DP -> bits + last component DP


# summary
- $dp_{i, u, j} :=$ patterns by finishing to check i-th character in $S$
  - $u :=$ Set of used character.
  - $j :=$ the character used at last.
- transition
  - initially, $dp_{i, u, j} := 0\ (\forall{i, u, j})$
  - let $x := s_{i}$
  - $dp_{i, u, j} = dp_{i, u, j} + dp_{i - 1, u, j}\ (\forall{u, j})$ (x is not used.)
  - $dp_{i, u, x} = dp_{i, u, x} + dp_{i - 1, u, x}$ (x is used, previous one is x.)
  - $dp_{i, u, x} = dp_{i, u, x} + \sum_{k \in u, k \neq x}{dp_{i - 1, u - \{x\}, k}}$ ( x is used. previous one is not x)
  - $dp_{i, 1 << x, x} = dp_{i, \{x\}, x} + 1$ (x is used at first.)



## sol_0
- pypy
- naive


## sol_1
- python
- effective Space Complexity


## sol_2
- numba (JIT)
- effective space complexity


## sol_3
- numba (AOT)
- effective space complexity



# similar 
- [ABC180 E - Traveling Salesman among Aerial Cities](https://atcoder.jp/contests/abc180/tasks/abc180_e)
- [LeetCode 1986. Minimum Number of Work Sessions to Finish the Tasks](https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/)