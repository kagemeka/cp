import typing
import numpy as np
import sys


def solve(
  n: int,
  a: np.array,
) -> typing.NoReturn:
  s = np.zeros(
    f



def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline()
    .split(),
    dtype=np.int64,
  )
  solve(n, a)


main()

