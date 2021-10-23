import typing 
import sys 
import numpy as np 
import numba as nb 


@nb.njit((nb.i8[:], ), cache=True)
def next_permutation(a: np.ndarray) -> typing.NoReturn:
    n = a.size
    i = -1
    for j in range(n - 1, 0, -1):
        if a[j - 1] >= a[j]:
            continue
        i = j - 1
        break
    if i == -1:
        a[:] = -1
        return
    a[i + 1:] = a[i + 1:][::-1]
    for j in range(i + 1, n):
        if a[i] >= a[j]:
            continue
        a[i], a[j] = a[j], a[i]
        break


@nb.njit
def csgraph_to_directed(g: np.ndarray) -> np.ndarray:
    m = len(g)
    g = np.vstack((g, g))
    g[m:, :2] = g[m:, 1::-1]
    return g


@nb.njit
def sort_csgraph(n: int, g: np.ndarray) -> typing.Tuple[(np.ndarray, ) * 3]:
    idx = g[:, 0] << 30 | g[:, 1]
    sort_idx = np.argsort(idx, kind='mergesort')
    g = g[sort_idx]
    original_idx = np.arange(len(g))[sort_idx]
    edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
    return g, edge_idx, original_idx


@nb.njit((nb.i8[:, :], nb.i8[:]), cache=True)
def solve(uv: np.ndarray, p: np.ndarray) -> typing.NoReturn:
    n = 9
    g = csgraph_to_directed(uv)
    g, edge_idx, _ = sort_csgraph(n, g)
    s = (1 << n) - 1
    for i in p:
        s &= ~(1 << i)
    print(s)
    for i in range(n):
        if ~s >> i & 1: continue
        e0 = i
    print(e0)
    
    perm = np.arange(n - 1)
    while perm[0] != -1:
        e = e0
        fixed = np.zeros(n - 1, np.bool8)
        c = np.full(n, -1, np.int64) # c[i] is item placed on node i
        for i in range(n - 1): c[p[i]] = i
        for i in perm:
            ...
        next_permutation(perm)
    
    

def main() -> typing.NoReturn:
    m = int(input())
    I = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    )
    uv = I[:-8].reshape(m, 2) - 1
    p = I[-8:] - 1
    solve(uv, p)


main()