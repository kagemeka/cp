from typing import List
from heapq import (
  heappush,
  heappop,
)


class Solution:
  def numberOfWeeks(
    self,
    milestones: List[int],
  ) -> int:
    a = []
    for i, x in enumerate(
      milestones,
    ):
      heappush(a, (-x, i))

    c = 0
    prev = -1
    while a:
      x, i = heappop(a)
      x += 1
      if i != prev:
        c += 1
        prev = i
        if not x: continue
        heappush(a, (x, i))
        continue
      if not a: break
      y, j = heappop(a)
      y += 1
      c += 2
      if y:
        heappush(a, (y, j))
      if x:
        heappush(a, (x, i))
    return c
