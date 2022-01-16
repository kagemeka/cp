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
    

def get_labels(uf: UnionFind) -> typing.List[int]:
    n = len(uf)
    labels = [-1] * n
    label = 0
    for i in range(n):
        if labels[i] != -1: continue
        root = uf.find(i)
        if labels[root] == -1:
            labels[root] = label
            label += 1
        labels[i] = labels[root]
    return labels
    
    
def main() -> None:
    n, m = map(int, input().split())
    
    uf = UnionFind(n)
    
    for _ in range(m):
        a, b = map(int, input().split())
        uf.unite(a, b)
    
    labels = get_labels(uf)
    print(max(labels) + 1)
    
main()