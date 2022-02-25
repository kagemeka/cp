def solve() -> int:
    n, m = map(int, input().split())
    xy = [tuple(map(int, input().split())) for _ in range(n)]

    inf = 1 << 60
    mx = -inf

    s = 0
    delta = 0
    a = []
    # sum of area of trapezoid
    for x, y in xy:
        # x *= 2
        if x == 0:
            s += y * delta
            if delta > 0:
                mx = max(mx, s)
                # mx = max(mx, i
            continue
        else:
            print(delta, -1, -1)
            # assert delta % x == 0
            if x < 0 and delta > 0:
                d = delta // (-x)
                assert d >= 0

                # if 0 <= d <= y and x < 0:
                # assert delta * d & 1 == 0
                mx = max(mx, s + (delta + delta + x * d) * (d + 1) // 2)
            mx = max(mx, s + delta)
            next_delta = delta + x * y
            s += (delta + next_delta) * y // 2
            delta = next_delta
            mx = max(mx, s)
        a.append((s, delta, mx))
    print(a)
    return mx
    # print(mx)

    # next_delta = delta +  x * y
    # if next_delta


def main() -> None:
    t = int(input())
    res = []
    for _ in range(t):
        res.append(solve())
    print(*res)


if __name__ == "__main__":
    main()
