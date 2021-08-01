# [G - Power Pair](https://atcoder.jp/contests/abc212/tasks/abc212_g)

# [official editorial (movie)](https://www.youtube.com/watch?v=hI8xC_1ZBf8)


# keywords 
- module 
- number theory 
- primitive root
- loop values
- corner case $(x, y) = (0, 0)$
- y is arbitral
- $\forall{x}$ find the possible $count_{y}(x)$, that is, $ans = 1 + \sum_{x = 1}^{p - 1} count_{y}(x)$
- this is equal to calc $ans = 1 + \sum_{x = 1}^{p - 1} \displaystyle{\frac{p - 1}{gcd(p - 1, x)}}$. (most important)
- calc $gcd(p - 1, x)$ per $g\in\{g: gcd(p - 1, x)\}$
  - this is similar to [ABC020 D - LCM Rush](https://atcoder.jp/contests/abc020/tasks/abc020_d)



# tips 
- primitive root
  - reference
    - [wiki](https://en.wikipedia.org/wiki/Primitive_root_modulo_n)
    - [wolfman](https://mathworld.wolfram.com/PrimitiveRoot.html)
    - [manabitimes](manabitimes.jp/math/842)
  - condtion `r` is primitive root 
    - $r, r^2, r^3, ...r^{p - 1} (\mod{p})$ are pairwise distinct
    - $r^{p - 1} \equiv 1 \mod{p}$
  - $x^n\equiv{y}\ (mod\ p) \leftrightarrow\ r^{an} \equiv{r^b}\ (mod\ p) \leftrightarrow an\equiv{b}\ (mod\ p - 1)$


# similar
- [ABC020 D - LCM Rush](https://atcoder.jp/contests/abc020/tasks/abc020_d)



## sol_0
- standard


## sol_1
- standard 
- modular class
- TLE 


