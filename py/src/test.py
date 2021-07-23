from __future__ import (
  annotations,
)


import numpy as np
import numba as nb


import typing


# @nb.njit(cache=True)
def compress(
  a: np.array,
) -> np.array:
  v = np.unique(a)
  return np.searchsorted(v, a)



def test():
  a = np.arange(1 << 23)
  a = compress(a)
  print(a)


if __name__ == '__main__':
  test()