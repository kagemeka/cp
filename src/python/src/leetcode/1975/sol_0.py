import typing 
from typing import List
import itertools


class Solution:
  def maxMatrixSum(
    self, 
    matrix: List[List[int]],
  ) -> int:
    n = len(matrix)
    *a, = itertools.chain.from_iterable(matrix)
    m = sum(x < 0 for x in a)
    *a, = map(abs, a)
    return sum(a) - min(a) * 2 * (m & 1)

        