from collections import defaultdict
import typing 



def gcd(a: int, b: int) -> int:
  return gcd(b, a % b) if b else a



class Solution:
  def interchangeableRectangles(
    self, 
    rects: typing.List[typing.List[int]],
  ) -> int:
    c = defaultdict(int)
    for a, b in rects:
      g = gcd(a, b)
      a //= g
      b //= g
      c[(a, b)] += 1
    return sum(v * (v - 1) // 2 for v in c.values())

    
        