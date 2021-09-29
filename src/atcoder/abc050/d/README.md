# [AtCoder ABC050 D - Xor Sum](https://atcoder.jp/contests/abc050/tasks/arc066_b)


# keywords 
- digits DP
- DP states compression 
- xor 
- $a + b = (a \And b) \ll 1 + a \oplus b$

# summary 
- consider constraints
- $\exists{a, b}\ 0 \ge a, b, 0 \le v = a + b \le N, 0 \le u = a \oplus b \le N$
  - $v, u \ge 0 \because a, b \ge 0$
  - $v = a + b = (a \And b) \ll 1 + a \oplus b = (a \And b) \ll 1 + u \ge u \ge 0$
  - therefore, it's enough to count the number of $\exists{a, b}\ a, b \ge 0, v = a + b \le N$

- define $dp_{i, j} :=$ count such that $(N \gg 1) - (v \gg 1) = j$ by fixing only higher or equal to $i$ -th bit of $a, b$
  - $dp_{*, j \lt 0}$ are invalid (do not satisfy the constraint $v = a + b \le N$)
- this dp as it is $O(N\log{N})$.
- consider compress DP states.
  - when $j \ge 2$, $dp_{i, j}$ would not contributes to $dp_{i\prime \lt i, j\prime \lt 2}$ even how we decide $i\prime$ -th bits of $a, b$.
- therefore, it's ok to compress states $dp_{i, j \ge 2}$ as $dp_{i, 2}$
- initialize $dp_{60, 0} = 1$
- transition 
  - case $N \gg i \And 1 = 1$
    - $dp_{i, 0} = dp_{i + 1, 0}$ ($(a, b) = (1, 0)$, be careful of $a \ge b$ to remove duplicates)
    - $dp_{i, 1} = dp_{i + 1, 0} + dp_{i + 1, 1}$ ($(a, b) = (0, 0), (1, 1)$)
    - $dp_{i, 2} = 3dp_{i + 1, 2} + 2dp_{i + 1, 1}$ ($(a, b) = [(0, 0), (1, 0), (1, 1)], [(0, 0), (1, 0)]$)
  - otherwise 
    - $dp_{i, 0} = dp_{i + 1, 0} + dp_{i + 1, 1}$ ($(a, b) = (0, 0), (1, 1)$)
    - $dp_{i, 1} = dp_{i + 1, 1}$ ($(a, b) = (1, 0)$)
    - $dp_{i, 2} = 3dp_{i + 1, 2} + dp_{i + 1, 1}$ ($(a, b) = [(0, 0), (1, 0), (1, 1)], [(0, 0)]$)


# code 
## sol_0
- numba (JIT)


# similar 

