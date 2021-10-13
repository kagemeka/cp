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
  dist = scipy.sparse.csgraph.dijkstra(
    csgraph=g, 
    directed=True, 
    indices=0,
  ).astype(np.int64)
  print(dist[-1])


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  uvc = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3)
  solve(n, uvc)


main()