# [1970. Last Day Where You Can Still Cross](https://leetcode.com/problems/last-day-where-you-can-still-cross/)




# [Weekly Contest 254](https://leetcode.com/contest/weekly-contest-254)


# keywords
- Union Find(Disjoint Set)
- reverse order
- dummy node (0, n + 1)


# summary
- at first, all cells are filled with water.
- let node[y, x]'s index := y * cols + x + 1 (y, x are 0-indexed)
- prepare dummy nodes 0 and n + 1
- if drying node[y, x], look at surrounding nodes, if each of them is already dryed,
  connect current node[y, x] and it.
- after finishing to dry node[y, x], if index 0 and n + 1 are in the same group, terminate searching.





# similar
