import typing
import sys 
import numpy as np 



def dfs(
  l: int,
  r: int,
  s: np.array,
  cache: np.array,
) -> int:
  ... 
  

def solve(
  n: int,
  a: np.array,
) -> typing.NoReturn:
  ... 


def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline()
    .split(),
    dtype=np.int64,
  )


main()