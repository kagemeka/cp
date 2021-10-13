# [AtCoder Typical90 015 - Don't be too close（★6）](https://atcoder.jp/contests/typical90/tasks/typical90_o)


# keywords 
- count up 
- combinations
- math 
- harmonic series


# summary
- $\forall{1 \le k \le N}$
  - print $f(k)$
- let $f(k) :=$ count such that any two pair's difference is more than or equal to $k$.
  - fix $|S| = x$
  - $f(k) = \sum_{x=1}^{N}{{N - (k - 1)(x - 1)}\choose{x}}$
  - this can be calculated with $O(N\log{N})$ in total. $\because {{N - (k - 1)(x - 1)}\choose{x}} = 0 (\text{when } N - (k - 1)(x - 1) \lt x)$
  - harmonic series

  

# editorial
- [twitter](https://twitter.com/e869120/status/1382827276673306624/photo/1)


# code 
## sol_0
- numba (JIT)


# similar 
