import typing 
import sys
import numpy as np 
import scipy.sparse


def solve(
  n: int,
  abc: np.ndarray,
) -> typing.NoReturn:
  a, b, c = abc.T 
  g = scipy.sparse.coo_matrix(
    (c, (a, b)),
    shape=(n, n),
    dtype=np.int64,
  )
  print(g)
  mst = scipy.sparse.csgraph.minimum_spanning_tree(
    g,
    overwrite=False,
  ).astype(np.int64)
  print(mst)
  print(g.sum() - mst.sum())



def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  abc = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3)
  abc[:, :2] -= 1
  solve(n, abc)


main()