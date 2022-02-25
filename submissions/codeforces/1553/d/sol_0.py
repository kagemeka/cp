import typing


def solve(
  s: str,
  t: str,
) -> typing.NoReturn:
  j = 0
  n, m = len(s), len(t)
  for i in range(n + 1):
    ri, rj = n - i, m - j
    if ri < rj:
      print('NO')
      return
    if (ri - rj) & 1: continue
    if j == m:
      print('YES')
      return
    if s[i] == t[j]: j += 1


def main():
  q = int(input())
  for _ in range(q):
    s = input()
    t = input()
    solve(s, t)


main()
