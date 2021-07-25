


def solve(
  a: int,
  b: int,
):
  s = a + b
  print(
    1 if s < 3
    else 2 if s <= 10
    else 3 if s <= 60
    else 4
  )

def main():
  t = int(input())
  for _ in range(t):
    a, b = map(
      int,
      input().split(),
    )
    solve(a, b)

main()