import typing 
import numpy as np
import sys


def solve(
  n: int,
  a: np.array,
) -> typing.NoReturn:
  i = np.arange(30)
  j = 1 << i
  a = a[:, None] >> i & 1
  a = a.sum(axis=0)
  x = (j * (a == n)).sum()
  s = (j * (a > 0)).sum()
  print(x, s - x)


def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    n = int(input())
    a = np.array(
      sys.stdin.readline()
      .split(),
      dtype=np.int64,
    )
    solve(n, a)


main()