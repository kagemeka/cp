n = int(input())
for _ in range(n):
    b, t = map(int, input().split())
    lhs = t * 9 + 160
    rhs = b * 5
    ans = 'Lower' if rhs < lhs else 'Higher' if rhs > lhs else 'Same'
    print(ans)