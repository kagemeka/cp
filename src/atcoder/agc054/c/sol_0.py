import typing 

import dataclasses

class 

T =  typing.TypeVar('T')

class FenwickTree(typing.Generic[T]):
    def __init__(self, m: Monoid, a: typing.List[T]) -> None:
        n = len(a)
        data: typing.List[typing.Optional[T]] = [None] * (n + 1)
        data[1:] = a.copy()
        


def main() -> None:
    n, k = map(int, input().split())
    p = list(map(lambda x: int(x) - 1, input().split()))

    # n <= 5000, k < n
    MOD = 998_244_353

    # let c_i := count of j such that p_j > p_i (j < i).
    # consider the initial relative position against j such that p_j >= p_i for each i.
    # only i such that c_i >= k is swapped from the next right position.

    # fenwick tree
    