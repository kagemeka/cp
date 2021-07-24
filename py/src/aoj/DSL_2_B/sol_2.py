import typing
import sys



class FenwickTree():
  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn:
    self.__a = [0] * n
  

  def add(
    self,
    i: int,
    x: int,
  ) -> typing.NoReturn:
    a = self.__a
    n = len(a)
    while i < n:
      a[i] += x
      i |= i + 1


  def sum(
    self,
    i: int,
  ) -> int:
    s = 0 
    while i >= 0:
      s += self.__a[i]
      i &= i + 1
      i -= 1
    return s



def solve(
  n: int,
  q: typing.List[
    typing.Tuple[int],
  ],
) -> typing.NoReturn:
  fen = FenwickTree(n)
  for com, x, y in q:
    x -= 1
    if com == 0:
      fen.add(x, y)
    else:
      y -= 1
      s = fen.sum(y)
      s -= fen.sum(x - 1)
      print(s)


def main() -> typing.NoReturn:
  n, q = map(
    int, 
    input().split(),
  )
  q = [
    tuple(
      int(x)
      for x in (
        sys.stdin.readline()
        .split()
      )
    )
    for _ in range(q)
  ]
  solve(n, q)


main()