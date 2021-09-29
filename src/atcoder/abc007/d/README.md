# [AtCoder ABC007 D - 禁止された数字](https://atcoder.jp/contests/abc007/tasks/abc007_4)


# keywords
- digits DP
- remove complementary events
- inline DP

# summary
- define $f(n) :=$ count of NG numbers in range $[1..n]$ (inclusive)
- answer = $f(b) - f(a - 1)$
- in $f$, define a $dp$
  - $dp_{i, j} :=$ count of ok numbers by enumerating only digits higher than or equal to $i$ -th one. $j \in \{0, 1\}$. if $j = 1$, it's comfirmed that numbers are less than $n$, otherwise, not confirmed.
  - transition
    - $dp_{i, 1} = 8dp_{i + 1, 1} + dp_{i + 1, 0} \times (d - \begin{cases}1 & (d \gt 4) \\ 0 & \text{otherwise} \end{cases})$ ($d$ is $i$ -th digit of $n$)
    - $dp_{i, 0} = \begin{cases}1 & \text{if NG digits don't appear in higher than or equal to } i \text{ -th digit} \\ 0 & \text{otherwise} \end{cases}$
  - NG count = $\sum{dp_{0, *}}$
  - return $n - \text{NG count}$


# code 
## sol_0
- python

## sol_1, sol_2 
- numba (JIT) 


# similar 
