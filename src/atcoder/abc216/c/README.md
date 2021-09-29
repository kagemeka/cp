# [C - Many Balls](https://atcoder.jp/contests/abc216/tasks/abc216_c)


# keywords 
- bits
- greedy


# summary
- while $N > 0$
  - if $N \land 1 = 1$, $N = N - 1$, append 'A' to result.
  - else $N = \frac{N}{2}$, append 'B' to result.
- reverse result      
  