import typing 
from math import factorial
import numpy as np
import sys


class ModFactorial:
  def __call__(
    self, 
    n: int = 1 << 20,
  ) -> np.array:
    a = np.arange(n); a[0] = 1
    return self.cumprod(a)


  def cumprod(
    self, 
    a: np.array,
  ) -> np.array:
    m = self.__mod
    l = len(a)
    n = int(np.sqrt(l) + 1)
    a = np.resize(a, (n, n))
    for i in range(n-1):
      a[:, i + 1] *= a[:, i]
      a[:, i + 1] %= m
    for i in range(n-1):
      a[i + 1] *= a[i, -1]
      a[i + 1] %= m
    return np.ravel(a)[:l]


  def __init__(
    self,
    modulo: int,
  ) -> typing.NoReturn:
    self.__mod = modulo 
  

  def inv(
    self, 
    n: int = 1 << 20,
  ) -> np.array:
    a = np.arange(1, n + 1)
    m = self.__mod
    x = int(self(n)[-1])
    a[-1] = pow(x, m - 2, m)
    return self.cumprod(
      a[::-1],
    )[n::-1]



def main() -> typing.NoReturn:
  mod = 10 ** 9 + 7

  fn = ModFactorial(mod)
  fact = fn(1 << 18)
  ifact = fn.inv(1 << 18)

  n = int(input())
  c = np.array(
    sys.stdin.readline()
    .split(),
    dtype=np.int64,
  )
  m = fact[n]
  for x in c:
    m *= ifact[x]
    m %= mod
  
  a = m * ifact[n] % mod * c
  a %= mod
  a *= fact[n - 1]
  a %= mod
  d = 1
  sd = 0
  for i in range(n):
    sd += d
    d *= 10
    d %= mod
  s = sd * a % mod
  s *= np.arange(9) + 1
  s %= mod
  print(s.sum() % mod)


main()

  