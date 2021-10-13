import typing 




def ceil(
  n: int,
  d: int,
) -> int:
  return (n + d - 1) // d



def solve(
  a: int,
  b: int,
) -> typing.NoReturn:
  x = ceil(b - a, 2)
  if a == b:
    print(x)
    return 
  y = ceil(b - a - 1, 2) + 1
  print(max(x, y))





def main():
  t = int(input())
  for _ in range(t):
    a, b = map(
      int, input().split(),
    )
    solve(a, b)


main()