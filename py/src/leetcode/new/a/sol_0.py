import typing 
from typing import List 
import numpy as np



class Solution:
  def minimumDifference(
    self, 
    nums: List[int], 
    k: int,
  ) -> int:
    a = np.array(nums)
    a.sort()
    k -= 1
    return (a[k:] - a[:a.size - k]).min()
   
        