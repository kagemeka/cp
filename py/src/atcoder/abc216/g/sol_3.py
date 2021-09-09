import typing 
import heapq 
import sys 
import numpy as np 
import numba as nb 



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
  idx = np.searchsorted(csgraph[:, 0], np.arange(n + 1)) 
  dist = np.full(n, inf, np.int64)
  dist[src] = 0
  hq = [(0, src)]
  while hq:
    du, u = heapq.heappop(hq)
    if du > dist[u]: continue
    for edge_idx in range(idx[u], idx[u + 1]):
      _, v, w = csgraph[edge_idx]
      dv = du + w
      if dv >= dist[v]: continue
      dist[v] = dv 
      heapq.heappush(hq, (dv, v))
  return dist
      


@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def solve(
  n: int,
  lrx: np.ndarray,
) -> typing.NoReturn:
  m = len(lrx)
  edges = np.zeros((2 * n + m, 3), np.int64)

  edge_idx = 0
  def add_edge(u, v, w):
    nonlocal edge_idx 
    edges[edge_idx] = (u, v, w)
    edge_idx += 1
  
  for i in range(n):
    add_edge(i, i + 1, 1)
    add_edge(i + 1, i, 0)
  
  for i in range(m):
    l, r, x = lrx[i]
    add_edge(l - 1, r, r - l + 1 - x) 
    
  sort_idx = np.argsort(
    edges[:, 0],
    kind='mergesort',
  )
  edges = edges[sort_idx]
  b = shortest_dist_dijkstra(n + 1, edges, 0)
  a = b[1:] - b[:-1] ^ 1
  return a 


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  lrx = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3)
  a = solve(n, lrx)
  print(*a)
  
main()