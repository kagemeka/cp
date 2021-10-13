# [AtCoder ABC186 E - Throne](https://atcoder.jp/contests/abc186/tasks/abc186_e)


# keywords 
- euler phi function
- prime number 
- fermat little theorem
- extended GCD 
- CRT (chinese remainder theorem)
- Garner algorithm 
- math 
- modular


# summary 
## solution 1 ExtGCD
- let $x$ is answer
- $kx + s \equiv 0 \mod{N} \leftrightarrow x \equiv -sk^{-1} \mod{N}$
- $\exist{x, y}, kx + Ny = 1 \leftrightarrow x \equiv k^{-1} \mod{N}$
- so at first, let $d := \gcd(k, N)$, $k := k/d, N := N/d, s := s/d$ to make $\gcd(k, N) = 1$
  - if not $d|s$, answer does not exist.
- calculate $k^{-1} = x$ such that $kx + Ny = 1$
- answer is $-sx \mod{N}$


## solution 2 Euler Totien Function
- $a^{\varphi(N)} \equiv 1 \mod{N} (a \bot N)$
- so at first, let $d := \gcd(k, N)$, $k := k/d, N := N/d, s := s/d$ to make $\gcd(k, N) = 1$
  - if not $d|s$, answer does not exist.
- calculate $x = k^{-1} = k^{\varphi(N) - 1}$
- answer is $-sx \mod{N}$


## solution 3 CRT
- calc $y = s + xk$
  $\begin{cases}
  y \equiv 0 \mod{N} \\
  y \equiv s \mod{K} \\
  \end{cases}$
  with Chinese Remainder Theorem
- if $s \not\equiv 0 \mod{\text{lcm}(N, k)}$ answer does not exist.
- otherwise, 
  $\text{answer} = 
  \begin{cases} 
  \displaystyle{\frac{y}{d}} & \text{if } y \ge s \\
  \displaystyle{\frac{y + \text{lcm}(N, k)}{d}} & otherwise
  \end{cases}$



# editorial
- [youtube](https://www.youtube.com/watch?v=hY2FicqnAcc)



# code 
## sol_0
- numba (JIT)
- extGCD


## sol_1
- numba (JIT)
- euler totient function


## sol_2
- numba (JIT)
- crt


## sol_3
- python
- std pow(k, -1, mod)

## sol_4
- numba (JIT)
- Garner algorithm 


# similar 

