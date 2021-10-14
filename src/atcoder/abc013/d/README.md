# [AtCoder ABC013 D - 阿弥陀](https://atcoder.jp/contests/abc013/tasks/abc013_4)


# keywords 
- doubling 
- graph
- cycle
- connected components 
- chost leg


# summary 
## solution 1
- at first, $\forall{i}\ $ calculate the goal after an operation. $O(N)$
- answer can be calculated with doubling.
  - $\because d = c_02^0 + c_12^1 + ... + c_k2^k (c_j \in \{0, 1\})$
- $O(N\log{N})$


## solution 2
- at first, $\forall{i}\ $ calculate the goal after an operation. $O(N)$
- $\forall{i}$
  - after $l_i$ times of operations, it's sure to come back to initial place. 
- all $l_i$ are calculated by using connected components DFS/BFS algorithm.
- $O(N)$


# code 
## sol_0
- numpy 
- solution 1


## sol_1
- numba (JIT)
- solution 1

## sol_2
- numba (JIT)
- solution 2



# similar 