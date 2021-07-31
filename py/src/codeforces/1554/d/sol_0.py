import typing 


def solve(
  n: int,
) -> typing.NoReturn:
  if n == 1:
    print('a')
    return
  k = n // 2
  mid = 'b'
  if n & 1: mid += 'c'
  s = 'a' * k
  s += mid
  s += 'a' * (k - 1)
  print(s)


def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    n = int(input())
    solve(n)


main()