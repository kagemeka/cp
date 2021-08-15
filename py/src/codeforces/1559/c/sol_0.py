import typing 



def solve(
  n: int,
  a: typing.List[int],
) -> typing.NoReturn:
  p = list(range(n))
  for i in range(n - 1):
    if a[i] == 1 or a[i + 1] == 0:
      continue
    p.insert(i + 1, n)
    break
  else:
    if a[-1] == 0:
      p.append(n)
    elif a[0] == 1:
      p.insert(0, n)
    else:
      print(-1)
      return
  
  p = [x + 1 for x in p]
  print(*p)


def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    n = int(input())
    *a, = map(int, input().split())
    solve(n, a)


main()