class Solution:
  def minimumPerimeter(
    self,
    neededApples: int,
  ) -> int:
    n = neededApples

    lo, hi = 0, 1 << 30
    while hi - lo > 1:
      x = (lo + hi) // 2
      if self.s(x) >= n:
        hi = x
      else:
        lo = x
    return hi * 8


  def s(
    self,
    n: int,
  ) -> int:
    return 6 * n * (n + 1)
