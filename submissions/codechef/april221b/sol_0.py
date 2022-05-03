# dazzling GCD pair
import math


def solve() -> None:
    a, b = map(int, input().split())
    if b - a < 2:
        print(-1)
        return
    if a % 2 == 0:
        print(a, a + 2)
        return
    if b - a < 3:
        print(-1)
        return 
    if math.gcd(a, a + 3) != 1:
        print(a, a + 3)
    else:
        print(a + 1, a + 3)


def main() -> None:
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
