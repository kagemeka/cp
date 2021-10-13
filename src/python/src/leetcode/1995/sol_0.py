import typing 
import itertools


class Solution:
  def countQuadruplets(
    self, 
    a: typing.List[int],
  ) -> int:
    c = 0 
    for comb in itertools.combinations(a, 4):
      c += sum(comb[:3]) == comb[3]
    return c
      

        