import typing
import sys 
import numpy as np 



def dfs(
  l: int,
  r: int,
  s: np.array,
  cache: np.array,
) -> int:
  if r - l == 1: return 0
  v = cache[l, r]
  if v != 0: return v 
  v = 1 << 50
  for m in range(l + 1, r):
    v = min(
      v,
      dfs(l, m, s, cache)
      + dfs(m, r, s, cache),
    )
  v += s[r] - s[l]
  cache[l, r] = v 
  return v
  

def solve(
  n: int,
  a: np.array,
) -> typing.NoReturn:
  s = np.zeros(n + 1, np.int64)
  s[1:] = a
  s = np.cumsum(s)
  cache = np.zeros(
    (n + 1, n + 1),
    dtype=np.int64,
  )
  print(dfs(0, n, s, cache))


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
  dfs = njit(dfs)

  fn = solve
  signature = (i8, i8[:])
  
  from numba.pycc import CC 
  cc = CC('my_module')
  cc.export(
    fn.__name__,
    signature,
  )(fn)

  cc.compile()

  exit(0)


from my_module import solve
main()