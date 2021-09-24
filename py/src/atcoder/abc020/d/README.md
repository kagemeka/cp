# [AtCoder ABC020 D - LCM Rush](https://atcoder.jp/contests/abc020/tasks/abc020_d)


# keywords 
- count up 
- modular 
- LCM 
- GCD
- consider per GCD
- divisors
- prime factors
- highly composite number
- fast mobius transform


# summary 
## solution 1 inclusive exclusive theory
$$
\text{answer} = \sum_{i=1}^{N}{\text{lcm}(i, K)} \\
= \sum_{i=1}^{N}\displaystyle{\frac{iK}{\gcd{(i, K)}}} \\
= \sum_{g \in \{\forall{i}\ \gcd{(i, K)}\}}\sum_{i, \gcd{(i, K)} = g}\displaystyle{\frac{iK}{\gcd{(i, K)}}} \\
= \sum_{g \in \{\forall{i}\ \gcd{(i, K)}\}}\displaystyle{\frac{K}{g}}\sum_{1 \le i \le N, \gcd{(i, K)} = g}i \\
$$
- define $d(n) =$ number of divisors of $n$
- $d(K)$ is not too large. $\max{d(K)} = 1334$ when $K = 735134400$ $(K \le 10 ^ 9)$
- define $f(g) = \sum_{1 \le i \le N, \gcd{(i, K)} = g}i$
- define $s(g) = \sum_{1 \le i \le N, g|i}i$
- then, $f(g) = s(g) - \sum_{g|d, g \lt d \le K}{f(d)}$ ($O(d(K))$)
- so this problem can be solved with $O(\sqrt{K} + d(K)\log{d(K)} + d(K)^2)$

## solution 2 fast mobius transformation
- calculate $f(g)$ faster than solution 1 with mobius transformation
- $K = p_0^{e_0}p_1^{e_1}..p_k^{e_k}$
- $\forall{p \in \{p_0, p_1, ... p_k\}}$
  - $\forall{d|K}$
    - if $p\not|d$ 
      - do nothinng
    - otherwise
      - $s(\frac{d}{p}) \leftarrow s(\frac{d}{p}) - s(d)$
- $O(\sqrt{K} + d(K)\log{d(K)} + d(K)\log{K})$ = $O(\sqrt{K} + d(K)\log{K})$



# code 
## sol_0, sol_2
- numba (JIT)
- solution 1

## sol_1
- python
- solution 1
- moodular class 

## sol_3
- python
- solution 2

## sol_4
- python
- solution 1


# similar
- [ABC212 G - Power Pair](https://atcoder.jp/contests/abc212/tasks/abc212_g)