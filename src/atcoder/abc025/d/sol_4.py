import typing 
import sys 
import numpy as np 
import numba as nb 


@nb.njit 
def popcount(n: int) -> int:
    n -= (n >> 1) & 0x5555555555555555
    n = (n & 0x3333333333333333) + ((n >> 2) & 0x3333333333333333)
    n = (n + (n >> 4)) & 0x0f0f0f0f0f0f0f0f
    n = n + (n >> 8)
    n = n + (n >> 16)
    n = n + (n >> 32)
    return n & 0x0000007f


@nb.njit((nb.i4[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  n = len(a)
  fixed_idx = np.full(n, -1, np.int8)
  fixed_val = np.full(n, -1, np.int8)
  for i in range(n):
    if a[i] == -1: continue
    fixed_idx[a[i]] = i
    fixed_val[i] = a[i]

  cum_fixed_idx_set = np.zeros(n, np.int32)
  for i in range(n):
    if not fixed_idx[i]: continue
    cum_fixed_idx_set[i] = 1 << fixed_idx[i]
  for i in range(n - 1):
    cum_fixed_idx_set[i + 1] |= cum_fixed_idx_set[i]


  def can_transit(s, i):
    y, x = divmod(i, 5)
    if 1 <= y < 4 and (s >> i - 5 & 1) ^ (s >> i + 5 & 1):
      return False 
    if 1 <= x < 4 and (s >> i - 1 & 1) ^ (s >> i + 1 & 1):
      return False 
    return True

  def is_impossible(s):
    v = popcount(s) - 1
    return s | cum_fixed_idx_set[v] != s


  mod = 1_000_000_007
  dp = np.empty(1 << n, np.int32)
  dp[0] = 1
  for s in range(1, 1 << n):
    if is_impossible(s): continue
    dp[s] = 0
    v = popcount(s) - 1
    for i in range(n):
      if ~s >> i & 1: continue
      u = s & ~(1 << i)
      if fixed_idx[v] != -1 and fixed_idx[v] != i: continue 
      if fixed_val[i] != -1 and fixed_val[i] != v: continue
      if not can_transit(u, i): continue
      dp[s] = (dp[s] + dp[u]) % mod
  print(dp[-1])


def main() -> typing.NoReturn:
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int32,
  ) - 1
  solve(a)


main()