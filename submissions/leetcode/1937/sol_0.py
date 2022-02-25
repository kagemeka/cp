import typing

class Solution:
  def maxPoints(
    self,
    points: typing.List[
      typing.List[int],
    ],
  ) -> int:
    return Solve()(points)



class Solve():
  def __call__(
    self,
    points: typing.List[
      typing.List[int],
    ],
  ) -> int:
    a = points
    n = len(a)
    m = len(a[0])
    for i in range(n - 1):
      b = a[i]
      lmx = [-1] * m
      rmx = [-1] * m
      mx = 0
      for j in range(m):
        mx = max(mx - 1, b[j])
        lmx[j] = mx
      mx = 0
      for j in range(
        m - 1, -1, -1,
      ):
        mx = max(mx - 1, b[j])
        rmx[j] = mx
      for j in range(m):
        a[i + 1][j] += max(
          lmx[j], rmx[j],
        )
    return max(a[-1])
