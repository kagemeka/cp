# [G - 01Sequence](https://atcoder.jp/contests/abc216/tasks/abc216_g)



# keywords 
- ushi game 
- shortest path probelm (duality)
- Dijkstra method 
- Fenwick Tree (Binary Indexed Tree)
- stack


# summary
## 1: this is Ushi-Game
- consider least conditions
  - let $B$ is a sequence
  - $B_i$ denotes the count of 0 in in $A_0 .. A_i$
  - conditions
    - $B_{R_k} - B_{L_k - 1} \le R_k - L_k + 1 - X_k$
    - $B_{i + 1} - B_{i} \le 1$
    - $B_{i + 1} \ge B_i \leftrightarrow B_i - B_{i + 1} \le 0$
  - sort edges are like below
    - cost $R_k - L_k + 1 - X_k$, $B_{L_k - 1} \rightarrow B_{R_k}$
    - cost 1, $B_i \rightarrow B_{i + 1}$
    - cost 0, $B_{i + 1} \rightarrow B_i$


## 2: Fenwick Tree + stack 
- sort $L, R, X$ by R in ascending order
- initialize $i = 0$ and prepare empty stack $st$
- loop for $l, r, x$
  - while $i \lt r, st.append(i), i = i + 1$
  - get $c = \sum_{j=l}^{r} A_j (O(\log{N}) \text{ with fenwick tree})$ 
  - while $c \lt x, k = st.pop(), fenwick.update(k + 1, 1), A_k = 1, c = c + 1$



# Code
## sol_0
- python
- TLE 


## sol_1
- pypy


## sol_2, sol_3
- numba (JIT)


## sol_4
- numba (JIT)
- self implemented Binary Heap 


## sol_5
- python
- fenwick tree 


## sol_6, sol_7, sol_8
- numba (JIT)
- fenwick tree 





# About Ushi Game
- there are given some condition $dist_j - dist_i \le c_k$
- calculate the `maximum` value of $dist_{T, S}$, where, $S, T$ denote certain src and target node.
- this problem can be solved as Shortest Path problem (Dijkstra method).