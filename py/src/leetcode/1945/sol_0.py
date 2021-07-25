import typing


class Solution:
  def getLucky(
    self, 
    s: str, 
    k: int,
  ) -> int:
    s = self.convert(s)
    for _ in range(k):
      s = self.transform(s)
    return int(s)


  def convert(
    self,
    s: str,
  ) -> str:
    s = [
      ord(x) - ord('a') + 1
      for x in s
    ]
    return ''.join(
      map(str, s),
    )
  

  def transform(
    self,
    s: str,
  ) -> str:
    s = sum(map(int, list(s)))
    return str(s)
        