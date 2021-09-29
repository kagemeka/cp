import typing 


def solve(
  n: int,
  a: typing.List[int],
) -> typing.NoReturn:
  mx = 0 
  for i in range(n - 1):
    mx = max(
      mx, 
      a[i] * a[i + 1],
    )
  print(mx)


def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    n = int(input())
    *a, = map(
      int, input().split(),
    )
    solve(n, a)


main()