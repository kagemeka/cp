import typing 
from itertools import (
  permutations,
)


def main() -> typing.NoReturn:
  mod = 10 ** 9 + 7
  n = int(input())
  *c, = map(
    int, input().split(),
  )
  a = []
  for i in range(9):
    a += [i + 1] * c[i]

  *perms, = set(
    permutations(a),
  )
  s = [0] * n
  for p in perms:
    for i in range(n):
      s[i] += p[i]
      s[i] %= mod
  
  d = 1
  tot = 0
  for i in range(n):
    tot += d * s[i]
    d *= 10
  print(tot % mod)


main()
  