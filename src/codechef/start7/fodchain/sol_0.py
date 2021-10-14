import typing 


def solve(
  e: int,
  k: int,
) -> typing.NoReturn:
  cnt = 0
  while e:
    e //= k
    cnt += 1
  print(cnt)


def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    e, k = map(
      int, input().split(),
    )
    solve(e, k)


main()