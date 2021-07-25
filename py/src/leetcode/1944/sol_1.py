from typing import List


class Solution:
  def canSeePersonsCount(
    self, 
    heights: List[int],
  ) -> List[int]:
    n = len(heights)
    s = []
    res = [0] * n 
    for i in range(
      n - 1, -1, -1,
    ):
      h = heights[i]
      while s and s[-1] <= h:
        s.pop(); res[i] += 1
      res[i] += len(s) > 0
      s.append(h)
    return res
