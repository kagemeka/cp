# [AtCoder Typical90 005 - Restricted Digits（★7）](https://atcoder.jp/contests/typical90/tasks/typical90_e)


# keywords 
- count up
- digits DP
- $A^N, N \le 10^{18}, 10^{9} \rightarrow$ doubling 
- matrix power $O(B^3\log{N})$ $\rightarrow$ TLE ($B = |A|$)
- replace matrix power with kitamasa method
- Kitamasa method $O(B^2\log{N})$
- Fast Kitamasa method $O(B\log{B}\log{N})$


# summary
- $N$ is so large -> doubling
  - $N = c_02^0 + c_12^1 + ... + c_{59}2^{59}$
  - $c_i \in \{0, 1\}$
- $A_{i, r} :=$ cases where number of digits is $2^{i}$, remainder is $r$
- transition
  - $A_{i + 1, r} = \sum_{j=0}^{j=B - 1} A_{i, j}A_{i, k}$
    - where
      - $j\times 10^{2^{i}} + k \equiv r \mod{B}$
    - $O(B)$
  - for each $i$, O(B^2)
  - $i$ is $O(\log{N})$



# code 
## sol_0
- numba (JIT)


## sol_1
- numba (JIT)
- preprocess $A$


# similar 
- [AtCoder TDPC T - フィボナッチ](https://atcoder.jp/contests/tdpc/tasks/tdpc_fibonacci)