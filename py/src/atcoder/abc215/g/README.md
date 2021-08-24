# [G - Colorful Candies 2](https://atcoder.jp/contests/abc215/tasks/abc215_g)



# keywords 
- combinatorics
- linearity of expectation
- count up 
- complement probability
- the number of kind of counts is $O(\sqrt{N})$
- convolution($O(N\log{N})$)


# summary
1. official editorial solution
- if fix $k$, $ans = \sum_{x_i \in X}{P(x_i)}$, 
  - where $P$ means probability, $x$ means a pattern.
  - $\#X = \displaystyle{{N}\choose{k}}$
- $\sum_{x_i \in X}{P(x_i)} = \sum_{x_i \in X}{\displaystyle{\frac{c_i}{{N}\choose{k}}}}$
  $= \displaystyle{{N}\choose{k}}^{-1}\sum_{x_i \in X}{c_i}$
  - where $c_i$ is number of kind of colors.
- so, it's ok to calculate $\sum_{x_i \in X}{c_i}$
- $\sum_{x_i \in X}{c_i} = \sum_{x_i \in X}{\sum_{color_j \in C}{flg_j}}$
  - where $C$ denotes the set of colors.
  - $flg$ means wheter the color is contained in the pattern or not.
- $$\sum_{x_i \in X}{\sum_{color_j \in C}{flg_j}} 
  = \sum_{color_j \in C}{\sum_{x_i \in X}{flg_j}} \\
  = \sum_{color_j \in C}{f(j)}
  $$
  - where $f(j)$ means the number of patterns in which $color_j$ is contained.
- here, let $f^{-1}(j) :=$ the number of patterns in which $color_j$ is not contained.
  - $f(j) = \displaystyle{{N}\choose{k}} - f^{-1}(j)$
  - $f^{-1}(j) = \displaystyle{{N - cnt_j}\choose{k}}$ where $cnt_j$ is the count of $color_j$ in the given array.
- $$
  \displaystyle{{N}\choose{k}}^{-1}\sum_{x_i \in X}{c_i} 
  = \displaystyle{{N}\choose{k}}^{-1}\sum_{color_j \in C}{f(j)} \\
  = \displaystyle{{N}\choose{k}}^{-1}\sum_{color_j \in C}{(\displaystyle{{N}\choose{k}} - \displaystyle{{N - cnt_j}\choose{k}})} \\
  = \#C - \displaystyle{{N}\choose{k}}^{-1}\sum_{color_j \in C}{\displaystyle{{N - cnt_j}\choose{k}}} \\
  = \#C - \displaystyle{{N}\choose{k}}^{-1}\sum_{l}{\displaystyle{{N - l}\choose{k}} \times \#\{j| cnt_j = l\}}
  $$
  - this can be calculated with $O(\sqrt{N})$ complexity, beacuse the number of $l$ is at most $\sqrt{N}$


2. convolution




## sol_0
- array compression + bincounting
- $O(N(\log{N} + \sqrt{N}))$
- numpy 


## sol_1
- array compression + bincounting
- $O(N(\log{N} + \sqrt{N}))$
- pypy


## sol_2
- bincounting with dict
- $O(N(\sqrt{N}))$
- pypy


## sol_3
- array compression + bincounting
- $O(N(\log{N} + \sqrt{N}))$
- numba (JIT)