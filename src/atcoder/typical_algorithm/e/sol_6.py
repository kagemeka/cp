import typing 
import sys 
import numpy as np
import numba as nb 



@nb.njit(
  (nb.i8[:, :], ),
  cache=True,
)
def shortest_dist_floyd_warshall(
  g: np.ndarray,
) -> np.ndarray:
  n = len(g)
  assert g.shape == (n, n)
  dist = g.copy()
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
  (nb.i8[:, :], nb.i8),
  cache=True,
)
def csgraph_to_dense(
  csgraph: np.ndarray,
  n: int,
) -> np.ndarray:
  m = len(csgraph)
  assert csgraph.shape == (m, 3)
  inf = 1 << 60
  g = np.full((n, n), inf, np.int64)
  for i in range(m):
    u, v, w = csgraph[i]
    g[u, v] = min(g[u, v], w)
  return g 


@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def solve(
  n: int,
  uvc: np.ndarray,
) -> typing.NoReturn:
  g = csgraph_to_dense(uvc, n)
  s = shortest_dist_floyd_warshall(g).sum()
  print(s)


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  uvc = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3)
  solve(n, uvc)


main()