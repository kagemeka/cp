import typing 




def f(x: int, k: int) -> typing.List[int]:
    cnt = [0] * k
    for i in range(k):
        q, r = divmod(x, 1 << (i + 1))
        cnt[i] = q * (1 << i) + max(0, r - (1 << i) + 1)
    return cnt

def solve() -> typing.NoReturn:
    l, r = map(int, input().split())
    # f(N) = for each bit, how many number has the bit under N 
    # (r - l + 1) - max(f(r) - f(l - 1))
    k = 23
    cnt_r = f(r, k)
    cnt_l = f(l - 1, k)
    for i in range(k):
        cnt_r[i] -= cnt_l[i]
    print(r - l + 1 - max(cnt_r))
    

def main() -> typing.NoReturn:
    t = int(input())
    for _ in range(t):
        solve()

main()