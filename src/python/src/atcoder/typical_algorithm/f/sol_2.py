import typing 
import sys 
import numpy as np 
import numba as nb
import heapq




@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def mst_prim_sparse(
  n: int,
  csgraph: np.ndarray,
) -> np.ndarray:
  m = len(csgraph)
  assert csgraph.shape == (m, 3)
  inf = 1 << 60
  assert np.all(csgraph[:, 2] < inf) 
  csgraph = csgraph_to_undirected(csgraph)
  m *= 2
  sort_idx = np.argsort(csgraph[:, 0], kind='mergesort')
  csgraph = csgraph[sort_idx]
  edge_idx = np.searchsorted(csgraph[:, 0], np.arange(n + 1))

  mst = np.zeros((m + 1, 3), np.int64)
  mst_idx = -1
  def add_edge(u, v, w):
    nonlocal mst, mst_idx 
    mst[mst_idx] = (u, v, w)
    mst_idx += 1

  hq = [(0, -1, 0)]
  weight = np.full(n, inf, np.int64)
  weight[0] = 0
  visited = np.zeros_like(weight, np.bool8)
  while hq:
    wu, pre, u = heapq.heappop(hq)
    if visited[u]: continue
    visited[u] = True
    add_edge(pre, u, wu)
    for i in range(edge_idx[u], edge_idx[u + 1]):
      _, v, wv = csgraph[i]
      if wv >= weight[v] or visited[v]: continue
      weight[v] = wv 
      heapq.heappush(hq, (wv, u, v))
  mst = mst[:mst_idx]
  assert weight.sum() == mst[:, 2].sum()
  return mst 
      


@nb.njit(
  (nb.i8[:, :], ),
  cache=True,
)
def csgraph_to_undirected(
  g: np.ndarray,
) -> np.ndarray:
  n = len(g)
  assert g.shape == (n, 3)
  g = np.vstack((g, g))
  g[n:, :2] = g[n:, 1::-1]
  return g  


@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def solve(
  n: int,
  uvc: np.ndarray,
) -> typing.NoReturn:
  mst = mst_prim_sparse(n, uvc)
  print(mst[:, 2].sum())


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  uvc = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3)
  solve(n, uvc)


main()