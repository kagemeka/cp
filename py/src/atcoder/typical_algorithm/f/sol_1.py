import typing 
import sys 
import numpy as np 
import numba as nb



@nb.njit
def mst_prim(
  n: int,
  csgraph: np.ndarray,
) -> np.ndarray:
  m = len(csgraph)
  assert csgraph.shape == (m, 3)
  



@nb.njit
def solve(
  n: int,
  uvc: np.ndarray,
) -> typing.NoReturn:
  g = mst_prim(n, uvc)
  print(g[:, 2].sum())


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  uvc = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3)
  solve(n, uvc)


main()