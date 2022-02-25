import typing
from typing import List


def gcd(
  a: int,
  b: int,
) -> int:
  if not b: return a
  return gcd(b, a % b)


class Solution:
  def findGCD(
    self,
    nums: List[int],
  ) -> int:
    return gcd(max(nums), min(nums))
