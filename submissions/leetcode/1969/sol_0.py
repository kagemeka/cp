import typing


mod = 10 ** 9 + 7

class Solution:
  def minNonZeroProduct(
    self,
    p: int,
  ) -> int:
    n = (1 << p) - 1
    res = n % mod * pow(n - 1, n // 2, mod) % mod
    return res
