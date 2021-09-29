# [AtCoder ABC018 D - バレンタインデー](https://atcoder.jp/contests/abc018/tasks/abc018_4)


# keywords 
- brute force $x$ on $f(x, y)$
- bits brute force 
- combinations 
- next combination
- bit count


# summary 
- brute force all the girls' combinations.
- sort boys
- $O(\displaystyle{N\choose{P}}(NM + M\log{M}))$


# code 
## sol_0, sol_3
- numpy 


## sol_1
- numba (JIT)
- enumerate only valid combinations

## sol_2
- numba (JIT)
- bits brute force
- pruning
- $O(2^N(NM + M\log{M}))$



# similar 


