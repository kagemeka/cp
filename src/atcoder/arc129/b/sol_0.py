import typing 
# import bisect 
import numpy as np 
import numba as nb 
import sys



@nb.njit((nb.i8, nb.i8[:, :]), cache=True)
def solve(n: int, lr: np.ndarray) -> typing.NoReturn:
    l, r = lr[:, 0], lr[:, 1]

    def max_dist(x):
        dist = np.zeros(n, np.int64)
        dist[x < l] = l - x
        dist[r < x] = x - r
        return dist.min()


    def ternary_search():
        lo, hi = 0, 1 << 30
        while hi - lo > 1:
            x0 = (lo * 2 + hi) // 2
            x1 = (lo + hi * 2) // 3
            if max_dist(x0) <= max_dist(x1):
                hi = x1
            else:
                lo = x0
        return lo
    
    res = ternary_search()
    print(res)
    


def main() -> typing.NoReturn:
    n = int(input())
    lr = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(n, 2)
    solve(n, lr)