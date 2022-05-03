# pass or fail


def main() -> None:
    t = int(input())

    pass_count = 0
    for _ in range(t):
        m, p = map(int, input().split())
        if m > p:
            m, p = p, m
        if p < 10:
            continue
        if m + p < 15:
            continue
        pass_count += 1
    print("Genius" if pass_count >= (t + 1) // 2 else "Not Genius Yet")


if __name__ == "__main__":
    main()
