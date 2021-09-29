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
    


class ShortestDistDijkstra():
  def __call__(
    self,
    g: Graph,
    src: int,
  ) -> typing.List[int]:
    import heapq 
    inf = float('inf')
    dist = [inf] * g.size
    dist[src] = 0
    hq = [(0, src)]
    while hq:
      du, u = heapq.heappop(hq)
      if du > dist[u]: continue
      for e in g.edges[u]:
        v, dv = e.to, du + e.weight
        if dv >= dist[v]: continue
        dist[v] = dv 
        heapq.heappush(hq, (dv, v))
    return dist




def solve(
  n: int,
  uvc: typing.Iterator[typing.Tuple[int]],
) -> typing.NoReturN:
  g = Graph.from_size(n)
  for u, v, c in uvc:
    g.add_edge(Edge(u, v, c))
  
  dijkstra = ShortestDistDijkstra()
  s = 0
  for i in range(n):
    s += sum(dijkstra(g, i))
  print(s)

import sys 

def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  uvc = map(int, sys.stdin.read().split())
  uvc = zip(*[uvc] * 3)
  solve(n, uvc)


main()