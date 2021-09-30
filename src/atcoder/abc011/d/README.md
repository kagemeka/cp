# [AtCoder ABC011 D - 大ジャンプ](https://atcoder.jp/contests/abc011/tasks/abc011_4)


# keywords 
- probability
- count up


# summary 
- consider constraints
  - if $x \not\equiv 0 \mod d \lor y \not\equiv 0 \mod d$
    - it's impossible to achieve target.
  - answer is not changed by letting $x := |x|, y := |y|$
  - $\therefore\ x := \frac{|x|}{d}, y := \frac{|y|}{d}$
    - map distance -> move count capacity.
  - then, if $n < x + y \lor n - x - y \not\equiv 0 \mod 2$
    - it's impossible to achieve target.
  - otherwise, at least one path to achieve target exists.
- we must move to up at least $y$ times and to right at least $x$ times.
- $\therefore$ consider split remaining $n - x - y$ moves to up, down, right, left
  - be careful of that $up + down \equiv right + left \equiv 0 \mod 2$
- these events are mutual independent.
$$
\text{answer} \\
= \displaystyle{\frac{1}{4^N}}\sum_{i=0, i \le n - x - y, i := i + 2}{\displaystyle{\frac{N!}{u!d!l!r!}}} \\
= \displaystyle{\frac{1}{4^N}}\sum_{i=0, i \le n - x - y, i := i + 2}{\displaystyle{N\choose{u}}\displaystyle{(N - u)\choose{d}}\displaystyle{(N - u - d)\choose{l}}\displaystyle{(N - u - d - l)\choose{r}}}

$$
- where
  - $d := \frac{i}{2}$
  - $u := y + d$
  - $l := \frac{(n - x - y - i)}{2}$
  - $r := x + l$
- be careful of overflow and calculation order.

- by preprocessing choose table with pascal $O(N^2)$, answer can be calculated $O(N)$
- total is $O(N^2)$


# code 
## sol_0, sol_2
- scipy.special.comb

## sol_1
- numba (JIT)

# similar 

