# stable mex


def solve() -> None:
    ...
    # mex = 0 -> min - 1
    # mex = max + 1 -> -1
    # ex if mex = n -> (number of continuous n integers sequence) - 1

    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(set(a))

    n = len(a)

    if a[0] != 0:
        print(a[0] - 1)
        return

    if 1 not in a:
        print(-1)
        return

    for i in range(n):
        if a[i] != i:
            mex = i
            break
    else:
        print(0)
        return

    count = 0
    now = 1
    for i in range(1, n):
        if a[i] == a[i - 1] + 1:
            now += 1
            continue
        count += now >= mex - 1
        now = 1
    count += now >= mex - 1
    print(count - 1)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
