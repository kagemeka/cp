from typing import List

from bisect import (
  bisect_right,
)


class Solution:
  def canSeePersonsCount(
    self, 
    heights: List[int],
  ) -> List[int]:
    n = len(heights)
    inf = 1 << 30
    a = [-inf] * n
    res = [0] * n 
    for i in range(
      n - 1, -1, - 1,
    ):
      h = heights[i]
      j = bisect_right(a, h)
      k = bisect_right(a, -inf)
      res[i] = j - k + (j != n)
      while k < j:
        a[k] = -inf 
        k += 1
      a[j - 1] = h
    return res