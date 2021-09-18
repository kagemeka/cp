# [AtCoder ABC202 D - aab aba baa](https://atcoder.jp/contests/abc202/tasks/abc202_d)



# keywords 
- string
- permutations
- count up 
- k-th string in rexicographically order.
  - fix characters from head to tail in order.
- pascal
- binomial
- choose
- combinations


# summary
- fast permutation simulation
- consider fixing i-th character
  - if number of strings that start with 'a' is less thatn $k$, i-th character is 'b'
  - otherwise, i-th character is 'a' 




# code 
## sol_0
- numba (JIT)
- dfs


## sol_1
- numba (JIT)
- bfs


## sol_2
- numba (JIT)
- pascal choose



# similar 