import collections


def solve() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    c = max(collections.Counter(a).values())

    operations = 0
    while c < n:
        operations += 1
        if c <= n // 2:
            operations += c
            c *= 2
        else:
            operations += n - c
            c = n
    print(operations)


def main() -> None:
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
