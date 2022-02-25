import typing
import sys
sys.setrecursionlimit(1 << 20)


def gcd(a: int, b: int) -> int:
  if not b: return a
  return gcd(b, a % b)


def dfs(
  x: int,
  y: int,
) -> int:
  g = gcd(x, y)
  if g != 1: return 0
  return min(
    dfs(x + 1, y),
    dfs(x, y + 1),
  ) + 1


def solve(
  x: int,
  y: int,
) -> typing.NoReturn:
  g = gcd(x, y)
  if g != 1:
    print(0)
    return

  g = gcd(x + 1, y)
  if g != 1:
    print(1)
    return

  if gcd(x, y + 1) != 1:
    print(1)
    return
  print(2)



def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    x, y = map(
      int, input().split(),
    )
    solve(x, y)


main()
