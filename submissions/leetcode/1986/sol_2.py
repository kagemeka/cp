import typing
import functools



class Solution:
  def minSessions(
    self,
    a: typing.List[int],
    t0: int,
  ) -> int:
    inf = 1 << 10
    n = len(a)

    @functools.lru_cache(maxsize=None)
    def dfs(
      s: int,
    ) -> typing.Tuple[int, int]:
      if s == 0: return (0, 0)
      res = (inf, 0)
      for i in range(n):
        if ~s >> i & 1: continue
        u = s & ~(1 << i)
        c, t = dfs(u)
        if t + a[i] > t0:
          c += 1
          t = a[i]
        else:
          t += a[i]
        res = min(res, (c, t))
      return res

    c, t = dfs((1 << n) - 1)
    return c + (t > 0)
