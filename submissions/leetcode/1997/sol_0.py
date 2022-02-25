import typing
import functools


class Solution:
  def firstDayBeenInAllRooms(
    self,
    nx: typing.List[int],
  ) -> int:
    mod = 10 ** 9 + 7

    @functools.lru_cache(maxsize=None)
    def dfs(i: int):
      if i == 0: return 0
      res = 2 + dfs(i - 1)
      if nx[i - 1] != i - 1:
        res += dfs(i - 1) - dfs(nx[i - 1])
      return res % mod

    return dfs(len(nx) - 1)
