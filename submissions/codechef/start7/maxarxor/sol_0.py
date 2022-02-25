import typing


def solve(
  n: int,
  k: int,
) -> typing.NoReturn:
  v = (pow(2, n) - 1) * 2
  k = min(k, pow(2, n - 1))
  print(v * k)



def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    n, k = map(
      int, input().split(),
    )
    solve(n, k)



main()
