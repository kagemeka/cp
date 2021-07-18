import typing
import numpy as np


class Solution:
  def addRungs(
    self, 
    rungs: typing.List[int], 
    dist: int,
  ) -> int:
    return Solve()(rungs, dist)


class Solve():
  def __call__(
    self,
    rungs: typing.List[int],
    dist: int,
  ) -> int:
    a = np.array(rungs)
    a = np.pad(a, (1, 0))
    d = a[1:] - a[:-1]
    return np.sum(
      (d - 1) // dist,
    )                 