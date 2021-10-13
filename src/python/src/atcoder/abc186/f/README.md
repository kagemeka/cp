# [AtCoder ABC186 F - Rook on Grid](https://atcoder.jp/contests/abc186/tasks/abc186_f)




# keywords 
- grid 
- count up 
- math
- inclution-exlsusion principle
  - https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle
- fenwick tree
- segment tree 
- scanning algorithm 


# summary
## solution 1
- $A \cup B = A + B - A\cap B$
- count up right -> down (easy)
- count up down -> right (easy)
- remove duplicates (hard)
  - using scanning algorithm and fenwick tree 

## solution 2
- $A \cup B = A + B \cap \overline{A}$



# editorial
- [youtube](https://www.youtube.com/watch?v=hY2FicqnAcc)


# code 
## sol_0
- numba (JIT)
- solution 1
