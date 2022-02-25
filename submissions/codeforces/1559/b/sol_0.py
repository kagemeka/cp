import typing


def solve(
  n: int,
  s: typing.List[int],
) -> typing.NoReturn:
  inf = 1 << 30
  dp = [[inf] * 2 for _ in range(n + 1)]
  dp[0] = [0, 0]
  for i in range(n):
    if s[i] != 1:
      dp[i + 1][0] = min(
        dp[i][0] + 1,
        dp[i][1],
      )
    if s[i] != 0:
      dp[i + 1][1] = min(
        dp[i][0],
        dp[i][1] + 1,
      )

  rev = [int(dp[-1][1] <= dp[-1][0])]
  for i in range(n - 1, 0, -1):
    a = dp[i]
    rev.append(
      int(dp[i][1] == dp[i + 1][rev[-1]] - (rev[-1] == 1)),
    )

  res = ['R' if x else 'B' for x in rev[::-1]]
  print(''.join(res))



def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    n = int(input())
    s = input()
    s = [
      2 if x == '?' else
      0 if x == 'B' else
      1
      for x in s
    ]
    solve(n, s)


main()
