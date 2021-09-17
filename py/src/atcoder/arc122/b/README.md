# [AtCoder ARC122 B - Insurance](https://atcoder.jp/contests/arc122/tasks/arc122_b)



# keywords 
- ternary search
- median 
- downward convez



# summary
- $f(x) = \displaystyle{\frac{1}{N}}(Nx + \sum_i{A_i} - \sum_i{\min{(A_i, 2x)}})$
## solution 1 $O(N)$
- sort $A$
- if let $j =$ minimum $i$ such that $2x \le A_i$
- $f(x) = \displaystyle{\frac{1}{N}}(Nx - \sum_{i=j + 1}^{N}{2x} + Const)$
- $f\prime(x) = 1 - \displaystyle{\frac{2(N - j)}{N}}$ 
- $f\prime(x) = 0 \leftrightarrow j = \displaystyle{\frac{N}{2}}$ that is, $A_j$ is the median. 


## solution_2 ternary search $O(N\log{N})$


# code 
## sol_0
- numpy
- median
- solution 1


## sol_1
- numpy
- ternary search
- solution 2

# similar