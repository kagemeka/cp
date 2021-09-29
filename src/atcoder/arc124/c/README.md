# [LCM of GCDs](https://atcoder.jp/contests/arc124/tasks/arc124_c)



## sol_0 (TLE)
- x should be in divisors of a[0] and y should be in divosors of b[0]
- brute force (fix x and y)
- number of divisors of n under 10^9 is at most around 1500. for detail, see [highly composite number](https://en.wikipedia.org/wiki/Highly_composite_number)


## sol_1, sol_2, sol_3, sol_4
- optimize with numba



## sol_5
- the patterns of gcd of N integers may be not so many as large N become.
  - as large N, the gcd of integers -> 1.
- brute force
- dfs
- cache (functools.lru_cache)


# sol_6, sol_7, sol_8
- this solution is same concept with sol_5.
- bfs 
- hash table queue (cache)



# tips
- GCD of multiple integers equals the product of the  prime factors common to all the numbers.
- this value can also be calculated by repeatedly taking the GCDs of pairs of numbers.
