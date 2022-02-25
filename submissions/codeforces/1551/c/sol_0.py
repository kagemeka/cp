import typing
import sys
from collections import (
  Counter,
)


def solve(
  n: int,
  a: typing.List[str],
) -> typing.NoReturn:
  l = [len(s) for s in a]
  a = [Counter(s) for s in a]


  def calc_max(
    letter: str,
  ) -> int:
    b = [
      a[i][letter] * 2 - l[i]
      for i in range(n)
    ]
    b.sort(reverse=1)
    s = 0
    for i in range(n):
      s += b[i]
      if s <= 0: return i
    return n

  mx = max(
    calc_max(letter)
    for letter in 'abcde'
  )
  print(mx)


def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    n = int(input())
    a = [
      sys.stdin.readline()
      .rstrip()
      for _ in range(n)
    ]
    solve(n, a)
    print()


main()
