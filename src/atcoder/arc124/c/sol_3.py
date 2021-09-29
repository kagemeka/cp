import typing
import numpy as np
import sys
import numba as nb



@nb.njit
def divisors(
  n: int,
) -> np.array:
  x = int(n ** .5)
  i = np.arange(1, x + 1)
  i = i[n % i == 0]
  d = np.concatenate((
    i, 
    n // i,
  ))
  return np.unique(d)


@nb.njit(
  (nb.i8, nb.i8[:], nb.i8[:]),
  cache=True,
)
def solve(
  n: int,
  a: np.array,
  b: np.array,
) -> typing.NoReturn:

  d1 = divisors(a[0])
  d2 = divisors(b[0])

  tmp = []
  for d in d1:
    if (
      (a % d == 0)
      | (b % d == 0)
    ).all(): tmp.append(d)
  d1 = np.array(tmp)
      
  tmp = []
  for d in d2:
    if (
      (a % d == 0)
      | (b % d == 0)
    ).all(): tmp.append(d)
  d2 = np.array(tmp)
  
  def ok(x, y):
    for i in range(n):
      if (
        a[i] % x == 0
        and b[i] % y == 0
      ): continue
      if (
        a[i] % y == 0
        and b[i] % x == 0
      ): continue
      return False 
    return True
  
  mx = 0
  for x in d1:
    for y in d2:
      if ok(x, y): 
        mx = max(mx, x * y)

  g = 0
  for x in a: g = np.gcd(g, x)
  for x in b: g = np.gcd(g, x)
  return mx // g

      
 

def main() -> typing.NoReturn:
  n = int(input())
  a, b = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2).T
  print(solve(n, a, b))
  

main()