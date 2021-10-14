import typing
import numpy as np


def solve(
  n: int,
  a: typing.List[np.array],
  b: np.array,
) -> typing.NoReturn:
  g = np.zeros(n, dtype=int)
  for i, x in enumerate(a):
    x = np.array(x)[1:] - 1
    g[x] = i
  b -= 1
  diff = g[b[:-1]] != g[b[1:]]
  
  print(
    np.count_nonzero(diff) + 1
  ) 


def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    n, m, l = map(
      int,
      input().split(),
    )
    a = [
      [
        int(x) for x in (
          input().split()
        )
      ]
      for _ in range(m)
    ]
    b = np.array(
      input().split(),
      dtype=np.int64,
    )
    solve(n, a, b)


main()