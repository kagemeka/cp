import typing
from typing import List
from heapq import (
  heappush,
  heappop,
)


mod = 10 ** 9 + 7


class Solution:
  def countPaths(
    self,
    n: int,
    roads: List[List[int]],
  ) -> int:

    g = [[] for _ in range(n)]

    for u, v, t in roads:
      g[u].append((v, t))
      g[v].append((u, t))


    inf = 1 << 60
    dist = [inf] * n
    dist[0] = 0
    paths = [0] * n
    paths[0] = 1

    q = [(0, 0)]
    while q:
      du, u = heappop(q)
      if du > dist[u]: continue
      for v, d in g[u]:
        dv = du + d
        if dv > dist[v]: continue
        if dv == dist[v]:
          paths[v] += paths[u]
          paths[v] %= mod
          continue
        dist[v] = dv
        paths[v] = paths[u]
        heappush(q, (dv, v))
    return paths[-1]
