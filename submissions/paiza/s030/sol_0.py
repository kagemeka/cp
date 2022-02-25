import typing
import dataclasses


S = typing.TypeVar('S')
@dataclasses.dataclass
class Monoid(typing.Generic[S]):
    op: typing.Callable[[S, S], S]
    e: typing.Callable[[], S]
    commutative: bool



S = typing.TypeVar('S')
@dataclasses.dataclass
class Group(typing.Generic[S], Monoid[S]):
    inverse: typing.Callable[[S], S]



def bit_length_table(n: int) -> typing.List[int]:
    l = [0] * n
    for i in range(1, n): l[i] = l[i >> 1] + 1
    return l


S = typing.TypeVar('S')
class SparseTable():
    def __init__(
        self,
        monoid: Monoid[S],
        a: typing.List[S],
    ) -> typing.NoReturn:
        n = len(a)
        bit_len = bit_length_table(n + 1)
        k = bit_len[n]
        table = [[-1] * n for _ in range(k)]
        table[0] = a.copy()
        for i in range(k - 1):
            table[i + 1] = table[i].copy()
            for j in range(n - (1 << i)):
                table[i + 1][j] = monoid.op(table[i][j], table[i][j + (1 << i)])
        self.__table = table
        self.__bit_len = bit_len
        self.__monoid = monoid


    def get(self, l: int, r: int) -> S:
        k = self.__bit_len[r - l] - 1
        t = self.__table
        return self.__monoid.op(t[k][l], t[k][r - (1 << k)])


S = typing.TypeVar('S')
class FenwickTree(typing.Generic[S]):
    def __init__(
        self,
        monoid: Monoid[S],
        a: typing.List[S],
    ) -> typing.NoReturn:
        n = len(a)
        fw = [None] * (n + 1)
        fw[1:] = a.copy()
        for i in range(1, n + 1):
            j = i + (i & -i)
            if j < n + 1:
                fw[j] = monoid.op(fw[j], fw[i])
        self.__data = fw
        self.__monoid = monoid

    def __setitem__(self, i: int, x: S) -> typing.NoReturn:
        d = self.__data
        size = len(d) - 1
        assert 0 <= i < size
        i += 1
        while i < size + 1:
            d[i] = self.__monoid.op(d[i], x)
            i += i & -i

    def __getitem__(self, i: int) -> S:
        m, d = self.__monoid, self.__data
        assert 0 <= i < len(d)
        v = m.e()
        while i > 0:
            v = m.op(v, d[i])
            i -= i & -i
        return v

    def max_right(self, is_ok: typing.Callable[[S], bool]) -> int:
        m, d = self.__monoid, self.__data
        n = len(d)
        l = 1
        while l << 1 < n: l <<= 1
        v, i = m.e(), 0
        while l:
            if i + l < n and is_ok(m.op(v, d[i + l])):
                i += l
                v = m.op(v, d[i])
            l >>= 1
        return i



class PointAddRangeSum():
    __G = Group(
        op=lambda x, y: x + y,
        e=lambda: 0,
        commutative=True,
        inverse=lambda x: -x,
    )

    def __init__(self, a: typing.List[int]) -> typing.NoReturn:
        self.__fw = FenwickTree(self.__G, a)


    def __setitem__(self, i: int, x: S) -> typing.NoReturn:
        self.__fw[i] = x

    def __getitem__(self, i: int) -> S:
        return self.__fw[i]


    def get_range(self, l: int, r: int) -> S:
        G = self.__G
        return G.op(G.inverse(self.__fw[l]), self.__fw[r])


    def max_right(self, is_ok: typing.Callable[[S], bool]) -> int:
        return self.__fw.max_right(is_ok)



class Multiset():
    def __init__(self, n: int) -> typing.NoReturn:
        self.__fw = PointAddRangeSum([0] * n)
        self.__n = n

    def size(self) -> int:
        return self.__fw[self.__n - 1]

    def add(self, x: int) -> typing.NoReturn:
        self.__fw[x] = 1

    def pop(self, x: int) -> typing.NoReturn:
        fw = self.__fw
        assert fw.get_range(x, x + 1) > 0
        fw[x] = -1

    def get(self, i: int) -> typing.NoReturn:
        fw = self.__fw
        assert 0 <= i < fw[self.__n - 1]
        def is_ok(v: S) -> bool: return v < i + 1
        return fw.max_right(is_ok)

    def max(self) -> int:
        return self.get(self.size() - 1)

    def min(self) -> int:
        return self.get(0)

    def lower_bound(self, x: int) -> int:
        return self.__fw[x]

    def upper_bound(self, x: int) -> int:
        return self.__fw[x + 1]




def solve(a: typing.List[int], m: int) -> typing.NoReturn:
    n = len(a)
    inf = 1 << 30
    monoid = Monoid(op=lambda x, y: min(x, y), e=lambda: inf, commutative=True)
    sparse_table = SparseTable(monoid, a)
    multiset = Multiset(n)

    tot = 0
    cnt = 0
    for i, x in sorted(enumerate(a), key=lambda x: -x[1])[:-2]:
        k = multiset.lower_bound(i)
        l = multiset.get(k - 1) if k - 1 >= 0 else 0
        r = multiset.get(k) if k < cnt else n
        p = x - max(sparse_table.get(l, i + 1), sparse_table.get(i, r))
        tot += p >= m
        multiset.add(i)
        cnt += 1
    print(tot)



import sys

def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    *a, = map(int, sys.stdin.read().split())
    solve(a, m)
    ...

main()
