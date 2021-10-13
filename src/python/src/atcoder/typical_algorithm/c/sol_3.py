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


class TSP():
  def __call__(
    self,
    g: Graph,
    src: int,
  ) -> int:
    g = self.__graph_to_matrix(g)
    return self.from_matrix(g, src)
  

  def __graph_to_matrix(
    self,
    g: Graph
  ) -> typing.List[typing.List[int]]:
    n = g.size
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
      for e in g.edges[i]:
        dist[i][e.to] = e.weight
    return dist

  
  def from_matrix(
    self,
    g: typing.List[typing.List[int]],
    src: int,
  ) -> int:
    n = len(g)
    assert len(g[0]) == n
    inf = 1 << 60
    assert inf > sum(map(sum, g))
    dist = [[inf] * n for _ in range(1 << n)]
    dist[1 << src][src] = 0 
    for s in range(1 << n):
      for i in range(n):
        if ~s >> i & 1: continue
        for j in range(n):
          if s >> j & 1: continue
          u = s | 1 << j 
          dist[u][j] = min(
            dist[u][j], 
            dist[s][i] + g[i][j],
          )
    return min(
      dist[-1][i] + g[i][src] 
      for i in range(n)
    )



def solve(
  a: typing.List[typing.List[int]],
) -> typing.NoReturn:
  n = len(a)
  g = Graph.from_size(n)
  for i in range(n):
    for j in range(n):
      g.add_edge(Edge(i, j, a[i][j]))
  print(TSP()(g, 0))


def main() -> typing.NoReturn:
  n = int(input())
  a = [
    list(map(int, input().split()))
    for _ in range(n)
  ]
  solve(a)


main()


