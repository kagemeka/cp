# [AtCoder ARC119 C - ARC Wrecker 2](https://atcoder.jp/contests/arc119/tasks/arc119_c)



# keywords 
- count up 
- group by cumsum value 
- odd sum = even sum
- array compression 
- binary search tree
- hash map


# summary
- if fix $l, r$, it's enough to check whether 
  $\sum_{i=l, i \le r, i := i + 2}A_i = \sum_{i=l + 1, i \le r, i := i + 2}A_i$

- at first, multiply $A_2, A_4,, A_6, ...$  by $-1$.
- calculate $S :=$ cumulative sum of $A$.
- let $f(x) := \text{count of } x \text{ in } S$
- ans = $f(0) + \sum_{v \in S} \displaystyle{f(v)\choose{2}}$ 


# code 
## sol_0
- numpy


## sol_1
- numba (JIT)


# similar 
