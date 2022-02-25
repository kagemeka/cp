import typing
import sys
import numpy as np
import heapq



def solve(bp: np.ndarray, c: int, k: int) -> typing.NoReturn:
    n = len(bp)
    b, p = bp.T
    sort_idx = np.argsort(b)
    b, p = b[sort_idx].tolist(), p[sort_idx].tolist()
    hq = []
    s = 0
    for i in range(n - 1, -1, -1):
        s += p[i]
        heapq.heappush(hq, -p[i])
        if len(hq) < k: continue
        if len(hq) > k:
            s += heapq.heappop(hq)
        if s > c: continue
        print(b[i])
        return



def main() -> typing.NoReturn:
    n, c, k = map(int, input().split())
    bp = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(n, 2)
    solve(bp, c, k)


main()
