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
    

class ShortestDistDesopoPape():
  def __call__(
    self,
    g: Graph,
    src: int,
  ) -> typing.List[int]:
    import collections 
    inf = float('inf')
    n = g.size 
    dist = [inf] * n
    dist[src] = 0
    dq = collections.deque([src])
    state = [-1] * n
    while dq:
      u = dq.popleft()
      state[u] = 0
      for e in g.edges[u]:
        v, dv = e.to, dist[u] + e.weight 
        if dv >= dist[v]: continue
        dist[v] = dv
        if state[v] == 1: continue 
        if state[v] == -1: dq.append(v)
        else: dq.appendleft(v)
        state[v] = 1
    return dist



def solve(
  n: int,
  uvc: typing.Iterator[typing.Tuple[int]],
) -> typing.NoReturn:
  g = Graph.from_size(n)
  for u, v, c in uvc:
    g.add_edge(Edge(u, v, c))
  s = 0
  desopo_pape = ShortestDistDesopoPape()
  for i in range(n):
    s += sum(desopo_pape(g, i))
  print(s)

import sys 

def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  uvc = map(int, sys.stdin.read().split())
  uvc = zip(*[uvc] * 3)
  solve(n, uvc)


main()