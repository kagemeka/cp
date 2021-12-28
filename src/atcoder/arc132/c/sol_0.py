import typing 




def main() -> typing.NoReturn:
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    a = [x - 1 for x in a]
    cnt = [0] * n
    for x in a:
        if x < 0: continue
        cnt[x] += 1
    if max(cnt) >= 2:
        print(0)
        return 
    
    cand = [x for x in range(n) if cnt[x] == 0]
    idx = [i for i in range(n) if a[i] < 0]
    print(cand)
    print(idx)
    MOD = 998_244_353
    
    

main()