from typing import (
  List,
)

class Solution:
  def maximumNumber(
    self,
    num: str,
    change: List[int],
  ) -> str:
    n = len(num)

    a = list(
      map(int, list(num))
    )
    cnt = 0
    for i in range(n):
      x = a[i]
      if cnt == 0:
        if change[x] <= x:
          continue
        cnt = 1
        a[i] = change[x]
        continue
      if change[x] < x:
        break
      a[i] = change[x]


    return ''.join(
      map(str, a),
    )
