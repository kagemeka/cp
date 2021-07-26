# [Disjoint Set Union](https://atcoder.jp/contests/practice2/tasks/practice2_a)


# implementation


## sol_0
- create Node class out of UnionFind and use it.


## sol_1
- UF holds parent, size, rank as its properties.



## sol_2
- manage parent and size with only one array.
- root node has the size info and the others have their parent node id.
- be careful of that the size of each set is negative value.