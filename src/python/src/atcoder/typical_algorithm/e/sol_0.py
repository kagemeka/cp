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
    (c, (u, v)),
    shape=(n, n),
    dtype=np.int64,
  )
  dist = scipy.sparse.csgraph.floyd_warshall(
    csgraph=g,
    directed=True,
  ).astype(np.int64)
  print(dist.sum())
  

def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  uvc = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3)
  solve(n, uvc)


main()