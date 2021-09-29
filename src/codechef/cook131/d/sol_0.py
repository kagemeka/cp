import typing 
from collections import (
  Counter,
)



def solve(
  n: int,
  a: typing.List[int],
) -> typing.NoReturn:
  c = Counter(a)
  a = sorted(c.keys())
  
  m = len(a)
  print(
    0 if m == 1 else
    n if a[1] <= a[0] * 2
    else n - c[a[0]]
  )
  


def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    n = int(input())
    *a, = map(
      int, input().split(),
    )
    solve(n, a)


main()