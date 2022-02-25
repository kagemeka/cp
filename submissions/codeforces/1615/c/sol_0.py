import typing 


def solve() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input()))
    b = list(map(int, input()))
    # a, b, c, d := 00, 01, 10, 11
    # choose c first -> c - 1, d, a + 1, b -> a + 1, b - 1, c - 1, d + 1 -> ... (even, b = c)
    # choose d first -> c, d - 1, a, b + 1 -> a - 1, b + 1, c + 1, d - 1 -> ... (odd, a = d - 1)
    cnt = [0] * 4
    for i in range(n):
        j = 0 
        if a[i] == 1: j |= 1 << 1
        if b[i] == 1: j |= 1 << 0
        cnt[j] += 1
    
    inf = 1 << 60
    mn = inf 
    if cnt[1] == cnt[2]: mn = min(mn, cnt[1] * 2)
    if cnt[0] == cnt[3] - 1: mn = min(mn, cnt[0] * 2 + 1)
    print(-1 if mn == inf else mn)
    

def main() -> typing.NoReturn:
    t = int(input())
    for _ in range(t):
        solve()

main()