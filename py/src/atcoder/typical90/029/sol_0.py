import typing 
import sys 
import numpy as np 
import numba as nb 



@nb.njit 
def seg_build(n: int) -> np.ndarray:
  inf = 1 << 60
  return np.full(2 * n, -inf, np.int64)


@nb.njit 
def seg_build_from_array(a: np.ndarray) -> np.ndarray:
  n = len(a)
  seg = np.empty(n * 2, np.int64)
  seg[n:] = a
  for i in range(n - 1, 0, -1):
    seg[i] = max(seg[i << 1], seg[i << 1 | 1])
  return seg


@nb.njit 
def seg_set(seg: int, l: int, r: int):
  ...


@nb.njit 
def set_get():
  ... 



@nb.njit((nb.i8, nb.i8[:, :]), cache=True)
def solve(w: int, lr: np.ndarray) -> typing.NoReturn:
  a = np.zeros(w, np.int64)
  seg = seg_build_from_array(a)
  print(seg)



def main() -> typing.NoReturn:
  w, n = map(int, input().split())
  lr = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2) - 1
  solve(w, lr)


main()