import typing 


def solve(
  n: int,
) -> typing.NoReturn:
  print((n + 1) // 10)


def main():
  t = int(input())
  for _ in range(t):
    n = int(input())
    solve(n)

main()