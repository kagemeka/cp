# [G - Power Pair](https://atcoder.jp/contests/abc212/tasks/abc212_g)

# [official editorial (movie)](https://www.youtube.com/watch?v=hI8xC_1ZBf8)


# keywords 
- count up
- modulo
- number theory 
- primitive root
- loop values
- Multiplicative Group
- Additive Group
- GCD (Greatest Common Divisors)
- Prime Factorization
- inclusive exclusive theory
- euler function (totient function)
- fast mobius transform



# summary
- fix x and count up the candidates of y
- corner case $(x, y) = (0, 0)$
- y is arbitral
- $\forall{x}$ find the possible $count_{y}(x)$, that is, $ans = 1 + \sum_{x = 1}^{p - 1} count_{y}(x)$
- this is equal to calc $ans = 1 + \sum_{x = 1}^{p - 1} \displaystyle{\frac{p - 1}{gcd(p - 1, x)}}$. (most important)
  - where `1` comes from (x, y) = (0, 0)
- calc $gcd(p - 1, x)$ per $g\in\{g: gcd(p - 1, x)\}$
  - method 1
    - this is similar to [ABC020 D - LCM Rush](https://atcoder.jp/contests/abc020/tasks/abc020_d)
    - let $f(x) =$ the number of x such that $p - 1\equiv 0 (mod\ x)$, that is, $\sum_{x|p - 1} 1$
    - let $g(x) =$ the number of x such that $gcd(p - 1, x) = x$
    - by there, $g(x) = f(x) - \sum_{y \in \{x|y, x \lt y \le p - 1 \}}g(y)$
    - ans $= 1 + \sum_{d|p-1} \frac{p - 1}{d} * g(d)$
    
  - method 2: euler't totient function
    - let $f(n, g) = \sum_{x \in \{\gcd(x, n) = g, 1 \le x \le n\}} {1}$
    - when $\gcd(x, n) = g$, by letting $x = gx\prime, n = gn\prime$, then $\gcd(x\prime, n\prime) = 1$
    - thus, $f(n, g) = \sum_{x \in \{gcd(x, n\prime) = 1, 1 \le x \le n\prime\}} {1}$
      $= (n\prime) = \varphi(\frac{n}{g})$
    - ans $= 1 + \sum_{g \in \{gcd(p - 1, g) = g, 1 \le g \le p - 1 \}} {\varphi(\frac{p - 1}{g}) * \frac{p - 1}{g}}$
      $= 1 + \sum_{d|p - 1} {\varphi(\frac{p - 1}{d}) * \frac{p - 1}{d}} = 1 + \sum_{d|p - 1} {\varphi(d) * d}$

  - method 3: fast mobius transformation 
    - [for detail](https://youtu.be/hI8xC_1ZBf8?t=2871)


# tips 
- primitive root
  - reference
    - [wiki](https://en.wikipedia.org/wiki/Primitive_root_modulo_n)
    - [wolfman](https://mathworld.wolfram.com/PrimitiveRoot.html)
    - [manabitimes](manabitimes.jp/math/842)
    - [drken blog](https://drken1215.hatenablog.com/entry/2021/08/01/163600)
  - condtion `r` is primitive root 
    - $r, r^2, r^3, ...r^{p - 1} (\mod{p})$ are pairwise distinct
    - $r^{p - 1} \equiv 1 \mod{p}$ ($Z/PZ$ (multiplicative group) is isomorphic to $Z/(P - 1)Z$ (Additive group)
  - $x^n\equiv{y}\ (mod\ p) \leftrightarrow\ r^{an} \equiv{r^b}\ (mod\ p) \leftrightarrow an\equiv{b}\ (mod\ p - 1)$

- fast zeta-transform(`FZT`), fast mobius-transform(`FMT`)
  - [qiita](https://qiita.com/convexineq/items/afc84dfb9ee4ec4a67d5)

- euler's totient function
  - reference
    - [drken blog](https://drken1215.hatenablog.com/entry/2021/08/01/163600)
    - [wiki](https://en.wikipedia.org/wiki/Euler%27s_totient_function)
    - [wolfman](https://mathworld.wolfram.com/TotientFunction.html)
  - $\varphi(n) = \sum_{x \in \{x\perp{n}, 1 \le x \le n \}} {1} = \sum_{x \in \{\gcd(x, n) = 1, 1 \le x \le n \}} {1}$

- Red Black Tree





## sol_0
- standard


## sol_1
- standard 
- modular class
- TLE 



## sol_2
- numba (JIT)


## sol_3
- numba (AOT)



## sol_4
- Euler's totient


## sol_5
- Euler's totient
- numba (JIT)


## sol_6
- Euler's totient
- numba (AOT)


## sol_7
- Euler's totient with prime numbers
- standard


## sol_8
- Euler's totient with prime numbers 
- numba (JIT)

## sol_9
- Euler's totient with prime numbers 
- numba (AOT)


## sol_10
- fast mobius transform
- standard



## sol_11
- fast mobius transform
- numba (JIT)
- rbtree (red black tree)



# similar
- [ABC020 D - LCM Rush](https://atcoder.jp/contests/abc020/tasks/abc020_d)


