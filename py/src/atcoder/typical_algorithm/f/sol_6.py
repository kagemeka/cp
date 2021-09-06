import typing 
import sys 
import numpy as np 
import numba as nb



@nb.njit(
  (nb.i8[:, :], ),
  cache=True,
)
def csgraph_to_undirected(
  csgraph: np.ndarray,
) -> np.ndarray:
  m = len(csgraph)
  assert csgraph.shape == (m, 3)
  csgraph = np.vstack((csgraph, csgraph))
  csgraph[m:, :2] = csgraph[m:, 1::-1]
  return csgraph 



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
  csgraph = csgraph_to_undirected(csgraph)
  m *= 2
  sort_idx = np.argsort(csgraph[:, 0], kind='mergesort')
  csgraph = csgraph[sort_idx]
  
  is_used = np.zeros(m, np.bool8)
  
  def label_nodes():
    label = np.full(n, -1, np.int64)
    
    ...
  

  mst = np.zeros((n - 1, 3), np.int64)
  mst_idx = 0
  def add_edge(u, v, w):
    nonlocal mst, mst_idx
    mst[mst_idx] = (u, v, w)
    mst_idx += 1
  
  min_edge = np.zeros((n, 3), np.int64)

  while not all_same():
    min_edge[:, 2] = inf
    for i in range(m):
      u, v, w = csgraph[i]
      if root[u] == root[v]: continue
      if w < min_edge[root[u], 2]:
        min_edge[root[u]] = (u, v, w)
      if w < min_edge[root[v], 2]:
        min_edge[root[v]] = (v, u, w)
    for i in range(n):
      if i != root[i]: continue
      u, v, w = min_edge[i]
      if uf_find(uf, u) == uf_find(uf, v): continue
      uf_unite(uf, u, v)
      add_edge(u, v, w)
    update_all_root()
  return mst
  


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