import typing 
import sys 
import numpy as np 
import numba as nb 



def solve(a, b, c) -> typing.NoReturn:
  cnt = 0 
  q, b = divmod(b, 2)
  if c < q:
    cnt += c
    q -= c
    c = 0
    if a < 2 * q:
      cnt += a // 2
      return cnt
    cnt += q
    a -= q * 2
  else:
    cnt += q
    c -= q    
  q, c = divmod(c, 2)
  if a < q:
    cnt += a
    return cnt
  cnt += q
  a -= q
  if a < c * 3:
    return cnt + a // 3
  cnt += c
  a -= c * 3
  q, a = divmod(a, 5)
  cnt += q
  return cnt


def main() -> typing.NoReturn:
  t = int(input())
  res = []
  for _ in range(t):
    a, b, c = map(int, input().split())
    res.append(solve(a, b, c))
  print(*res, sep='\n')


main()