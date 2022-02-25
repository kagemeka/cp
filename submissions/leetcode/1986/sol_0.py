import typing


class Solution:
  def minSessions(
    self,
    a: typing.List[int],
    t0: int,
  ) -> int:
    inf = 1 << 10
    n = len(a)
    dp = [
      [(inf, 0)] * n
      for _ in range(1 << n)
    ]
    for i in range(n):
      dp[1 << i][i] = (0, a[i])

    for s in range(1 << n):
      for i in range(n):
        if ~s >> i & 1: continue
        u = s & ~(1 << i)
        for j in range(n):
          if ~u >> j & 1: continue
          c, t = dp[u][j]
          if t + a[i] > t0:
            c += 1
            t = a[i]
          else:
            t += a[i]
          dp[s][i] = min(dp[s][i], (c, t))
    c, t = min(dp[-1])
    return c + (t > 0)
