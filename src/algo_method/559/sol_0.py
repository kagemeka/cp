import typing 


class UnionFind():
    def __init__(self, n: int) -> None:
        self.__data = [-1] * n
    
    def __len__(self) -> int:
        return len(self.__data)
    
    def find(self, u: int) -> int:
        if self.__data[u] < 0:
            return u
        self.__data[u] = self.find(self.__data[u])
        return self.__data[u]
    
    def unite(self, u: int, v: int) -> None:
        u, v = self.find(u), self.find(v)
        if u == v: return 
        d = self.__data
        if d[u] > d[v]:
            u, v = v, u
        d[u] += d[v]
        d[v] = u 
    
    
def main() -> None:
    n, m = map(int, input().split())
    
    uf = UnionFind(n)
    for _ in range(m):
        a, b = map(int, input().split())
        if uf.find(a) == uf.find(b):
            print('Yes')
            continue
        print('No')
        uf.unite(a, b)
    
main()