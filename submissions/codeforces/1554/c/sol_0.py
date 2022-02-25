import typing


def solve(
  n: int,
  m: int,
) -> typing.NoReturn:
  t = m + 1
  l = t.bit_length()
  k = 0
  for i in range(
    l - 1, -1, -1,
  ):
    if n ^ k >= t: break
    if ~t >> i & 1: continue
    k |= (
      (1 << i)
      * (n >> i & 1 ^ 1)
    )
  print(k)


def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    n, m = map(
      int, input().split(),
    )
    solve(n, m)


main()
