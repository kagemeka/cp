# [AtCoder ARC125 B - Squares](https://atcoder.jp/contests/arc125/tasks/arc125_b)



# keywords
- math
- modular 
- count up 


# summary 
- $x^2 - y = z^2 \leftrightarrow (x + z)(x - z) = y$
- $p := x + z, q := x - z$
- $1 \le pq = y \le N, q \le p, p - q = 2z \equiv 0 \mod 2, 1 \le x = (p + q) / 2 \le N$
- answer = $\sum_{q=1}^{\lfloor{\sqrt{N}}\rfloor}{1 + \displaystyle{\lfloor{\frac{\lfloor{\displaystyle{\frac{N}{q}}}\rfloor - q}{2}}\rfloor}}$
- $O(\sqrt{N})$


# code 
## sol_0


# similar 