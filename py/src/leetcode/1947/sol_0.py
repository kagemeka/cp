from typing import (
  List,
)
import numpy as np 
from itertools import (
  permutations,
)



class Solution:
  def maxCompatibilitySum(
    self, 
    students: List[List[int]],
    mentors: List[List[int]],
  ) -> int:
    a = np.array(students)
    b = np.array(mentors)
    n, m = a.shape
    i = 1 << np.arange(m)
    a = (a * i).sum(axis=1)
    b = (b * i).sum(axis=1)
    b = permutations(b)
    b = np.array((*b,))
    b ^= a
    b = b[:, :, None]
    b = b >> np.arange(m) & 1
    b = b.sum(axis=-1)
    b = b.sum(axis=-1)
    return (n * m - b).max()