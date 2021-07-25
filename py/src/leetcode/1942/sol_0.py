from heapq import (
  heappush,
  heappop,
)

from typing import (
  List,
)

import typing



class Solution:
  def smallestChair(
    self, 
    times: List[List[int]],
    targetFriend: int,
  ) -> int:
    n = len(times)
    m = 1 << 17
    start = [-1] * m  
    end = [
      [] for _ in range(m)
    ]
    for i in range(n):
      ta, tl = times[i]
      start[ta] = i
      end[tl].append(i)
    
    sit = [-1] * n
    q = list(range(m))
    for i in range(m):
      for j in end[i]:
        heappush(q, sit[j])
      j = start[i]
      if j == -1: continue 
      sit[j] = heappop(q)
    return sit[targetFriend]
        
    

      