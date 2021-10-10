import typing 
import sys 
import numpy as np 
import numba as nb 




@nb.njit
def euler_tour_edge(
  g: np.ndarray,
  edge_idx: np.ndarray,
  root: int,
) -> typing.Tuple[(np.ndarray, ) * 3]:
  n = g[:, :2].max() + 1
  parent = np.full(n, -1, np.int64)
  depth = np.zeros(n, np.int64)
  tour = np.empty(n << 1, np.int64)
  st = [root]
  for i in range(n << 1):
    u = st.pop()
    tour[i] = u
    if u < 0: continue
    st.append(~u)
    for v in g[edge_idx[u]:edge_idx[u + 1], 1][::-1]:
      if v == parent[u]: continue
      parent[v] = u
      depth[v] = depth[u] + 1
      st.append(v)
  return tour, parent, depth

@nb.njit 
def sort_csgraph(
  n: int, 
  g: np.ndarray,
) -> typing.Tuple[(np.ndarray, ) * 3]:
  idx = g[:, 0] << 31 | g[:, 1]
  sort_idx = np.argsort(idx, kind='mergesort')
  g = g[sort_idx]
  original_idx = np.arange(len(g))[sort_idx]
  edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
  return g, edge_idx, original_idx


@nb.njit 
def csgraph_to_directed(g: np.ndarray) -> np.ndarray:
  m = len(g)
  g = np.vstack((g, g))
  g[m:, :2] = g[m:, 1::-1]
  return g 


@nb.njit((nb.i8[:, :], nb.i8[:]), cache=True)
def solve(abc: np.ndarray, d: np.ndarray) -> typing.NoReturn:
  n = len(d)
  vertex_point_sum = d.sum()
  g = csgraph_to_directed(abc)
  g, edge_idx, _ = sort_csgraph(n, g)
  
  tour, parent, depth = euler_tour_edge(g, edge_idx, 0)


  edge_cost = np.zeros(n, np.int64)
  for i in range(len(g)):
    u, v, c = g[i]
    if u != parent[v]: continue
    edge_cost[v] = c


  dp = np.zeros(n, np.int64)

  # for root 
  size = np.ones(n, np.int64)
  for u in tour:
    if u >= 0: continue
    u = ~u
    p = parent[u]
    if p == -1: continue
    size[p] += size[u]
    dp[0] += size[u] * edge_cost[u]
  # dp[0] += vertex_point_sum - d[0]
  for u in tour:
    if u < 0: continue
    p = parent[u]
    dp[u] = dp[p] + edge_cost[u] * (n - 2 * size[u])
  dp += vertex_point_sum - d 
  print(dp)
    


def main() -> typing.NoReturn:
  n = int(input())
  I = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  abc = I[:-n].reshape(n - 1, 3)
  abc[:, :2] -= 1
  d = I[-n:]
  solve(abc, d)


main()
  