# [F - Common Prefixes](https://atcoder.jp/contests/abc213/tasks/abc213_f?lang=ja)



# Editorial
- [official site](https://atcoder.jp/contests/abc213/editorial/2391)
- [official youtube](https://www.youtube.com/watch?v=XX2oIn6-Gt4)
- [catupper youtube](https://www.youtube.com/watch?v=8IxLxfGB2_A)



# keywords 
- suffix array 
- lcp array 
- height array 
- cummulatie sum
- store height and the length.
- online update with stack
- SA-IS
- doubling
- counting sort



# summary
- calculate suffix array and lcp array.
  - suffix array: $O(N)$ SA-IS
  - lcp array: $O(N)$ Kasai
- then, for detail, see `sol_1`. or editorial



## sol_0
- dataclasses occurs RE with PyPy
- TLE with Python


## sol_1
- rewrite without dataclasses
- PyPy


## sol_2
- numba (JIT)
- slow


## sol_3
- numba (AOT)
- import error?


## sol_4
- calc Suffix Array with Doubling and counting sort 
- pypy
- TLE 




# reference
- [submission by kiri](atcoder.jp/contests/abc213/submissions/24899399)


# similar 
- [AtCoder ARC060 F - Best Representation](https://atcoder.jp/contests/arc060/tasks/arc060_d)
- [LeetCode 1944. Number of Visible People in a Queue](https://leetcode.com/problems/number-of-visible-people-in-a-queue/)

