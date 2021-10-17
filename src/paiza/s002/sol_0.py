import typing 
import sys 



def solve(
    g: typing.List[typing.List[int]],
    sy: int,
    sx: int,
    gy: int,
    gx: int,
) -> typing.NoReturn:
    h, w = len(g), len(g[0])

    dyx = ((-1, 0), (0, -1), (1, 0), (0, 1))
    
    def on_board(y: int, x: int) -> bool:
        return 0 <= y < h and 0 <= x < w
    
    inf = 1 << 30

    dist = [[inf] * w for _ in range(h)]
    dist[sy][sx] = 0
    que = [(sy, sx)]
    for y, x in que:
        for dy, dx in dyx:
            ny, nx = y + dy, x + dx 
            if not on_board(ny, nx): continue
            d = dist[y][x] + 1
            if g[ny][nx] == 1 or d >= dist[ny][nx]: continue
            dist[ny][nx] = d
            que.append((ny, nx))
    res = dist[gy][gx]
    print(res if res < inf else 'Fail')


def main() -> typing.NoReturn:
    w, h = map(int, input().split())
    g = [input().split() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if g[i][j] == 's':
                g[i][j] = 0
                sy, sx = i, j
            elif g[i][j] == 'g':
                g[i][j] = 0
                gy, gx = i, j
            else:
                g[i][j] = int(g[i][j])
    solve(g, sy, sx, gy, gx)


main()