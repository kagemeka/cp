import typing 
from collections import (
  Counter,
)


def solve(
  n: int,
  k: int,
  a: typing.List[int],
) -> typing.NoReturn:
  a = [x - 1 for x in a]
  cnt = Counter(a)
  cc = Counter(cnt.values())
  r = sum(
    c * cc[c]
    for c in range(1, k)
  ) // k + sum(
    cc[c]
    for c in range(k, n + 1)
  )
  r *= k 
  a = sorted(
    enumerate(a),
    key=lambda x: (
      -cnt[x[1]], 
      x[1],
    ),
  )
  c = 0
  p = [0] * n
  color = [0] * n
  for i, x in a:
    if not r: break
    if p[x] == k: continue
    color[i] = c + 1
    p[x] += 1
    c += 1; c %= k
    r -= 1
  print(*color)
  

def main():
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