def solve() -> None:
    n = int(input())
    h = list(map(int, input().split()))

    # greedy
    max_h = max(h)
    one = 0
    two = 0
    for x in h:
        d = max_h - x
        if d & 1:
            one += 1
            d -= 1
        two += d // 2

    diff = abs(one - two)
    if diff % 3 <= 1:
        x = diff // 3
    else:
        x = diff // 3 + 1
    if one > two:
        one -= x * 2
        two += x
    else:
        one += x * 2
        two -= x
    assert abs(one - two) <= 1
    if one <= two:
        print(two * 2)
    else:
        print(one + two)


def main() -> None:
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
