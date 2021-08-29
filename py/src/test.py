import typing 
import numba as nb 
import numpy as np



T = typing.TypeVar('T')
@nb.njit
def heappush(
  h: typing.List,
  x: T,
  less: typing.Callable[[T, T], bool],
) -> typing.NoReturn:
  
  ... 


@nb.njit(
  cache=True,
)
def test():
  h = [1]
  heappush(h, 1, lambda x, y: x < y)
  


if __name__ == '__main__':
  test()