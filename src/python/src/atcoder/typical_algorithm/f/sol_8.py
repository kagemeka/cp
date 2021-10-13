from __future__ import annotations
import typing 
import dataclasses


@dataclasses.dataclass
class Node(): ...



@dataclasses.dataclass 
class Edge():
  from_: int
  to: int
  weight: typing.Optional[int] = None,
  capacity: typing.Optional[int] = None



@dataclasses.dataclass 
class Graph():
  nodes: typing.List[Node]
  edges: typing.List[typing.List[Edge]]

  @classmethod  
  def from_size(
    cls,
    n: int,
  ) -> Graph:
    nodes = [Node() for _ in range(n)]
    edges = [[] for _ in range(n)]
    return cls(nodes, edges)


  def add_edge(
    self,
    e: Edge,
  ) -> typing.NoReturn:
    self.edges[e.from_].append(e)
    

  def add_edges(
    self,
    edges: typing.List[Edge],
  ) -> typing.NoReturn:
    for e in edges:
      self.add_edge(e)
  

  @property
  def size(self) -> int:
    return len(self.nodes)
    

import typing 


class MSTPrim():
  def __call__(
    self,
    g: Graph,
  ) -> Graph:
    import heapq
    n = g.size 
    new_g = Graph.from_size(n)
    visited = [False] * n
    inf = 1 << 60
    weight = [inf] * n
    hq = [(0, -1, 0)]
    while hq:
      wu, pre, u = heapq.heappop(hq)
      if visited[u]: continue
      visited[u] = True
      if pre != -1:
        new_g.add_edge(Edge(pre, u, wu))
      for e in g.edges[u]:
        v, wv = e.to, e.weight
        if visited[v] or wv >= weight[v]: continue
        weight[v] = wv 
        heapq.heappush(hq, (wv, u, v))
    return new_g 



def solve(
  n: int,
  uvc: typing.Iterator[typing.Tuple[int]],
) -> typing.NoReturn:
  g = Graph.from_size(n)
  for u, v, c in uvc:
    g.add_edge(Edge(u, v, c))
    g.add_edge(Edge(v, u, c))
  mst = MSTPrim()(g)
  s = sum(
    e.weight
    for u in range(n)
    for e in mst.edges[u]
  )
  print(s)
  

import sys 

def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  uvc = map(int, sys.stdin.read().split())
  uvc = zip(*[uvc] * 3)
  solve(n, uvc)


main()