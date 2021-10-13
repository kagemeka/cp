import typing 
from bisect import (
  bisect_left,
  bisect_right,
) 


def solve(
  n: int,
  d: int,
  p: typing.List[int],
  s: typing.List[int],
) -> typing.NoReturn:
  ps = sorted(zip(p, s))

  a = []
  b = []
  c = []
  mx = 0
  for p, s in ps:
    if s < mx:
      c.append((p, s))
      continue 
    a.append(p)
    b.append(s)
    mx = s
  
  if a[0] > d:
    print(0)
    return


  n = len(a)
  if n == 1:
    x_p = a.pop()
    x_s = b.pop()
    mx = 0
    for p, s in sorted(c):
      if s < mx:
        continue 
      a.append(p)
      b.append(s)
      mx = s
    i = bisect_right(
      a, 
      d - x_p,
    )
    if i: x_s += b[i - 1]
    print(x_s)
    return

  mx = 0  
  for i, x in enumerate(a):
    y = b[i]
    if x > d: break
    j = bisect_right(
      a,
      d - x,
    ) 
    if not j:
      mx = max(mx, y)
      continue
    j -= 1
    if j == i: j -= 1
    if j < 0:
      mx = max(mx, y)
      continue 
    mx = max(mx, y + b[j])
  print(mx)

  

def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    n, d = map(
      int, input().split(),
    )
    *p, = map(
      int,
      input().split()
    )
    *s, = map(
      int, 
      input().split(),
    )
    solve(n, d, p, s)



main()