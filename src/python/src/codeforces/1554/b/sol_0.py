import typing 


def solve(
  n: int,
  k: int,
  a: typing.List[int],
) -> typing.NoReturn:

  def f(i: int, j: int) -> int:
    x, y = a[i], a[j]
    i += 1; j += 1
    return i * j - k * (x | y)

  inf = 1 << 30
  mx = -inf
  for i in range(n):
    if i < n - 2 * k: continue
    for j in range(i + 1, n):
      mx = max(mx, f(i, j))
  
  print(mx)


def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    n, k = map(
      int, input().split(),
    )
    *a, = map(
      int, input().split(),
    )
    solve(n, k, a)


main()