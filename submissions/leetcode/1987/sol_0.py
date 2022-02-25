class Solution:
  def numberOfUniqueGoodSubsequences(
    self,
    binary: str,
  ) -> int:
    mod = 10 ** 9 + 7
    a = [int(d) for d in binary]

    dp = [0, 0]
    for d in a:
      dp[d] = sum(dp) + d
      dp[d] %= mod
    res = sum(dp) + (0 in a)
    return res % mod
