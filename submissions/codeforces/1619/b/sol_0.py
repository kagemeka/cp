import typing 


def solve() -> typing.NoReturn:
    n = int(input())
    cnt = 1 # 1 
    for i in range(2, n + 1):
        x = i * i
        if x > n: break
        cnt += 1
        x *= i
        if x <= n: cnt += 1
        x *= x
        if x <= n:
            cnt -= 1
    print(cnt)
        
         
    

def main() -> typing.NoReturn:
    t = int(input())
    for _ in range(t):
        solve()
    

main()