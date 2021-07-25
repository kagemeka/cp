from collections import (
  Counter,
)


class Solution:
  def areOccurrencesEqual(
    self, 
    s: str,
  ) -> bool:
    c = Counter(s)
    return len(
      set(c.values())
    ) == 1
        