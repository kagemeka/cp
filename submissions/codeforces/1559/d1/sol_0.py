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


  def same(
    self,
    u: int,
    v: int,
  ) -> bool:
    return self.find(u) == self.find(v)


def solve(
  n: int,
  uv1: typing.List[typing.Iterator[int]],
  uv2: typing.List[typing.Iterator[int]],
) -> typing.NoReturn:
  uf1 = UnionFind(n)
  uf2 = UnionFind(n)
  for u, v in uv1:
    uf1.unite(u, v)
  for u, v in uv2:
    uf2.unite(u, v)


  res = []
  for i in range(n - 1):
    for j in range(i + 1, n):
      if uf1.same(i, j) or uf2.same(i, j):
        continue
      uf1.unite(i, j)
      uf2.unite(i, j)
      res.append((i + 1, j + 1))
  print(len(res))
  for x in res:
    print(*x)



def main() -> typing.NoReturn:
  n, m1, m2 = map(int, input().split())
  uv1 = [
    map(lambda x: int(x) - 1, input().split())
    for _ in range(m1)
  ]
  uv2 = [
    map(lambda x: int(x) - 1, input().split())
    for _ in range(m2)
  ]
  solve(n, uv1, uv2)


main()
