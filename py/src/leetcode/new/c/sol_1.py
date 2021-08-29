import typing 


class Solution:
  def minSessions(
    self, 
    a: typing.List[int], 
    t0: int,
  ) -> int:
    inf = 1 << 10

    n = len(a)
    dp = [(inf, 0)] * (1 << n)
    dp[0] = (0, 0)
    
    for s in range(1 << n):
      for i in range(n):
        if ~s >> i & 1: continue
        u = s & ~(1 << i)
        c, t = dp[u]
        if t + a[i] > t0:
          c += 1
          t = a[i]
        else:
          t += a[i]
        dp[s] = min(dp[s], (c, t))
    c, t = dp[-1]
    return c + (t > 0)
