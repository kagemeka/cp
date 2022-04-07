# distinct dilemma


def solve() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    # (1 + mx) * mx // 2 <= sum(a)

    lo, hi = 1, 1 << 60
    s = sum(a)
    while hi - lo > 1:
        x = (lo + hi) // 2
        if (1 + x) * x // 2 <= s:
            lo = x
        else:
            hi = x
    print(lo)


def main() -> None:
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
