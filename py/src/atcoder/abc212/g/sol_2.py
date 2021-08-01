import typing 
import numpy as np
import numba as nb

# @nb.njit(
#   cache=True,
# )
# def find_divisors(
#   n: int,
# ) -> np.array:
#   i = np.arange(int(n ** .5))
#   i += 1
#   i = i[n % i == 0]
#   i = np.hstack((i, n // i))
#   return np.unique(i)






@nb.njit
def bit_length(n: int) -> int:
  c = 0
  while n: n >>= 1; c += 1
  return c



def main() -> typing.NoReturn:
  mod = 998244353
  # p = int(input())
  # n = p - 1
  # print(find_divisors(10 ** 6))
  print(bit_length(1))


main()