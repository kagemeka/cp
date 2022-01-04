import typing

def main() -> typing.NoReturn:
  n = int(input())
  # y >= x^2 - (x - 1)^2 = 2x - 1 (x >= 1 because 0 is a squqre number.)
  # y <= n
  # \sum_y{y} <= x^2
  # f(x) := count of y when x is fixed
  # f(x) = f(x - 1) + 1 (2x - 1 <= n, otherwize 0)
  # f(1) = 1
  # x <= (n + 1) / 2
  # \sum_{i=y}^{x} {2i - 1} = x - y + 1 + (y + x)(x - y + 1) = x^2 - y^2 + 2x <= min(x^2, n)
  # y^2 >= max(x^2 - n, 0) + 2x
  x_mx = (n + 1) // 2
  MOD = 998_244_353
  print(x_mx)
  s = (1 + x_mx) % MOD * x_mx % MOD * pow(2, -1, MOD) % MOD
  print(s)

main()