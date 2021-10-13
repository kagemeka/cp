# [AtCoder ABC218 D - Rectangles](https://atcoder.jp/contests/abc218/tasks/abc218_d)



# keywords 
- brute-force 
- binary search
- shakutori method 
- array compression 



# summary 
## solution 1
- fix lower-left and upper-left
- at first, compress array and calc $\exist{(x, y)}$. (not necessary)
- sort X, Y by X
- ansewer $= \sum_x{\sum_{i, j(X_i = X_j = x, i < j)}{\sum_{x\prime x}{\exist{(x\prime, Y_i)} \land \exist{(x\prime, Y_j)}}}}$


## solution 2
- fix lower-left and upper-right
- at first, compress array and calc $\exist{(x, y)}$. (not necessary)
- answer $= \sum_{i, j}{X_i \lt X_j \land Y_i \lt Y_j \land \exist{(X_i, Y_j)} \land \exist{(X_j, Y_i)}}$



# code
## sol_0
- numba (JIT)
- solution 1


## sol_1
- numba (JIT)
- solution 2


# similar


