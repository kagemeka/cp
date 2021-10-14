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



class MSTBoruvka():
  def __call__(
    self,
    g: Graph,
  ) -> Graph:
    n = g.size 
    self.__new_g = Graph.from_size(n)
    self.__uf = UnionFind(n)
    self.__root = list(range(n))
    self.__n = n
    edges = [
      (u, e.to, e.weight)
      for u in range(n) 
      for e in g.edges[u]
    ]
    self.__edge_is_added = [False] * len(edges)
    self.__edges = edges
    while not self.__all_same():
      self.__update_min_edge_indices()
      self.__add_min_edges()
      self.__update_all_roots()
    return self.__new_g
  

  def __add_min_edges(
    self,
  ) -> typing.NoReturn:
    edge_is_added = self.__edge_is_added
    for i in range(self.__n):
      if i != self.__root[i]: continue
      i = self.__min_edge_idx[i]
      if edge_is_added[i]: continue
      u, v, w = self.__edges[i]
      self.__uf.unite(u, v)
      self.__new_g.add_edge(Edge(u, v, w))
      edge_is_added[i] = True


  def __all_same(self) -> bool:
    n, root = self.__n, self.__root 
    return all(
      root[i] == root[i + 1] 
      for i in range(n - 1)
    )
  
  def __update_all_roots(
    self,
  ) -> typing.NoReturn:
    for i in range(self.__n):
      self.__root[i] = self.__uf.find(i)


  def __update_min_edge_indices(
    self,
  ) -> typing.NoReturn:
    root, edges = self.__root, self.__edges
    min_edge_idx = [-1] * self.__n
    for i, (u, v, w) in enumerate(edges):
      u, v = root[u], root[v]
      if u == v: continue
      j = min_edge_idx[u]
      if j == -1 or w < edges[j][2]:
        min_edge_idx[u] = i
      j = min_edge_idx[v]
      if j == -1 or w < edges[j][2]:
        min_edge_idx[v] = i
    self.__min_edge_idx = min_edge_idx
  

def solve(
  n: int,
  uvc: typing.Iterator[typing.Tuple[int]],
) -> typing.NoReturn:
  g = Graph.from_size(n)
  for u, v, c in uvc:
    g.add_edge(Edge(u, v, c))
    g.add_edge(Edge(v, u, c))
  mst = MSTBoruvka()(g)
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