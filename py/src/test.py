from __future__ import annotations 
import typing 



class FenwickTree():
  @classmethod 
  def from_array(
    cls,
    a: typing.List[int],
  ) -> FenwickTree:
    n = len(a)
    a = a.copy()
    assert a[0] == 0
    for i in range(n):
      j = i + (i & -i)
      if j < n: a[j] += a[i]
    fw = cls(n)
    fw._FenwickTree__a = a
    return fw


  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn:
    self.__a = [0] * (n + 1)
  

  def __setitem__(
    self,
    i: int,
    x: int,
  ) -> typing.NoReturn:
    a = self.__a
    while i < len(a):
      a[i] += x
      i += i & -i
  

  def __getitem__(
    self,
    i: int,
  ) -> int:
    v = 0 
    while i > 0:
      v += self.__a[i]
      i -= i & -i
    return v


  def get_range(
    self,
    l: int,
    r: int,
  ) -> int:
    return -self(l - 1) + self(r)



  # if monotonic increasing.
  # different per problem
  def lower_bound(
    self,
    x: int
  ) -> int:
    a = self.__a
    n = len(a)
    l = 1
    while l << 1 < n: l <<= 1
    v = 0 
    i = 0 
    while l:
      if i + l < n and v + a[i + l] < x:
        i += l
        v += a[i]
      l >>= 1
    return i + 1


class RangeAddRangeSum():
  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn:
    self.__fw0 = FenwickTree(n)
    self.__fw1 = FenwickTree(n)


  def __setitem__(
    self,
    lr: typing.Tuple[int, int],
    x: int,
  ) -> typing.NoReturn:
    l, r = lr 
    self.__fw0[l] = -x * (l - 1)
    self.__fw0[r + 1] = x * r 
    self.__fw1[l] = x 
    self.__fw1[r + 1] = -x 
  

  def __getitem__(
    self,
    i: int,
  ) -> int:
    return self.__fw0[i] + self.__fw1[i] * i
  

  def get_range(
    self,
    l: int,
    r: int,
  ) -> int:
    return -self[l - 1] + self[r]

  

def test():
  n = 10
  rars = RangeAddRangeSum(n)
  rars[1, 15] = 2
  rars[3, 10] = 3
  print(rars.get_range(0, 11))


if __name__ == '__main__':
  test()