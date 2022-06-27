# / mypy: ignore-errors
import typing


# similar to prim's mst algorithm
def min_weight_dijkstra_dense(
    g: typing.List[typing.List[typing.Optional[int]]],
    src: int,
) -> None:
    n = len(g)
    min_weight = [None] * n
    min_weight[src] = 0
    is_fixed = [False] * n
    for _ in range(n - 1):
        u, wu = None, None
        for i in range(n):
            if is_fixed[i] or min_weight[i] is None:
                continue
            if wu is None or min_weight[i] < wu:
                u, wu = i, min_weight[i]
        if u is None:
            break
        is_fixed[u] = True
        for v in range(n):
            wv = g[u][v]
            if is_fixed[v] or wv is None:
                continue
            if min_weight[v] is None or wv < min_weight[v]:
                min_weight[v] = wv
    return min_weight


T = typing.TypeVar("T")
G = typing.List[typing.List[T]]
F = typing.Callable[[T, T, T], T]
Cb = typing.Callable[[int, G], None]


def floyd_warshall(f: F, g: G, cb: typing.Optional[Cb] = None) -> G:
    n = len(g)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = f(g[i][j], g[i][k], g[k][j])
        if cb:
            cb(k, g)
    return g


def main() -> None:
    n = int(input())

    a = [tuple(map(int, input().split())) for _ in range(n)]

    inf = 1 << 60
    g = [[inf] * n for _ in range(n)]

    for i in range(n):
        xi, yi, pi = a[i]
        for j in range(n):
            xj, yj, pj = a[j]
            d = abs(xi - xj) + abs(yi - yj)
            d = (d + pi - 1) // pi
            g[i][j] = d

    def f(x: int, y: int, z: int) -> int:
        return min(x, max(y, z))

    min_w = floyd_warshall(f, g)
    res = min(max(row) for row in min_w)
    print(res)


main()
