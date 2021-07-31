import typing 
from collections import (
  Counter,
)


def solve(
  a: typing.List[int],
) -> typing.NoReturn:
  c = Counter(a)
  s = 0
  for k, v in c.items():
    s += min(v, k - 1)
  print(s)
  

def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    n = int(input())
    *a, = map(
      int, input().split(),
    )
    solve(a)


main()