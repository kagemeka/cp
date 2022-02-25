from typing import List



class Solution:
  def numberOfWeeks(
    self,
    milestones: List[int],
  ) -> int:
    s = sum(milestones)
    mx = max(milestones)
    if mx <= (s + 1) // 2:
      return s
    return (s - mx) * 2 + 1
