import typing 
import bisect 



def solve(
  a: typing.List[int],
  k: int,
) -> typing.NoReturn:
  i = bisect.bisect_left(a, k)
  print(-1 if i == len(a) else i)


def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  *a, = map(int, input().split())
  solve(a, k)


main()