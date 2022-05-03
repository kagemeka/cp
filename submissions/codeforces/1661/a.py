def solve() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s = 0
    for i in range(n - 1):
        d0 = abs(a[i] - a[i + 1])
        d1 = abs(b[i] - b[i + 1])
        d2 = abs(a[i] - b[i + 1])
        d3 = abs(b[i] - a[i + 1])
        s += min(d0 + d1, d2 + d3)
    print(s)


def main() -> None:
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
