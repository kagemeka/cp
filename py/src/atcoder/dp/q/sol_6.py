import typing 
import sys 
import numpy as np
import numba as nb
from numba import njit, i8



@njit
def seg_f(
  a: int,
  b: int,
) -> int:
  if a >= b: return a 
  return b 


@njit
def seg_e() -> int:
  return 0



@njit
def build_seg(
  raw: np.array,
) -> np.array:
  n = raw.size
  a = np.zeros(
    n << 1,
    dtype=np.int64,
  )
  a[n:] = raw
  for i in range(n - 1, 0, -1):
    a[i] = seg_f(
      a[i << 1],
      a[i << 1 | 1],
    )
  return a


@njit
def set_val(
  seg: np.array,
  i: int,
  x: int,
) -> typing.NoReturn:
  n = seg.size // 2
  i += n
  seg[i] = x
  while i > 1:
    i >>= 1
    seg[i] = seg_f(
      seg[i << 1],
      seg[i << 1 | 1],
    )


def



@njit(
  (i8, i8[:], i8[:]),
  cache=True,
)
def solve(
  n: int,
  h: np.array,
  a: np.array,
) -> typing.NoReturn:
  h -= 1
  seg = np.zeros(
    n,
    dtype=np.int64,
  )
  seg = build_seg(seg)
  print(seg)



def main() -> typing.NoReturn:
  n = int(input())
  h = np.array(
    sys.stdin.readline()
    .split(),
    dtype=np.int64,
  )
  a = np.array(
    sys.stdin.readline()
    .split(),
    dtype=np.int64,
  )
  solve(n, h, a)



main()