# [AtCoder Typical90 004 - Cross Sum（★2）](https://atcoder.jp/contests/typical90/tasks/typical90_d)



# keywords 
- cumsum
- grid 
- reduce calls of print function with string.



# summary
## solution 1
- $B_{i, j} = S_{up}(i, j) + S_{left}(i, j) + S_{right}(i, j) + S_{down}(i, j) - 3A_{i, j}$

## solution 2
- $B_{i, j} = S_{row}(i) + S_{col}(j) - A_{i, j}$


# code 
## sol_0
- numpy
- solution 1
- TLE


## sol_1
- numba (JIT)
- solution 1
- TLE


## sol_2
- numpy
- solution 1
- reduce calls of print function


## sol_3
- numpy
- solution 2
- reduce calls of print function

- 

# similar 