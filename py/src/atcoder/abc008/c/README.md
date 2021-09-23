# [AtCoder ABC008 C - コイン](https://atcoder.jp/contests/abc008/tasks/abc008_3)



# keywords 
- probability 
- expectation 
- math


# summary 
- $E(X) = \sum_\text{perm}{x_if_X(x_i)}$
  - $x_i :=$ number of face up coin after operations.
  - $f_X(x_i) :=$ probability of the permutation is perm.
  - $f_X(x_i) = \displaystyle{\frac{1}{N!}}$
$$
E(X) = \displaystyle{\frac{1}{N!}}\sum_\text{perm}{x_i} \\
= \displaystyle{\frac{1}{N!}}\sum_\text{perm}\sum_{i}
  \begin{cases}
  1 & \text{if coin}_i \text{ is face up} \\
  0 & \text{otherwise}
  \end{cases} \\
= \sum_{i}\displaystyle{\frac{1}{N!}}\sum_\text{perm}
  \begin{cases}
  1 & \text{if coin}_i \text{ is face up} \\
  0 & \text{otherwise}
  \end{cases} \\
= \sum_{i}\text{probability of coin}_i \text{ is face up through all the permutations.} \\
= \sum_{i} \text{probability of coin}_i \text{'s order is odd in divisors of C}_i \text{through all the permutations}.
$$


# code 
## sol_0
- numpy 


## sol_1
- numba (JIT) 


# similar 
