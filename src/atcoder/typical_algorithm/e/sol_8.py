import typing 
import sys 
import numpy as np
import numba as nb 
import heapq 


@nb.njit(
  (nb.i8, nb.i8[:, :], nb.i8),
  cache=True,
)
def shotest_dist_bellman_ford(
  n: int,
  csgraph: np.ndarray,
  src: int,
) -> np.ndarray:
  m = len(csgraph)
  assert csgraph.shape == (m, 3)
  inf = 1 << 60
  assert inf > csgraph[:, 2].max() * n
  dist = np.full(n, inf, np.int64)
  dist[src] = 0
  for _ in range(n - 1):
    for i in range(m):
      u, v, w = csgraph[i]
      dist[v] = min(dist[v], dist[u] + w)
  for i in range(m):
    u, v, w = csgraph[i]
    if dist[u] + w < dist[v]: 
      raise Exception('Negative cycle found.')
  return dist


@nb.njit(
  (nb.i8, nb.i8[:, :], nb.i8),
  cache=True,
) 
def shortest_dist_dijkstra(
  n: int,
  csgraph: np.ndarray,
  src: int,
) -> np.ndarray:
  assert csgraph.shape == (len(csgraph), 3)
  inf = 1 << 60
  assert inf > csgraph[:, 2].max() * n
  sort_idx = np.argsort(csgraph[:, 0], kind='mergesort')
  csgraph = csgraph[sort_idx]
  edge_idx = np.searchsorted(csgraph[:, 0], np.arange(n + 1))
  dist = np.full(n, inf, np.int64)
  dist[src] = 0
  hq = [(0, src)]
  while hq:
    du, u = heapq.heappop(hq)
    if du > dist[u]: continue
    for i in range(edge_idx[u], edge_idx[u + 1]):
      _, v, w = csgraph[i]
      dv = du + w 
      if dv >= dist[v]: continue
      dist[v] = dv
      heapq.heappush(hq, (dv, v))
  return dist


@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def shotest_dist_johnson(
  n: int,
  csgraph: np.ndarray,
) -> np.ndarray:
  m = len(csgraph)
  assert csgraph.shape == (m, 3)
  new_edges = np.zeros((n, 3), np.int64)
  new_edges[:, 0] = n
  new_edges[:, 1] = np.arange(n)
  csgraph = np.vstack((csgraph, new_edges))
  h = shotest_dist_bellman_ford(n + 1, csgraph, n)[:-1]
  csgraph = csgraph[:m]
  csgraph[:, 2] += h[csgraph[:, 0]] - h[csgraph[:, 1]]
  dist = np.zeros((n, n), np.int64)
  for i in range(n):
    d = shortest_dist_dijkstra(n, csgraph, i)
    dist[i] = d - h[i] + h  
  return dist
      

@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def solve(
  n: int,
  uvc: np.ndarray,
) -> typing.NoReturn:
  s = shotest_dist_johnson(n, uvc).sum()
  print(s)


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  uvc = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3)
  solve(n, uvc)


main()