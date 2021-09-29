import typing 


class Node(): ...



class Edge():
  def __init__(
    self,
    from_: int,
    to: int,
    weight: typing.Optional[int] = None,
    capacity: typing.Optional[int] = None,
  ) -> typing.NoReturn:
    self.from_ = from_
    self.to = to
    self.weight = weight 
    self.capacity = capacity




class Graph():
  def __init__(
    self,
    nodes: typing.List[Node],
    edges: typing.List[typing.List[Edge]],
  ) -> typing.NoReturn:
    self.nodes = nodes 
    self.edges = edges 


  @classmethod  
  def from_size(
    cls,
    n: int,
  ) -> typing.Any:
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


class ShortestDistBellmanFord():
  def __call__(
    self,
    g: Graph,
    src: int,
  ) -> typing.List[int]:
    n = g.size
    inf = float('inf')
    dist = [inf] * n
    dist[src] = 0
    for _ in range(n - 1):
      for u in range(n):
        for e in g.edges[u]:
          v, w = e.to, e.weight
          dist[v] = min(dist[v], dist[u] + w)
    for u in range(n):
      for e in g.edges[u]:
        v, w = e.to, e.weight 
        if dist[u] + e.weight >= dist[e.to]: continue
        raise Exception('Negative cycle found.')
    return dist
           

def solve(
  n: int,
  uvc: typing.Iterator[typing.Tuple[int]],
) -> typing.NoReturn:
  g = Graph.from_size(n)
  for u, v, c in uvc:
    g.add_edge(Edge(u, v, c))
  
  bellman_ford = ShortestDistBellmanFord()
  s = 0
  for i in range(n):
    s += sum(bellman_ford(g, i))
  print(s)

import sys 

def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  uvc = map(int, sys.stdin.read().split())
  uvc = zip(*[uvc] * 3)
  solve(n, uvc)


main()