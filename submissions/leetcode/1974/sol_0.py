import typing


class Solution:
  def minTimeToType(
    self,
    word: str,
  ) -> int:
    *s, = map(
      lambda x: ord(x) - ord('a'),
      word,
    )
    n = len(s)
    tot = n
    s = [0] + s
    for i in range(n):
      d = abs(s[i + 1] - s[i])
      tot += min(d, 26 - d)
    return tot
