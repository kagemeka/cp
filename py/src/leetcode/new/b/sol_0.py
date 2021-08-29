import typing


class Solution:
  def kthLargestNumber(
    self, 
    nums: typing.List[str], 
    k: int,
  ) -> str:
    n = 100
    a = ['0' * (n - len(x)) + x for x in nums]
    a = sorted(zip(a, nums))
    return a[-k][1]
        