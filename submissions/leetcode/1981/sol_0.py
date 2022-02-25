import typing
from typing import List
import numpy as np


class Solution:
  def minimizeTheDifference(
    self,
    mat: List[List[int]],
    target: int,
  ) -> int:
    u = 1 << 17
    dp = np.zeros(u, dtype=np.bool8)
    dp[0] = True
    for row in mat:
      ndp = np.zeros(u, dtype=np.bool8)
      for x in row:
        ndp[x:] |= dp[:-x]
      dp = ndp
    i = np.flatnonzero(dp)
    return np.abs(target - i).min()
