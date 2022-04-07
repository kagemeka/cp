# make them equal


def solve() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    # if all are even at first, answer is 0
    # otherwise
    # to all odd (possible)
    # to all even (might be impossible)

    odd_count = sum(x & 1 for x in a)

    to_odd = n - odd_count
    to_even = 1 << 60 if odd_count & 1 else odd_count // 2
    print(min(to_odd, to_even))


def main() -> None:
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
