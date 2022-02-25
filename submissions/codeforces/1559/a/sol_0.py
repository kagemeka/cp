import typing



def solve(
  n: int,
  a: typing.List[int],
) -> typing.NoReturn:


  # def calc_max(
  #   l: int,
  #   r: int,
  # ) -> int:
  #   mx = 0
  #   m = (r - l) // 2
  #   for i in range(m + 1):
  #     mx = max(mx, a[l + i] & a[r - i])
  #   return mx


  # mn = max(a)
  # for l in range(n):
  #   for r in range(l, n):
  #     mn = min(mn, calc_max(l, r))

  # print(mn)
  v = (1 << 40) - 1
  for x in a:
    v &= x
  print(v)




def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    n = int(input())
    *a, = map(int, input().split())
    solve(n, a)


main()
