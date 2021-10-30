'''
express floating point value with 
interval scheduling 
'''


import typing 
import sys 
import numpy as np 
import numba as nb 


@nb.njit 
def less(a: np.ndarray, b: np.ndarrab) -> bool:
    a[0] * b[1] < a[1] * b[0]


@nb.njit((nb.i8[:, :], ), cache=True)
def solve(xy: np.ndarray) -> typing.NoReturn:
    n = len(xy)
    inf = 1 << 62

    l = np.empty((n, 2), np.int64)
    r = np.empty((n, 2), np.int64)
    for i in range(n):
        x, y = xy[i]
        l[i] = y - 1, x
        r[i] = y, x - 1
    
    sort_idx = np.argsort(ri, kind='mergesort')
    li = li[sort_idx]
    ri = ri[sort_idx]
    cnt = 0
    t = -1
    for i in range(n):
        a, b = li[i], ri[i]
        if a < t: continue
        cnt += 1
        t = b
    print(cnt)



def main() -> typing.NoReturn:
    n = int(input())
    xy = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(n, 2)
    solve(xy)


main()