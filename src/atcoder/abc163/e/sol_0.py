import typing 
import sys 
import numpy as np 
import numba as nb 


@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
    n = len(a)
    b = np.full(n, -1, np.int64)
    s = 0
    for i in np.argsort(a, kind='mergesort')[::-1]:
        d = 0
        p = i
        for j in range(n):
            if b[j] != -1: continue
            if abs(j - i) <= d: continue
            d = abs(j - i)
            p = j
        b[p] = i
        s += d * a[i]
    print(s)
    

def main() -> typing.NoReturn:
    n = int(input())
    a = np.array(sys.stdin.readline().split(), dtype=np.int64)
    solve(a)


main()