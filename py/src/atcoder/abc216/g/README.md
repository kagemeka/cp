# [G - 01Sequence](https://atcoder.jp/contests/abc216/tasks/abc216_g)



# keywords 
- ushi game 
- shortest path probelm (duality)
- Dijkstra method 



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


## 2: Fenwick Tree  



# Code
## sol_0
- python
- TLE 


## sol_1
- pypy


## sol_2 



# About Ushi Game
- there are given some condition $dist_j - dist_i \le c_k$
- calculate the `maximum` value of $dist_{T, S}$, where, $S, T$ denote certain src and target node.
- this problem can be solved as Shortest Path problem (Dijkstra method).