from typing import List


import typing 
import sys



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


  def size(
    self,
    u: int,
  ) -> int:
    return -self.__a[self.find(u)]



class Solution:
  def latestDayToCross(
    self, 
    row: int, 
    col: int, 
    cells: List[List[int]]
  ) -> int:
    h, w = row, col 
    n = h * w
    uf = UnionFind(n + 2)
    
    dyx = (
      (-1, 0),
      (0, -1),
      (0, 1),
      (1, 0),
    )

    is_land = [[False] * w for _ in range(h)]

    def on_grid(y: int, x: int) -> bool:
      return 0 <= y < h and 0 <= x < w
 
    for i in range(n - 1, -1, -1):
      y, x = cells[i]
      y -= 1; x -= 1
      is_land[y][x] = True
      u = y * w + x + 1
      for dy, dx in dyx:
        ny = y + dy
        nx = x + dx 
        if not on_grid(ny, nx): continue
        if not is_land[ny][nx]: continue
        v = ny * w + nx + 1
        uf.unite(u, v)
      if y == 0: uf.unite(0, u)
      if y == h - 1: uf.unite(u, n + 1)
      if uf.find(0) != uf.find(n + 1): continue
      return i

        