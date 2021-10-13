import typing 
import sys
import numpy as np



def dfs(
  l: int,
  r: int,
  a: np.array,
  cache: np.array,
) -> int:
  if l + r == a.size: return 0
  v = cache[l, r]
  if v != 1 << 50: return v
  x = dfs(l + 1, r, a, cache)
  y = dfs(l, r + 1, a, cache)
  if (l + r) & 1 == 0:
    v = max(
      x + a[l],
      y + a[-1 - r],
    )
  else: 
    v = min(
      x - a[l],
      y - a[-1 - r],
    )
  cache[l, r] = v
  return v 


def solve(
  n: int,
  a: np.array,
) -> typing.NoReturn:
  inf = 1 << 50
  cache = np.full(
    (n + 1, n + 1),
    inf,
    np.int64,
  )
  print(dfs(0, 0, a, cache))



def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline()
    .split(),
    dtype=np.int64,
  )
  solve(n, a)


OJ = 'ONLINE_JUDGE'
if sys.argv[-1] == OJ:
  from numba import njit, i8
  from numba.pycc import CC 
  cc = CC('my_module')
  dfs = njit(dfs)
  fn = solve
  signature = (i8, i8[:])

  cc.export(
    fn.__name__,
    signature,
  )(fn)
  cc.compile()
  exit(0)


from my_module import solve 
main()