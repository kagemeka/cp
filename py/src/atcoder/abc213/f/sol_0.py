import typing 



# TODO implement SA-IS (Suffix Array with Induced Sorting)




class SAIS():
  def __call__(
    self,
    a: typing.List[int],
  ) -> typing.List[int]:
    assert all(0 < x < self.__m for x in a)
    a.append(0)
    n = len(a)
    self.__a = a
    
    is_s = [True] * n
    for i in range(n - 2, -1, -1):
      is_s[i] = (
        is_s[i + 1] if a[i] == a[i + 1] else 
        a[i] < a[i + 1]
      )
    
    is_lms = [
      is_s[i] and not is_s[i - 1] 
      for i in range(n)
    ]
    lms = [i for i in range(n) if is_lms[i]]

    self.__is_s = is_s
    self.__lms = lms

    self.__make_bucket()
    self.__induce()
    return self.__sa


  def __induce(
    self,
  ) -> typing.NoReturn:
    self.__sa = [-1] * len(self.__a)
    self.__set_lms()
    self.__induce_l()
    self.__induce_s()
   

  def __induce_l(
    self,
  ) -> typing.NoReturn:
    sa = self.__sa
    sa_index = self.__b.copy()
    s = 0
    for i in range(self.__m):
      s += sa_index[i]
      sa_index[i] = s - sa_index[i]
    for i in range(len(sa)):
      i = sa[i] - 1
      if i < 0 or self.__is_s[i]: continue
      x = self.__a[i]
      sa[sa_index[x]] = i
      sa_index[x] += 1


  def __induce_s(
    self,
  ) -> typing.NoReturn:
    sa = self.__sa
    sa_index = self.__b.copy()
    for i in range(self.__m - 1):
      sa_index[i + 1] += sa_index[i]
    for i in range(len(sa) - 1, -1, -1):
      i = sa[i] - 1
      if i < 0 or not self.__is_s[i]: continue
      x = self.__a[i]
      sa_index[x] -= 1
      sa[sa_index[x]] = i


  def __init__(
    self,
    max_val: int = 1 << 8,
  ) -> typing.NoReturn:
    self.__m = max_val


  def __make_bucket(
    self,
  ) -> typing.NoReturn:
    a = self.__a
    b = [0] * self.__m
    for x in a: b[x] += 1
    self.__b = b

  
  def __set_lms(
    self,
  ) -> typing.NoReturn:
    sa_index = self.__b.copy()
    for i in range(self.__m - 1):
      sa_index[i + 1] += sa_index[i]
    for i in self.__lms:
      x = self.__a[i]
      sa_index[x] -= 1
      self.__sa[sa_index[x]] = i



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


def sa_test() -> typing.NoReturn:
  s = 'toukoudai'
  s = 'zazazazaz'
  a = list(map(ord, s))
  sa_is = SAIS()
  sa = sa_is(a)
  print(sa)



# main()
sa_test()