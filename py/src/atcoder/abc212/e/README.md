# [E - Safety Journey](https://atcoder.jp/contests/abc212/tasks/abc212_e)


# think during contest 
- at first, it looks like to use fast matrix power.
- but N is 5000. this solution is NG.
- $$ O(N^3\log{k}) $$
- notice M is small. this constraint should be used anyhow but i don't know.


# keywords 
- DP 
- $dp[i][j]$ = the number of i days trip from city 0 to city j (city is 0-indexed)
- let $s_j = \{j' | connected\ to\ j\}$
- $dp[i][j] = \sum_{j}{dp[i - 1][j]} - dp[i - 1][j] - \sum_{j'\in{s_j}}{dp[i - 1][j']}$
- $\sum_{j}{dp[i - 1][j]}$ is enough to be calculated only once per $i$.
- total number of j' is $2M$ per $i$
- so time comprexity is $O(M + N)$ per $i$ 
- complety of $i$ is $O(K)$
- so entirely, the problem can solved with $O((M + N)K)$


# tips 
- counting on graph -> DP
- Dijkstra is DP 
- Bellman Ford is DP 
- Floyd Warshall is DP
- subtract small pattern from all pattern.



## sol_0
- pypy 
- graph


## sol_1
- edge
- numba (JIT)


## sol_2
- edge 
- numba (AOT)


## sol_3
- pypy
- edge 