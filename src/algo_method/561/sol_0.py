import typing 


def main() -> None:
    n, q = map(int, input().split())
    w = list(map(int, input().split()))
    
    uf = [-1] * n 
    
    def find(u: int) -> int:
        if uf[u] < 0: 
            return u
        uf[u] = find(uf[u])
        return uf[u]
    
    def unite(u: int, v: int) -> None:
        u, v = find(u), find(v)
        if u == v: return 
        if uf[u] > uf[v]:
            u, v = v, u
        uf[u] += uf[v]
        uf[v] = u
    
    for _ in range(q):
        t, x, y = map(int, input().split())
        if t == 0:
            x, y = find(x), find(y)
            if x == y: continue
            nw = w[x] + w[y]
            unite(x, y)
            w[find(x)] = nw
        else:
            print(w[find(x)])
    

main()


