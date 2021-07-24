import typing 
from collections import (
  Counter,
)



def solve(
  n: int,
  k: int,
  a: typing.List[int],
) -> typing.NoReturn:
  c = Counter(a)
  for x in a:
    c[x] = min(c[x], k)
  
  b = []
  for i in range(n):
    x = a[i]
    if not c[x]: continue
    c[x] -= 1
    b.append(i)
  
  b.sort(key=lambda i: a[i])
  b = b[:len(b) // k * k]

  color = [0] * n
  c = 1
  for i in b:
    color[i] = c 
    c = c % k + 1
  
  print(*color)
  


def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    n, k = map(
      int,
      input().split(),
    )
    *a, = map(
      int,
      input().split(),
    )
    solve(n, k, a)


main()