import typing 


def euler_tour(
    g: typing.List[typing.Tuple[int, int]], 
    root: int,
) -> typing.Tuple[(typing.List[int], ) * 3]:
    n = len(g) + 1
    t = [[] for _ in range(n)]
    for u, v in g:
        t[u].append(v)
        t[v].append(u)
    parent = [-1] * n
    depth = [0] * n
    tour = [-1] * (n << 1)
    st = [root]
    for i in range(n << 1):
        u = st.pop()
        tour[i] = u 
        if u < 0: continue
        st.append(~u)
        for v in t[u][::-1]:
            if v == parent[u]: continue
            parent[v] = u
            depth[v] = depth[u] + 1
            st.append(v)
    return tour, parent, depth


def find_first_indices():
    ...


def find_last_indices(tour: typing.List[int]


def main() -> typing.NoReturn:
    n = int(input())
    uvw = []
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        uvw.append((u, v, w))
    
    tour,_, _ = euler_tour([(u, v) for u, v, w in uvw], 0)
    print(tour)
    MOD = 10 ** 9 + 7
     


main()