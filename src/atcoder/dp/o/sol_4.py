import typing
import sys 
import numpy as np


class BitCnt():
  def __getitem__(
    self,
    n: int,
  ) -> int:
    return self.__a[n]
  
  def __call__(
    self,
    n: int,
  ) -> int:
    return self.__a[n]
  

  def __init__(
    self,
    n: int,
  ) -> typing.NoReturn:
    a = [0] * (n + 1)
    for i in range(n):
      a[i] = a[i // 2] + i % 2
    self.__a = a
    

  
def solve(
  n: int,
  a: typing.List[int],
) -> typing.NoReturn:
  a = a.astype(np.bool8)
  mod = 10 ** 9 + 7
  dp = np.zeros(
    1 << n,
    dtype=np.int64,
  )
  dp[0] = 1
  bitcnt = BitCnt(1 << 22)


  i = np.arange(n)
  j = 1 << i
  for s in range((1 << n) - 1):
    c = bitcnt[s]
    ok = ~s >> i & 1 == 1
    ok &= a[c]
    k = s | j[ok]
    dp[k] += dp[s]
    dp[k] %= mod  
  print(dp[-1])
    


def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, n)
  solve(n, a)


main()