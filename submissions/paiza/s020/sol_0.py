import typing 
import sys 
import numpy as np 
import pprint 

def solve(a: typing.List[int], wc: np.ndarray) -> typing.NoReturn:
    n, m = len(a), len(wc)
    w, c = wc.T 
    w = w.tolist()
    c = c.tolist()
    
    inf = 1 << 30
    l = 101
    dp = [[0] * l for _ in range(m)]
    for x in a:
        ndp = [[inf] * l for _ in range(m)]
        mn = [min(dp[j][0], min(dp[j][1:]) + c[j]) for j in range(m)]
        for i in range(m):
            if x > w[i]: continue
            for j in range(m):
                ndp[i][x] = min(ndp[i][x], mn[j])
            for j in range(1, w[i] - x + 1):
                ndp[i][j + x] = min(ndp[i][j + x], dp[i][j])
                
        dp = ndp 
    mn = [min(dp[j][0], min(dp[j][1:]) + c[j]) for j in range(m)]
    print(min(mn)) 


def main() -> typing.NoReturn:
    n = int(input())
    a = [int(input()) for _ in range(n)]
    m = int(input())
    wc = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(m, 2)
    solve(a, wc)


main()
    