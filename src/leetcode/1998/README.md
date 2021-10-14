# [Weekly Contest 257](https://leetcode.com/contest/weekly-contest-257)

# [LeetCode 1998. GCD Sort of an Array](https://leetcode.com/problems/gcd-sort-of-an-array/)


# keywords
- GCD
- UnionFind
  - its values are not index but prime factors and elements of an array.
- Disjoint Set 
- prime factorization
- LPF (Least Prime Factor)
- sort
- connected components
  - connect values with prime factors


# summary
## solution 1
- pre-calc LPF with sieve of eratosthenes $O(\max{A}\log{\log{\max{A}}})$
- build UnionFind (size $= \max{A} + 1$)
- $\forall{i},$ 
  - prime factorize $A_i$ with LPF. $O(\log{\max{A}})$
  - $\forall{p} \in \text{prime factors of } A_i, $ unite($p, A_i$). 
    $O(\log{\max{A}}\text{Ackerman}^{-1}(\max{A}))$
- let $B :=$ sorted $A$
- if $\forall{i}, $ same($A_i, B_i$), return true, otherwise return false.
- $O(\max{A}\log{\log{\max{A}}} + N\log{\max{A}}\text{Ackerman}^{-1}(\max{A}) + N\log{N})$

## solution 2
- use DFS instead of UnionFind to calculate connected components.


# code 
## sol_0
- solution 1
- prime factorize with LPF 
- UnionFind


# similar