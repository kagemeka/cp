import typing 



def solve(
  x: int,
  y: int,
) -> typing.NoReturn:
  
  p = max(
    0,
    (6 - x - y) / 6,
  )
  print(p)


def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    x, y = map(
      int,
      input().split(),
    )
    solve(x, y)


main()