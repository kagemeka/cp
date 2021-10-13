# [AtCoder Typical90 019 - Pick Two（★6）](https://atcoder.jp/contests/typical90/tasks/typical90_s)


# keywords 
- $O(N^2), O(N^3) \rightarrow$ range DP ? 
- minimum value


# summary
- let $dp_{l, r} :=$ answer when $A \leftarrow A[l, r]$
- closed range [l, r]
- initialize
  - $dp_{*, *} = \inf$
  - $dp_{i, i + 1} = |A_i - A_{i + 1}|$
- transition
  - fix $d := r - l$
  - $\forall{d, 2 \le d \le n - 1}$
    - $\forall{l, r}$
      - $dp_{l, r} = dp_{l + 1, r - 1} + |A_l - A_r|$
      - $\forall{m, l + 1 \le m \le r - 2}$
        - $dp_{l, r} = \min{(dp_{l, r}, dp_{l, m} + dp_{m + 1, r})}$
- answer = $dp_{1, n}$


# code 
## sol_0
- numba (JIT)


# similar 
- [AtCoder EDPC L - Deque](https://atcoder.jp/contests/dp/tasks/dp_l)
- [AtCoder EDPC N - Slimes](https://atcoder.jp/contests/dp/tasks/dp_n)
- [AtCoder ABC217 F - Make Pair](https://atcoder.jp/contests/abc217/tasks/abc217_f)