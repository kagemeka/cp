# [AtCoder ABC047 D - 高橋君と見えざる手](https://atcoder.jp/contests/abc047/tasks/arc063_b)


# keywords
- DP
- cummin 
- greedy 
- math 


# summary
- each the number of towns where takahashi will buy apples and that where he sell apples is at most one.
- if Takahashi buy apples at town $i$, he should sell all of them at town $j$ such that $A_j = \max_{k=i}^{N}A_k$
  - $\leftrightarrow$ if Takahashi sell apples at town $j$, he should by all of them at town $i$ such that $A_i = \min_{k=0}^{j}A_k$
  - in other words, if we fix $j$, $i$ can be found with $O(1)$ with preprocess cumulative minimum.
- let $d_{max} = \max_{i}{A_j - A_i}$
- $$\text{answer} = 
  \sum_{i}{\begin{cases}
  1 & (A_j - A_i = d_{max}) \\
  0 & \text{otherwise}
  \end{cases}}$$
- it's will not happen that there occurs a new pair $j \lt j\prime$ such that $A_j\prime - A_j \ge d_{max}$ $\because A_i$ are pairwise distinct, if $A_j\prime - A_j \ge d_{max}$, $A_j\prime - A_i \gt d_{max}$. this is conflict to $d_{max} = A_j - A_i$


# code 
## sol_0
- numpy 


# similar