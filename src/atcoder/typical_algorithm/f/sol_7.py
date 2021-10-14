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


class UnionFind():
  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn: 
    self.__a = [-1] * n
 

  def find(
    self, 
    u: int,
  ) -> int:
    a = self.__a
    if a[u] < 0: return u
    a[u] = self.find(a[u])
    return a[u]


  def same(
    self,
    u: int,
    v: int,
  ) -> bool:
    return self.find(u) == self.find(v)


  def unite(
    self,
    u: int,
    v: int,
  ) -> typing.NoReturn:
    u = self.find(u)
    v = self.find(v)
    if u == v: return
    a = self.__a 
    if a[u] > a[v]: u, v = v, u
    a[u] += a[v]
    a[v] = u



class MSTKruskal():
  def __call__(
    self,
    g: Graph,
  ) -> Graph:
    n = g.size 
    new_g = Graph.from_size(n)
    edges = [
      (e.weight, u, e.to)
      for u in range(n)
      for e in g.edges[u]
    ]
    edges.sort()
    uf = UnionFind(n)
    for w, u, v in edges:
      if uf.same(u, v): continue
      new_g.add_edge(Edge(u, v, w))
      uf.unite(u, v)    
    return new_g 


def solve(
  n: int,
  uvc: typing.Iterator[typing.Tuple[int]],
) -> typing.NoReturn:
  g = Graph.from_size(n)
  for u, v, c in uvc:
    g.add_edge(Edge(u, v, c))
    g.add_edge(Edge(v, u, c))
  mst = MSTKruskal()(g)
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