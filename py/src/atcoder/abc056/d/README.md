# [AtCoder ABC056 D - No Need](https://atcoder.jp/contests/abc056/tasks/arc070_b)


# keywords 
- sort
- binary search
- DP
- preprocess DP from left and right.
- cumsum 
- bits
- bits DP 

# summary
## solution 1 DP + binary search 
- a card $i$ is not needed $\leftrightarrow$ there is a good set $S$ containing $i$ and $S\setminus{i}$ is also a good set.
- in otherwords, a card $i$ is needed $\leftrightarrow$ there is set $S \setminus{i}$ not containing $i$ such that $K - A_i \le \sum_{j \in S}A_j \lt K $ and $S \cup i$ is a good set.
- whether $i$ is needed or not can be judged with $O(NK)$ DP easily.
- by the way, if card $i$ is not needed, $\forall{j, A_j \le A_i}\ j$ is not needed.
  - there is a good set $S$ not containing $i$, let $S\prime = S\setminus{j} \cup i$, then $S\prime$ must be a good set and not containing $j$
- therefore we sort $A$ at first, and binary search lowest $i$ such that $A_i$ is needed, or highest $i$ such that $A_i$ is not needed.
- $O(N\log{N} + NK\log{N}) = O(NK\log{N})$

## solution 2 preprocess DP + cumulative sum (+ binary search)
- using DP is same to solution 1.
- $dpl_{i, j} =$ whether it's possible to make $j$ by using any of only $\{A_1, A_2, ..., A_i\}$
- $dpr_{i, j} =$ whether it's possible to make $j$ by using any of only $\{A_i, A_{i + 1}, ..., A_N\}$
- $dpl_{*, *}, dpr_{*, *} \in \{0, 1\}$
- $dpl_{0, 0} = dpr_{N + 1, 0} = 1$
- whether $i$ is needed or not can be judged with $O(K)$
  - consider we check $dpl_{i - 1, x} + dpr_{i + 1, y}$.
  - $K - A_i \le x + y \lt K \land (x, y) \text{ are valid}$
  - if fix $x\\$
    $K - A_i - x \le y \lt K - x \leftrightarrow \\$
    $\exists{y, K - A_i - x \le y \lt K - x}, \ dpr_{i + 1, y} = 1 \leftrightarrow \\$
    $\sum_{j=\max{(1, K - A_i - x)}}^{K - x - 1}{dpr_{i + 1, j}} \ge 1$
  - this can be calculated with $O(K)$ by preprocessing cumulative sum of $dpr_{i + 1}$
- total to $O(NK)$
- by doing sort A at first and binary search, $O(N\log{N} + NK + K\log{N})$ 


# code 
## sol_0
- numba (JIT)
- binary search 

## sol_1
- numpy
- binary search 

## sol_2
- python
- bits
- binary search 


## sol_3, sol_4
- numba (JIT)
- preprocess DP
- cumulative sum

## sol_5
- numba (JIT)
- preprocess DP
- cumulative sum 
- binary search 


## sol_6
- numpy
- preprocess DP
- cumulative sum 
- binary search 


# similar 

