import sys
import typing



def win_case(
  s: str,
) -> int:
  s = list(s)
  n = len(s)
  for i in range(n):
    if s[i] != '?': continue
    s[i] = (
      '0' if i & 1 else '1'
    )
  c = [0] * 2
  for i in range(n):
    j = i & 1
    c[j] += s[i] == '1'
    r = (n - i - 1) // 2
    if c[j ^ 1] - c[j] > r:
      return i + 1
    r += j ^ 1
    if c[j] - c[j ^ 1] > r:
      return i + 1
  return 10


def lose_case(
  s: str,
) -> int:
  s = list(s)
  n = len(s)
  for i in range(n):
    if s[i] != '?': continue
    s[i] = (
      '1' if i & 1 else '0'
    )
  c = [0] * 2
  for i in range(n):
    j = i & 1
    c[j] += s[i] == '1'
    r = (n - i - 1) // 2
    if c[j ^ 1] - c[j] > r:
      return i + 1
    r += j ^ 1
    if c[j] - c[j ^ 1] > r:
      return i + 1
  return 10



def solve(
  s: str,
) -> typing.NoReturn:
  mn = min(
    10,
    win_case(s),
    lose_case(s),
  )
  print(mn)


def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    s = input()
    solve(s)


main()
