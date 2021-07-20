from __future__ import (
  annotations,
)

import enum


class Modulo(
  enum.IntEnum
):
  MOD0 = 10 ** 4 + 7
  MOD1 = 998_244_353
  MOD2 = 10 ** 9 + 7
  MOD3 = 10 ** 9 + 9


# TODO cut below


from abc import (
  ABC,
)
import typing



@typing.final
class Modular():

  def __init__(
    self,
    value: int,
    modulo: int,
  ) -> typing.Noreturn:
    self.__value = value
    self.__mod = modulo
    self.__value %= self.mod


  @property
  def mod(self) -> int:
    return self.__mod
  

  def __repr__(self) -> str:
    return f'{self.__value}'
  
  
  def clone(self) -> Modular:
    return Modular(
      self.__value,
      self.__mod,
    )


  @classmethod
  def __to_mod(
    cls, 
    rhs: T,
  ):
    if type(rhs) != int:
      return rhs 
    return cls(rhs, self.mod)


  def __add__(
    self, 
    rhs: T,
  ) -> Modular:
    x = self.clone()
    rhs = self.__to_mod(rhs)
    x.__value += rhs.__value
    x.__value %= self.mod
    return x
  

  def __iadd__(
    self, 
    rhs: T,
  ) -> Modular:
    return self + rhs


  def __radd__(
    self, 
    lhs: T,
  ) -> Modular:
    return self + lhs
  

  def __neg__(self) -> Modular:
    return Modular(
      -self.__value,
      self.mod,
    )


  def __sub__(
    self, 
    rhs: T,
  ) -> Modular:
    return self + -rhs
  

  def __isub__(
    self, 
    rhs: T,
  ) -> Modular:
    return self - rhs

  
  def __rsub__(
    self, 
    lhs: T,
  ) -> Modular:
    return -self + lhs


  def __mul__(
    self, 
    rhs: T,
  ) -> Modular:
    x = self.clone()
    rhs = self.__to_mod(rhs)
    x.__value *= rhs.__value
    x.__value %= self.mod
    return x


  def __imul__(
    self, 
    rhs: T,
  ) -> Modular:
    return self * rhs


  def __rmul__(
    self, 
    lhs: T,
  ) -> Modular:
    return self * lhs
  

  def __truediv__(
    self, 
    rhs: T,
  ) -> Modular:
    rhs = self.__to_mod(rhs)
    return self * rhs.inv()
  

  def __itruediv__(
    self,
    rhs: T,
  ) -> Modular:
    return self / rhs


  def __rtruediv__(
    self,   
    lhs: T,
  ) -> Modular:
    return self.inv() * rhs 


  def __pow__(self, n: int):
    if n == 0:
      e = self.mul_identity()
      return e
    a = self ** (n >> 1)
    a *= a
    if n & 1: a *= self
    return a
  

  def __ipow__(self, n: int):
    return self ** n


  def __rpow__(self, rhs):
    rhs = self.modularize(
      rhs,
    )
    return rhs ** self.value


  @classmethod
  def mul_identity(cls) -> cls:
    return cls(1)

    
  def inv(self):
    i = self ** (self.mod - 2)
    return i
  

  def __eq__(self, rhs):
    rhs = self.modularize(
      rhs,
    )
    return (
      self.value == rhs.value
    )


  def congruent(
    self, 
    rhs,
  ):
    return self == rhs
  

  def factorial(
    self, 
  ):
    n = self.value
    fact = [
      self.__class__(i)
      for i in range(n)
    ]
    fact = np.array(fact)
    e = self.mul_identity()
    fact[0] = e
    fact.cumprod(out=fact)
    return fact
  

  def inv_factorial(
    self,
  ): 
    fact = self.factorial()
    n = self.value
    ifact = np.arange(
      1, 
      n + 1,
    ).astype(object)
    ifact[-1] = fact[-1].inv()
    ifact[::-1].cumprod(
      out=ifact[::-1],
    )
    return ifact



T = typing.Type = typing.Union[
  int,
  Modular,
]


class ModFactory():
  def __call__(
    self,
    value: int,
  ) -> typing.NoReturn:
    ...
  

  def __init__(
    self,
    modulus: int,
  ) -> typing.NoReturn:
    self.__mod = modulus



def test():
  s = open('..


if __name__ == '__main__':
  test()