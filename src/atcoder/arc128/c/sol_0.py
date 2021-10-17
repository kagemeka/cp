import typing 
import sys 
import numpy as np 
import numba as nb 



@nb.njit((nb.i8[:], nb.i8, nb.f8), cache=True)
def solve(a: np.ndarray, m: int, s: float) -> typing.NoReturn:
    n = len(a)
    buf = []
    mx = -1
    for i in range(n):
        if a[i] <= mx: continue
        buf.append(i)
        mx = a[i]
    que = np.array(buf)[::-1]
    cum = np.hstack((np.array([0]), a.cumsum()))
    print(cum)
    print(que)


    r = n
    while True:
        
    res = .0
    r = n
    for l in que:
        # x  * (r - l) <= s, x <= m
        x = s / (r - l)
        if s <= 0: continue
        if s <= m * (r - l):
            res += x * (cum[r] - cum[l])
            print(res)
            s -= x * (r - l)
            # return 
        else:
            res += m * (cum[r] - cum[l])
        s -= m * (r - l)
        print(s)
        r = l
    print(s)
    print(res)
    


def main() -> typing.NoReturn:
    n, m, s = map(int, input().split())
    a = np.array(
        sys.stdin.readline().split(),
        dtype=np.int64,
    )
    solve(a, m, s)


main()