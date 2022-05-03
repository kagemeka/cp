# prime sum
import math


def solve() -> None:
    a, b = map(int, input().split())
    if a == 1 or b == 1:
        print(-1)
        return
    if math.gcd(a, b) == 1:
        print(1)
    else:
        print(0)


def main() -> None:
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
