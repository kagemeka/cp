import typing
from typing import List



class Solution:
  def rearrangeArray(
    self, 
    nums: List[int]
  ) -> List[int]:
    n = len(nums)
    nums.sort()
    a = [-1] * n 
    m = n // 2
    for i in range(m):
      a[i * 2] = nums[i]
      a[i * 2 + 1] = nums[i + m + (n & 1)]

    if n & 1: a[-1] = nums[m]

    return a
        