# [LCM of GCDs](https://atcoder.jp/contests/arc124/tasks/arc124_c)



## sol_0 (TLE)
- x should be in divisors of a[0] and y should be in divosors of b[0]
- brute force (fix x and y)
- number of divisors of n under 10^9 is at most around 1500. for detail, see [highly composite number](https://en.wikipedia.org/wiki/Highly_composite_number)


## sol_1, sol_2, sol_3, sol_4
- optimize with numba