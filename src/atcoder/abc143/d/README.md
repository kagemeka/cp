# [AtCoder ABC143 D - Triangles](https://atcoder.jp/contests/abc143/tasks/abc143_d)


# keywords 
- brute-force
- fix 2 and search remaining 1 efficiently 
- binary search
- shakutori method
- convolution


# summary
## solution 1
- total $a, b, c$ patterns is $N\choose{3}$
- let $a \lt b \lt c$
- if brute-force $a, b$ and search $c$ with binary search or shakutorimethod
- $O(N^2\log{N})$ (binary search)
- $O(N^2)$ (shakutori method)

## solution 2
- convolution
- for detail, see [editorial](https://img.atcoder.jp/abc143/editorial.pdf)


# code 
## sol_0
- numba (JIT)
- shakutori method



# similar