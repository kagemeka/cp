import typing 
import sys 
import numpy as np 
import scipy.sparse



def solve(
  n: int,
  uvc: np.ndarray,
) -> typing.NoReturn:
  u, v, c = uvc.T 
  g = scipy.sparse.csr_matrix(
    arg1=(c, (u, v)),
    shape=(n, n),
    dtype=np.int64,
  )
  mst = scipy.sparse.csgraph.minimum_spanning_tree(
    csgraph=g,
    overwrite=False,
  ).astype(np.int64)
  print(mst.sum())


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  uvc = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3)
  solve(n, uvc)


main()