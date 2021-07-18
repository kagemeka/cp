
# sieve of eratosthenes
import numpy as np 
import typing

import numba as nb


@nb.njit
def combinations(
  n: int,
  r: int,
) -> np.array:
  a = np.arange(n)
  ls = []
  if r < 0 or r > n: return np.array(ls)
  rng = np.arange(r)[::-1]
  i = np.arange(r)
  ls.append(list(a[:r]))
  while 1:
    for j in rng:
      if i[j] != j + n - r:
        break
    else: return np.array(ls)
    i[j] += 1
    for j in range(j + 1, r):
      i[j] = i[j - 1] + 1
    b = []
    for j in i: b.append(a[j])
    ls.append(b)





# TODO cut below

import typing



class Permutations():
  def __call__(
    self,
    a: typing.Iterable[
      typing.Any,
    ],
    r: int,
  ) -> typing.AsyncIterator[
    typing.Tuple[typing.Any],
  ]:
    a = tuple(a)
    n = len(a)
    if r < 0 or r > n: return
    rng = range(r)
    i = list(range(n))
    c = list(rng)
    yield a[:r]
    while 1:
      for j in reversed(rng):
        c[j] += 1
        if c[j] == n:
          i[j:] = (
            i[j + 1:]
            + i[j:j + 1]
          )
          c[j] = j
          continue
        k = c[j]
        i[j], i[k] = i[k], i[j]
        yield tuple(
          a[j] for j in i[:r]
        )
        break
      else: return





def test():
  # a = np.arange(5)
  # for i in range(1):
  #   c = combinations(20, 10)
  # print(c)
  fn = Permutations()
  for p in fn(range(5), 3):
    print(p)
  ...


if __name__ == '__main__':
  test()

