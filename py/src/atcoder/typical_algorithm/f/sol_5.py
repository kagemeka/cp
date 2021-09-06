import typing 
import sys 
import numpy as np 
import numba as nb



@nb.njit
def uf_build(
  n: int,
) -> np.ndarray:
  return np.full(n, -1, np.int64)


@nb.njit
def uf_find(
  uf: np.ndarray,
  u: int,
) -> int:
  if uf[u] < 0: return u
  uf[u] = uf_find(uf, uf[u])
  return uf[u]


@nb.njit
def uf_unite(
  uf: np.ndarray,
  u: int,
  v: int,
) -> typing.NoReturn:
  u = uf_find(uf, u)
  v = uf_find(uf, v)
  if u == v: return 
  if uf[u] > uf[v]: u, v = v, u
  uf[u] += uf[v]
  uf[v] = u


@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def mst_boruvka(
  n: int,
  csgraph: np.ndarray,
) -> np.ndarray:
  m = len(csgraph)
  assert csgraph.shape == (m, 3)
  inf = 1  << 60
  assert csgraph[:, 2].max() < inf
  edge_is_added = np.zeros(m, np.bool8)
  min_edge_idx = np.zeros(n, np.int64)
  uf = uf_build(n)
  root = np.arange(n)
    
  def update_all_roots():
    nonlocal uf, n, root
    for i in range(n):
      root[i] = uf_find(uf, i)

  def all_same():
    nonlocal root
    return np.all(root == root[0])

  def update_min_edge_indices():
    nonlocal min_edge_idx, m, csgraph, root
    min_edge_idx[:] = -1
    for i in range(m):
      u, v, w = csgraph[i]
      u, v = root[u], root[v]
      if u == v: continue
      j = min_edge_idx[u]
      if j == -1 or w < csgraph[j, 2]:
        min_edge_idx[u] = i
      j = min_edge_idx[v]
      if j == -1 or w < csgraph[j, 2]:
        min_edge_idx[v] = i

  def add_min_edges():
    nonlocal n, root, min_edge_idx, csgraph, uf
    for i in range(n):
      if i != root[i]: continue
      i = min_edge_idx[i]
      if edge_is_added[i]: continue
      u, v, _ = csgraph[i]
      uf_unite(uf, u, v)
      edge_is_added[i] = True

  while not all_same():
    update_min_edge_indices()
    add_min_edges()
    update_all_roots()

  added_edge_indices = np.flatnonzero(edge_is_added)
  assert added_edge_indices.size == n - 1
  return csgraph[added_edge_indices]
  


@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def solve(
  n: int,
  uvc: np.ndarray,
) -> typing.NoReturn:
  mst = mst_boruvka(n, uvc)
  print(mst[:, 2].sum())


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  uvc = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3)
  solve(n, uvc)


main()