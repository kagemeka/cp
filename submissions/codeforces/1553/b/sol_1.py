import typing


def solve(
  s: str,
  t: str,
) -> typing.NoReturn:
  n, m = len(s), len(t)
  for i in range(n):
    for j in range(i, n):
      ok = True
      k = 0
      for l in range(i, j + 1):
        if (
          k == m
          or s[l] != t[k]
        ):
          ok = False
          break
        k += 1
      for l in range(
        j - 1, -1, -1,
      ):
        if k == m: break
        if s[l] != t[k]:
          ok = False
          break
        k += 1
      if not ok or k != m:
        continue
      print('YES')
      return
  print('NO')


def main():
  t = int(input())
  for _ in range(t):
    s = input()
    t = input()
    solve(s, t)


main()
