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


  def groups(
    self,
  ) -> typing.List[typing.List[int]]:
    n = len(self.__a)
    groups = [[] for _ in range(n)]
    for i in range(n):
      groups[self.find(i)].append(i)
    return [g for g in groups if g]



class SieveOfEratosthenes():
  def __call__(
    self,
    n: int = 1 << 20,
  ) -> typing.List[int]:
    assert n > 1
    s = self.gpf(n)
    for i in range(n):
      s[i] = s[i] == i
    return s


  def gpf(
    self,
    n: int = 1 << 20,
  ) -> typing.List[int]:
    assert n > 1
    s = list(range(n))
    s[0] = s[1] = -1
    i = 0
    while i * i < n - 1:
      i += 1
      if s[i] != i: continue
      for j in range(i, n, i):
        s[j] = i
    return s


  def lpf(
    self,
    n: int = 1 << 20,
  ) -> typing.List[int]:
    assert n > 1
    s = list(range(n))
    s[0] = s[1] = -1
    i = 0
    while i * i < n - 1:
      i += 1
      if s[i] != i: continue
      for j in range(i, n, i):
        if s[j] == j: s[j] = i
    return s


import collections

class PrimeFactorize():
  def __call__(
    self,
    n: int,
  ) -> typing.DefaultDict[int, int]:
    f = collections.defaultdict(int)
    while n > 1:
      p = self.__lpf[n]
      n //= p
      f[p] += 1
    return f


  def __init__(
    self,
    n: int = 1 << 20,
  ) -> typing.NoReturn:
    self.__lpf = SieveOfEratosthenes().lpf(n)


  def factorial(
    self,
    n: int,
  ) -> typing.List[int]:
    f = collections.defaultdict(int)
    for i in range(n + 1):
      for p, c in self(i).items():
        f[p] += c
    return f



class Solution:
  def gcdSort(
    self,
    a: typing.List[int],
  ) -> bool:
    n = len(a)
    uf = UnionFind(1 << 17)
    factorize = PrimeFactorize(1 << 17)
    for x in a:
      for p in factorize(x):
        uf.unite(p, x)
    b = sorted(a)
    for i in range(n):
      if uf.find(a[i]) == uf.find(b[i]): continue
      return False
    return True
