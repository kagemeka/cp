import typing 
import sys 
import numpy as np
import numba as nb 



@nb.njit(
  (nb.i8[:], nb.i8),
  cache=True,
)
def solve(
  a: np.ndarray,
  k: int,
) -> typing.NoReturn:
  i = np.searchsorted(a, k)
  print(-1 if i == a.size else i)



def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a, k)


main()
  
  