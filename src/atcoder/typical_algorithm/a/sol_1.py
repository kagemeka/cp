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
  def binary_search():
    lo, hi = -1, a.size 
    while hi - lo > 1:
      i = (lo + hi) // 2
      if a[i] >= k:
        hi = i 
      else:
        lo = i
    return hi 
  i = binary_search()
  print(-1 if i == a.size else i)



def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a, k)


main()
  
  