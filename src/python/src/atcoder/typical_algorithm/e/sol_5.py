import typing 
import sys 
import numpy as np
import numba as nb 
import heapq



@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def shortest_dist_floyd_warshall(
  n: int,
  g: np.ndarray,
) -> np.ndarray:
  m = len(g)
  assert g.shape == (m, 3)
  inf = 1 << 60
  assert inf > g[:, 2].max() * n
  dist = np.full((n, n), inf, np.int64)
  for i in range(m):
    u, v, w = g[i]
    dist[u, v] = min(dist[u, v], w)
  for i in range(n): dist[i, i] = 0
  for k in range(n):
    for i in range(n):
      for j in range(n):
        dist[i, j] = min(
          dist[i, j],
          dist[i, k] + dist[k, j],
        )
  return dist 


@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def solve(
  n: int,
  uvc: np.ndarray,
) -> typing.NoReturn:
  s = shortest_dist_floyd_warshall(n, uvc).sum()
  print(s)


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  uvc = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3)
  solve(n, uvc)


main()