import typing 
from itertools import (
  permutations,
)
import numpy as np



def main() -> typing.NoReturn:
  mod = 10 ** 9 + 7
  n = int(input())
  *c, = map(
    int, input().split(),
  )
  a = []
  for i in range(9):
    a += [i + 1] * c[i]
  p = np.array((
    *permutations(a),
  ))
  p = np.unique(p, axis=0)
  d = 10 ** np.arange(n)
  s = p.sum(axis=0) % mod * d
  print(s.sum() % mod)


main()
  