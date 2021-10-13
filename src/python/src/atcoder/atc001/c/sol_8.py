import typing 
import sys 


P = 998_244_353
PRIMITIVE_ROOT = 3
N = 23





def solve(
  a: typing.List[int],
  b: typing.List[int],
) -> typing.NoReturn:
  ... 



def main() -> typing.NoReturn:
  n = int(input())
  a = [-1] * (1 << N)
  b = [-1] * (1 << N)
  for i in range(n):
    a[i + 1], b[i + 1] = map(int, input().split())
  solve(a, b)



main()
