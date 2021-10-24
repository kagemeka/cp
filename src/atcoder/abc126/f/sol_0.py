r"""Note.

\forall{n \le 2}\ \xor_{i=0}^{2^n-1}{i} = 0
\xor_{0 \le i \lt 2^n, i \neq k (0 \le k \lt 2^n)}{i} = k
"""
import typing 
import sys 
# import numpy as np
# import numba as nb 


def main() -> typing.NoReturn:
    m, k = map(int, input().split())
    n = pow(2, m)
    if k >= n or m == k == 1:
        print(-1)
        return
    
    if m == 1:
        print(0, 0, 1, 1)
        return
    
    a = [-1] * (n << 1)
    ptr = 0 
    for i in range(n):
        if i == k: continue
        a[ptr] = i
        ptr += 1
    a[ptr] = k
    ptr += 1
    for i in range(n - 1, -1, -1):
        if i == k: continue
        a[ptr] = i
        ptr += 1
    a[-1] = k
    print(*a)

main()