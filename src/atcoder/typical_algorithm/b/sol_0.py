import typing 
import sys 
import numpy as np
import numba as nb 



@nb.njit(
  (nb.i8[:, :], ),
  cache=True,
)
def solve(
  ab: np.ndarray,
) -> typing.NoReturn:
  n = len(ab)
  sort_idx = np.argsort(ab[:, 1], kind='mergesort')
  ab = ab[sort_idx]
  
  c = t = 0 
  for i in range(n):
    a, b = ab[i]
    if a <= t: continue
    c += 1
    t = b
  print(c)
    

def main() -> typing.NoReturn:
  n = int(input())
  ab = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2)
  solve(ab)


main()
