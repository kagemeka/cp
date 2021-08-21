# [E - Chain Contestant](https://atcoder.jp/contests/abc215/tasks/abc215_e)




# keywords 
- bit DP 
- similar to Traveling Salesperson problem.


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


# similar 
- [ABC180 E - Traveling Salesman among Aerial Cities](https://atcoder.jp/contests/abc180/tasks/abc180_e)