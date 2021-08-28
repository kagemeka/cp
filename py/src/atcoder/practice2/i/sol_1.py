import typing 
import sys 
import numpy as np
import numba as nb





def sa_is(
  a: np.ndarray,
) -> np.ndarray:
  ...
  


def solve(
  a: np.ndarray,
) -> typing.NoReturn:
  ...



def main() -> typing.NoReturn:
  s = np.frombuffer(
    sys.stdin.buffer.readline().rstrip(),
    dtype='b',
  ) - ord('a') + 1
  print(s)
  solve(s)


main()