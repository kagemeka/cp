# [AtCoder ABC174 C - Repsept](https://atcoder.jp/contests/abc174/tasks/abc174_c)


# keywords
- repunit number 
  - $R_n = \displaystyle{\frac{10^n - 1}{9}}$ 
- pigeonhole principle
- greedy


# summary
- $n \mod{K}$ is $O(K)$
- $A_{i + 1} = A_i \times 10 + 7$
- if there exist $i$ such that $A_i \equiv 0 \mod{K}$
  - least $i$ is $1 \le i \le K$.
- otherwise, $A_i \mod{K}$ should get into loop.
- this problem can be solved with $O(K)$


# code 
## sol_0
- numba (JIT)



# references
- [wiki en Repunit](en.wikipedia.org/wiki/Repunit)
- [wiki ja Repunit](https://ja.wikipedia.org/wiki/レピュニット)
- [wiki en Pigeonhole Principle](https://en.wikipedia.org/wiki/Pigeonhole_principle)
- [wiki ja Pigeonhole Principle](https://ja.wikipedia.org/wiki/%E9%B3%A9%E3%81%AE%E5%B7%A3%E5%8E%9F%E7%90%86)