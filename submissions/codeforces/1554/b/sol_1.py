import typing



def solve(
  n: int,
  k: int,
  a: typing.List[int],
) -> typing.NoReturn:
  inf = 1 << 30

  m = n.bit_length()
  mx_i = [0] * (1 << m)
  mx_j = [0] * (1 << m)
  for i in range(
    n - 1, -1, -1,
  ):
    x = a[i]
    if mx_j[x] == 0:
      mx_j[x] = i + 1
      continue
    if mx_i[x] == 0:
      mx_i[x] = i + 1


  for l in range(m):
    for x in range(1 << m):
      if x >> l & 1: continue
      nx = x | (1 << l)
      i = max(
        mx_j[x],
        mx_i[nx],
      )
      j = mx_j[nx]
      if i > j: i, j = j, i
      mx_i[nx], mx_j[nx] = i, j
      print(mx_i, mx_j, l)

  mx = -inf
  for x in range(1 << m):
    if mx_i[x] == 0: continue
    mx = max(
      mx,
      mx_i[x] * mx_j[x] - k * x
    )
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
