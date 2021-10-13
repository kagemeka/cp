import typing 
import numpy as np
import sys


def solve(
  a: np.array,
  q: np.array,
) -> typing.NoReturn:
  a &= 1
  a = np.pad(
    a, 
    (1, 0),
    mode='constant',
  )
  s1 = (a == 1).cumsum()
  l, r = q.T
  o = s1[r] - s1[l - 1]
  e = r - l + 1 - o
  c = e * (e - 1) * (e - 2)
  c //= 6
  c += e * o * (o - 1) // 2
  print(*c, sep='\n')
  


def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    n, q = map(
      int,
      input().split(),
    )
    a = np.array(
      input().split(),
      dtype=np.int64,
    )
    
    q = [
      map(int, input().split())
      for _ in range(q)
    ]
    q = np.array(
      [(*x,) for x in q],
      dtype=np.int64,
    )
    solve(a, q)
    

main()