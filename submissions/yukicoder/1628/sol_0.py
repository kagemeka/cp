import typing


def main() -> typing.NoReturn:
  n = int(input())
  *c, = map(
    int, input().split(),
  )
  m = ''
  for i in range(9):
    m += str(i + 1) * c[i]
  print(m[::-1])


main()
