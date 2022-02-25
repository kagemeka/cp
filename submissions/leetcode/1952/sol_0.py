import typing

def find_divisors(
  n: int,
) -> typing.List[int]:
  i = 1
  a = []
  while i * i < n:
    if n % i:
      i += 1; continue
    a.append(i)
    a.append(n // i)
    i += 1
  if i * i == n:
    a.append(i)
  a.sort()
  return a



class Solution:
  def isThree(
    self,
    n: int,
  ) -> bool:
    divs = find_divisors(n)
    return len(divs) == 3
