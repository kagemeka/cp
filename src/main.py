# mypy: ignore-errors

import typing


def debug(*objects: object, **kwargs: object) -> None:
    import os
    import pprint

    if os.environ.get("PYTHON_DEBUG") is None:
        return

    for obj in objects:
        pprint.pprint(obj)

    for key, obj in kwargs.items():
        print(f"{key}: ")


def int_sqrt_binary_search(n: int) -> int:
    lo, hi = 0, n + 1
    while hi - lo > 1:
        x = (lo + hi) >> 1
        if x * x <= n:
            lo = x
        else:
            hi = x
    return lo


def floor_sqrt(n: int) -> int:
    return int_sqrt_binary_search(n)


def sieve_of_eratosthenes(sieve_size: int) -> typing.List[int]:
    if sieve_size <= 2:
        return []
    primes = [2]
    is_prime = [True] * (sieve_size >> 1)
    for i in range(3, sieve_size, 2):
        if not is_prime[i >> 1]:
            continue
        primes.append(i)
        for j in range(i * i >> 1, sieve_size >> 1, i):
            is_prime[j] = False
    return primes


def range_sieve_of_eratosthenes(
    less_than: int,
) -> typing.Callable[[int, int], typing.List[int]]:
    primes = sieve_of_eratosthenes(floor_sqrt(less_than) + 1)

    def query(lo: int, hi: int) -> typing.List[int]:
        assert lo <= hi <= less_than
        res: typing.List[int] = []
        if hi <= 2:
            return res
        if lo < 2:
            lo = 2
        if lo & 1 == 0:
            if lo == 2:
                res.append(2)
            lo += 1
        if lo == hi:
            return res
        size = (hi - lo + 1) >> 1
        if_prime = [True] * size
        for i in primes[1:]:
            mn = i * i
            if mn >= hi:
                break
            mn = max(mn, (lo + i - 1) // i * i)
            if mn & 1 == 0:
                mn += i
            for j in range((mn - lo) >> 1, size, i):
                if_prime[j] = False
        for i in range(size):
            if if_prime[i]:
                res.append(lo + (i << 1))
        return res

    return query


def sieve_of_eratosthenes_low_memory_generator(
    lo: int,
    hi: int,
) -> typing.Generator[int, None, None]:
    if lo < 2:
        lo = 2
    if hi < 2:
        hi = 2
    query = range_sieve_of_eratosthenes(hi)
    range_size = floor_sqrt(hi) << 3
    for i in range(lo, hi, range_size):
        yield from query(i, min(hi, i + range_size))


def main() -> None:
    a, b = map(int, input().split())
    range_sieve = range_sieve_of_eratosthenes(b + 1)
    print(len(range_sieve(a, b + 1)))

    # n, a, b = map(int, input().split())
    # primes = sieve_of_eratosthenes_low_memory_generator(0, n + 1)
    # i = 0
    # res = []
    # for p in primes:
    #     if i % a == b:
    #         res.append(p)
    #     i += 1
    # print(i, len(res))
    # print(*res)


if __name__ == "__main__":
    main()
