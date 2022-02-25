# [A. Cherry](https://codeforces.com/contest/1554/problem/A)



# summary
- if choose a[i] as leftmost, a[i] or a[i + 1] must be peak.
- otherwise, we can product greater value by choose a[j]: j != i as leftmost.
- ans = max(a[i] * a[i + 1]) (for i in 1 <= i <= n - 1)


# keywords
- brute force
