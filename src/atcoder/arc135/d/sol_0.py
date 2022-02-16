import typing


def main() -> None:
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    s = [[0] * (w - 1) for _ in range(h - 1)]

    for i in range(h - 1):
        for j in range(w - 1):
            for dy in range(2):
                for dx in range(2):
                    s[i][j] += a[i + dy][j + dx]

    def on_grid(y: int, x: int) -> bool:
        return 0 <= y < h - 1 and 0 <= x < w - 1

    def compute(i: int, j: int) -> int:
        d = 16
        tmp = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                ni, nj = i + dy, j + dx
                if not on_grid(ni, nj):
                    continue
                tmp += s[ni][nj]
        times = -(tmp // d)
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                ni, nj = i + dy, j + dx
                if not on_grid(ni, nj):
                    continue
                s[ni][nj] += times * (3 - abs(dy) - abs(dx)) 
        return times
    print(s)

    for i in range(h - 1):
        for j in range(w - 1):
            x = compute(i, j)
            for dy in range(2):
                for dx in range(2):
                    a[i + dy][j + dx] += x
    tot = 0
    for i in range(h):
        for j in range(w):
            tot += abs(a[i][j])
    print(tot)
    for i in range(h):
        print(*a[i])


if __name__ == "__main__":
    main()
