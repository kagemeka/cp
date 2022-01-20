import typing 


def sum_of_pow_2(n: int) -> int:
    return n * (n + 1) // 2 * (2 * n + 1) // 3


def f(n: int) -> int:
    return 4 * sum_of_pow_2(n) - 4 * n * (n + 1) // 2 + n


def main() -> None:
    l, r = map(int, input().split())
    print(f(r) - f(l - 1))

main()