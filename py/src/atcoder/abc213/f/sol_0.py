import typing 



# TODO implement SA-IS (suffix array induced sort)




class SAIS():
  def __call__(
    self,
    a: typing.List[int],
  ) -> typing.NoReturn:
    assert all(x > 0 for x in a)
    ...
  

  def __induce(
    self,
  ) -> typing.NoReturn:
    ... 
  

  def __induce_l(
    self,
  ) -> typing.NoReturn:
    ... 
  

  def __induce_s(
    self,
  ) -> typing.NoReturn:
    ... 
    

class SuffixArray():
  ... 



def solve(
  n: int,
  s: str,
) -> typing.NoReturn:
  ...



def main() -> typing.NoReturn:
  n = int(input())
  s = input()
  solve(n, s)


main()