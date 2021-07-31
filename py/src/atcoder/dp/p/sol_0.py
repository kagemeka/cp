import typing 
import sys 



def solve(
  n: int,
  xy: typing.Iterable[
    typing.Tuple(int, int),
  ],
) -> typing.NoReturn:
  ... 
  g = 


def main() -> typing.NoReturn:
  n = int(input())
  xy = map(
    int,
    sys.stdin.read().split(),
  )
  xy = zip(*[xy] * 2)
  solve(n, xy



main()