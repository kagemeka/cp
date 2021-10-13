import typing 
import sys 
import numpy as np
import numba as nb 



@nb.njit(
  (nb.i8, nb.i8[:, :], nb.i8),
  cache=True,
) 
def tsp(
  n: int,
  g: np.ndarray,
  src: int,
) -> int:
  m = len(g)
  assert g.shape == (m, 3)
  inf = 1 << 60
  assert inf > g[:, 2].sum()
  sort_idx = np.argsort(g[:, 0], kind='mergesort')
  g = g[sort_idx]
  idx = np.searchsorted(g[:, 0], np.arange(n + 1))
  dist = np.full((1 << n, n), inf, np.int64)
  dist[1 << src, src] = 0 
  for s in range(1 << n):
    for i in range(n):
      if ~s >> i & 1: continue
      for k in range(idx[i], idx[i + 1]):
        _, j, w = g[k]        
        if s >> j & 1: continue
        u = s | 1 << j 
        dist[u, j] = min(dist[u, j], dist[s, i] + w)
  mn = inf 
  for i in range(n):
    if i == src: continue
    for k in range(idx[i], idx[i + 1]):
      _, j, w = g[k]
      if j != src: continue
      mn = min(mn, dist[-1, i] + w)
  return mn
      
      

@nb.njit(
  (nb.i8[:, :], nb.b1),
  cache=True,
)
def csgraph_from_dense(
  g: np.ndarray,
  zero_is_null: bool=True,
) -> np.ndarray:
  n = len(g)
  assert g.shape == (n, n)
  exist_edge = np.full_like(g, 1, np.bool8)
  if zero_is_null:
    exist_edge &= g != 0
  m = exist_edge.sum()
  csgraph = np.zeros((m, 3), np.int64)
  k = 0  
  def add_edge(u, v, w):
    nonlocal csgraph, k 
    csgraph[k] = (u, v, w)
    k += 1
  for i in range(n):
    for j in range(n):
      if not exist_edge[i, j]: continue
      add_edge(i, j, g[i, j])
  return csgraph


@nb.njit(
  (nb.i8[:, :], ),
  cache=True,
) 
def solve(
  a: np.ndarray,
) -> typing.NoReturn:
  n = len(a)
  csgraph = csgraph_from_dense(a, zero_is_null=False)
  print(tsp(n, csgraph, 0))


def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, n)
  solve(a)


main()