import typing 
import numba as nb 
import numpy as np



@nb.njit
def mod_matrix_dot(
  a: np.ndarray,
  b: np.ndarray,
  mod: int,
) -> np.ndarray:
  r, c = a.shape
  h, w = b.shape
  assert c == h
  c = np.zeros(
    (r, w), 
    dtype=np.int64,
  )
  for i in range(r):
    for j in range(w):
      c[i, j] = np.sum(a[i] * b[:, j] % mod) % mod 
  return c
      

# @nb.njit
# def mod_matrix_pow(
#   a: np.ndarray,
#   n: int,
#   mod: int,
# ) -> np.ndarray:
#   if n == 0:
#     return np.eye(
#       a.shape[0],
#       dtype=np.int64,
#     )  
#   x = mod_matrix_pow(a, n >> 1, mod)
#   x = mod_matrix_dot(x, x, mod)
#   if n & 1: 
#     x = mod_matrix_dot(x, a, mod)
#   return x


@nb.njit
def mod_matrix_pow(
  a: np.ndarray,
  n: int,
  mod: int,
) -> np.ndarray:
  x = np.eye(
    a.shape[0],
    dtype=np.int64,
  )
  while n:
    if n & 1:
      x = mod_matrix_dot(x, a, mod)
    x = mod_matrix_dot(x, x, mod)
    n >>= 1
  return x


@nb.njit(
  cache=True,
)
def test():
  a = np.arange(1, 10).reshape(3, 3)
  mod = 998244353
  print(mod_matrix_pow(a, 2, mod))


if __name__ == '__main__':
  test()