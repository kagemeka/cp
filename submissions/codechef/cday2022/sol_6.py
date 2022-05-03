# grid x grid


def solve() -> None:
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    def can_do() -> bool:
        a[0][0] -= 1
        y, x = 0, 0
        while y != n - 1 or x != m - 1:
            if x + 1 < m and a[y][x + 1] != 0:
                x += 1
            elif y + 1 < n and a[y + 1][x] != 0:
                y += 1
            else:
                return False
            a[y][x] -= 1
        return True

    while a[0][0]:
        if can_do():
            continue
        print("NO")
        return

    for i in range(n):
        for j in range(m):
            if a[i][j] != 0:
                print("NO")
                return
    print("YES")


def main() -> None:
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
