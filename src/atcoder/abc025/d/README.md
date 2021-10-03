# [AtCoder ABC025 D - 25個の整数](https://atcoder.jp/contests/abc025/tasks/abc025_d)


# keywords 
- bit DP
- bit count 


# summary
## solution 1
- consider fix value on board in ascending order.
- precompute given fixed values and those indices.
- let $dp_S :=$ number of patterns to place values $0, 1, ...|S| - 1$ at just $\forall{i \in S}$ indices on the board.
- $dp_S := \sum_{i \in S} dp_{S \setminus{i}} \times \begin{cases} 1 & \text{if } \text{can-transit}(S\setminus{i} \rightarrow S) \\ 0 & \text{otherwise} \\ \end{cases}$
  - for detail see editorial.
- $O(2^NN), N \le 25$ (TLE = $5$ sec, it will be AC just in time.)
- be careful of MLE too.

## solution 2 prune to compute some $S$ with bottomup
- omit calculation for impossible states.
- bottomup
- $O(2^N + 2^{N - 5}N)$
- it's needed to preprocess bit_count table
- (MLE with number any how it's implemented)


## solution 3 prune some $S$ with Recursive function.
- omit calculation for impossible states.
- compute recursively.
- $O(2^{N - 5}N)$


## editorial
- [official slideshare](https://www.slideshare.net/chokudai/abc025)


# code 
## sol_0
- numba (JIT)
- solution 1
- AC


## sol_1
- numba (JIT)
- solution 2
- MLE 


## sol_2, sol_3
- python
- solution 3
- AC



# similar 

