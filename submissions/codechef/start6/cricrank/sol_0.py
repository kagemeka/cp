
import typing



def solve(
  a: typing.Iterator[int],
  b: typing.Iterator[int],
) -> typing.NoReturn:
  res = 0
  for x, y in zip(a, b):
    res += (x > y) * 2 - 1
  print(
    'A' if res > 0 else 'B',
  )



def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    a = map(
      int,
      input().split(),
    )
    b = map(
      int,
      input().split(),
    )
    solve(a, b)


main()
