import typing 
import sys 
import numpy as np 
import numba as nb 


@nb.njit 
def csgraph_to_undirected(g: np.ndarray) -> np.ndarray:
  m = len(g)
  g = np.vstack((g, g))
  g[m:, :2] = g[m:, 1::-1]
  return g


@nb.njit
def sort_csgraph(
  n: int, 
  g: np.ndarray,
) -> typing.Tuple[np.ndarray, np.ndarray, np.ndarray]:
  sort_idx = np.argsort(g[:, 0], kind='mergesort')
  g = g[sort_idx]
  edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
  original_idx = np.arange(len(g))[sort_idx]
  return g, edge_idx, original_idx



@nb.njit
def euler_tour(
  g: np.ndarray,
  edge_idx: np.ndarray,
  root: int,
) -> typing.Tuple[np.ndarray, np.ndarray, np.ndarray]:
  n = g[:, :2].max() + 1
  parent = np.full(n, -1, np.int32)
  depth = np.zeros(n, np.int32)
  tour = np.empty(n * 2, np.int32)
  st = [root]
  for i in range(2 * n):
    u = st.pop()
    tour[i] = u
    if u < 0: continue
    st.append(-u - 1)
    for v in g[edge_idx[u]:edge_idx[u + 1], 1][::-1]:
      if v == parent[u]: continue
      parent[v] = u
      depth[v] = depth[u] + 1
      st.append(v)
  return tour, parent, depth
  


@nb.njit((nb.i8[:, :], ), cache=True)
def solve(ab: np.ndarray) -> typing.NoReturn:
  n = len(ab) + 1
  g = csgraph_to_undirected(ab)
  g, edge_idx, _ = sort_csgraph(n, g)
  _, _, depth = euler_tour(g, edge_idx, 0)
  flg = np.count_nonzero(depth & 1) >= n // 2
  res = np.flatnonzero(depth & 1 ^ ~flg) + 1
  return res[:n // 2]



def main() -> typing.NoReturn:
  n = int(input())
  ab = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n - 1, 2) - 1
  res = solve(ab)
  print(*res)


main()