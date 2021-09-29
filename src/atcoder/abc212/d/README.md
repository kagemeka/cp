# [D - Querying Multiset](https://atcoder.jp/contests/abc212/tasks/abc212_d)


# keywords 
- priority queue 
- binary heap
- multiset
- online update
- lazy update
- store `s` the infomation of the sum of incremented number outside of the bag ever. (op = 2)
- when pushing a value `x` into the bag, instead push `x - s`. (op = 1)
- after pop a value x from the bag, print `x + s`. (op = 3)


## sol_0
- use heapq 