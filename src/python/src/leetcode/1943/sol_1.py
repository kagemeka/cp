from collections import (
  defaultdict,
)
from typing import List


class Solution:
  def splitPainting(
    self, 
    segments: List[List[int]],
  ) -> List[List[int]]:
    cnt = defaultdict(int)
    for l, r, c in segments:
      cnt[l] += c 
      cnt[r] -= c
    res = []
    s = l = 0
    for i, x in sorted(
      cnt.items(),
    ):
      if s > 0:
        res.append([l, i, s])
      l = i
      s += x
    return res