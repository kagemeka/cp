import typing
from typing import List
import itertools


class Solution:
  def findDifferentBinaryString(
    self, nums: List[str],
  ) -> str:
    n = len(nums)
    cands = set(
      ''.join(c)
      for c in itertools.product('01', repeat=n)
    )
    cands -= set(nums)
    return cands.pop()
