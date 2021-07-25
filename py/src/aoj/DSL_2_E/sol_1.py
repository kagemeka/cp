from __future__ import (
  annotations,
)
import typing


import dataclasses


T = typing.TypeVar('T')
@dataclasses.dataclass
class Monoid(
  typing.Generic[T],
):
  fn: typing.Callable[
    [T, T], 
    T,
  ]
  e: typing.Callable[[], T]
  


T = typing.TypeVar('T')
class LazySegTree():
  ...

  def __init__(
    self,
    monoid: Monoid[T],
    n: int,
  ) -> typing.NoReturn:
    self.__m = monoid
    n = (n - 1).bit_length()
    n = 1 << n
    self.__a = [
      monoid.e()
      for _ in range(n << 1)
    ]
    