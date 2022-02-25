# [C. Mocha and Hiking](https://codeforces.com/contest/1559/problem/C)



# keywords
- Greedy



# summary
- consider three cases
  - first case: $a_1 = 1$
    - in this case, one of the answers is $n + 1, 1, 2, ... n$.
  - second case: $a_n = 0$
    - in this case, one of the answers is $1, 2, 3, ... n, n + 1$.
  - third case: $a_{i} = 0$ and $a_{i + 1} = 1$ for any $1 \le i \lt n$
    - in this case, one of the answers is $1, ... i, n + 1, i + 1, ... n$
