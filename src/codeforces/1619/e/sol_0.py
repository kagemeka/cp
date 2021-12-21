import typing 


def solve() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    exist = [False] * (n + 1)
    cnt = [0] * (n + 1)
    for x in a:
        exist[x] = True
        cnt[x] += 1
    
    for i in range(n):
        exist[i + 1] &= exist[i]
    
    s = cnt.copy()
    for i in range(n):
        s[i + 1] += s[i]
    res = [-1] * (n + 1)
    res[0] = cnt[0]
    
    c = 0
    j = -1
    for i in range(1, n + 1):
        if not exist[i - 1]: break
        if exist[i - 1]:
            res[i] = cnt[i]
            continue
        if s[i - 1] <= i - 1: break
        if j == -1:
            j = i - 2
            while cnt[j] <= 1:
                j -= 1
                
            cnt[j] -= 1
            cnt[i - 1] += 1
            c += i - 1 - j
        c = cnt[i]
        
    print(*res, 'a')
        
    

def main() -> typing.NoReturn:
    t = int(input())
    for _ in range(t):
        solve()

main()