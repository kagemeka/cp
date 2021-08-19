import typing



class SADoubling():
  def __call__(
    self,
    a: typing.List[int],
  ) -> typing.List[int]:
    self.__a = a
    self.__compress()
    print(self.__a)
    n = len(self.__a)
    self.__cnt = [0] * (n + 1)
    self.__n = n
    self.__doubling()
    return self.__sa


  def __compress(
    self,
  ) -> typing.NoReturn:
    from bisect import bisect_left
    a = self.__a
    v = sorted(set(a))
    self.__a = [bisect_left(v, x) for x in a]
    
  
  def __count_sort(
    self,
    a: typing.List[int],
  ) -> typing.List[int]:
    c, n = self.__cnt, self.__n 
    assert len(a) == n
    for x in a: c[x + 1] += 1
    for i in range(n): c[i + 1] += c[i]
    idx = [0] * n
    for i in range(n):
      x = a[i]
      print(c[x])
      idx[c[x]] = i
      c[x] += 1
    for i in range(n + 1): c[i] = 0
    return idx
  

  def __doubling(
    self,
  ) -> typing.NoReturn:
    rank, n = self.__a, self.__n 
    k = 1
    while k < n:
      b = [0] * n
      for i in range(n - k): 
        b[i] = rank[i + k] + 1
      ord_b = self.__count_sort(b)
      a = [rank[i] for i in ord_b]
      ord_a = self.__count_sort(a)
      sa = [ord_b[i] for i in ord_a]
      c = [
        a[ord_a[i]] << 30 | b[sa[i]] 
        for i in range(n)
      ]
      rank = [0] * n
      for i in range(n - 1):
        rank[sa[i + 1]] = rank[sa[i]] + (c[i + 1] > c[i])
      k *= 2
    self.__sa = sa 
 



def solve(
  n: int,
  s: str,
) -> typing.NoReturn:
  s = [ord(x) for x in s]
  sa = SADoubling()(s)
  print(sa)



def main() -> typing.NoReturn:
  n = int(input())
  s = input()
  solve(n, s)


main()