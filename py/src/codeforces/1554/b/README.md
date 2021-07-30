# [B. Cobb](https://codeforces.com/contest/1554/problem/B)



# summary 
- k is small. so there must be something revolging it.
- let f(i, j) = i * j - k * (a[i] | a[j])
- i * j = O(n^2) and k * (a[i] | a[j]) = O(nk), that means f(i, j) must be larger for bigger i, j. 
- think about theoretical values
  - what is the `smallest i` which can contribute to the result (f(i, j): i < j)?
  - at first, think about smallest i when we `fix j`
  - think about theoretical maximum value for the f(i, j)
    - it's when i pairs with n and a[i] = a[j] = 0
    - so maximum value for f(i, j) = i * j - k * 0 = i * j
  - think about theoretical minimum value for the f(j - 1, j)
    - x | y <= x + y, that is, `x | y = O(x + y)`
    - since 0 <= a[i] <= n, the maximum possible of value any a[i] | a[j] is <= 2 * n.
    - so minimum value for f(j - 1, j) = (j - 1) * j - k * 2n = j ** 2 - j - 2kn
  - for i to contribute to the result, f(i, j) must be greater than f(j - 1, j).
  - that is, f(i, j) > f(j - 1, j) -> i * j > j ** 2 - j - 2kn -> i > j - 1 - 2kn/j -> i > j - 1 - floor(2kn / j)
  - let g(j) = j - 1 - floor(2kn / j).
  - g(j) is monotonic increasing for j. maximum g(j) is g(n) = n - 2k - 1
  - then, if f(i, n) > f(n - 1, n) -> i > n - 2k - 1.
  - so if i < n - 2k, that won't generate a value greater than theoritical minimum value of f(n - 1, n).
    - in other words, `if we take f(i, j): i < n - 2k, instead we can take f(n - 1, n)` because i < n - 2k.
    - be careful of `f(i, n) > f(n - 1, n)` -> `i > n - 2k - 1`, but not `n - 2k - 1` -> `f(i, n) > f(n - 1, n)` 
- This indices us that we just have to check the paris f(i, j) such that  i, j >= n - 2k -> O(k^2)
which is the heaviest pair.



# keywords
- brute force
- By fixing i or j, can we limit the range of the other.
  - think about theoritical value
  - the way might use binary search, or two pointers and so on.
- consider wether it's possible to revole explicit constraints.



## sol_0
- brute force
- O(tk^2), O(6 * 10^7)      
- pypy.
