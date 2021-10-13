# [AtCoder Typical90 006 - Smallest Subsequence（★5）](https://atcoder.jp/contests/typical90/tasks/typical90_f)



# keywords 
- priority queue
- binary heap queue
- smalles subsequence in lexicographically order.
- greedy


# summary
- let $l := -1$
- first letter is first occurrence of smallest value in $\{S_{l + 1}, S_{l + 2}, ...S_{n - k}\}$
  - relace $l$ with the index
- second letter is first occurrence of smallest value in $\{S_{l + 1}, S_{l + 2}, ...S_{n - k + 1}\}$
- third letter is ...
- this is achievable with Priority queue. $O(N\log{N})$



# code 
## sol_0
- numba (JIT)



# similar 