def debug(*objects: object, **kwargs: object) -> None:
    import os
    import pprint

    if os.environ.get("PYTHON_DEBUG") is None:
        return

    for obj in objects:
        pprint.pprint(obj)

    for key, obj in kwargs.items():
        print(f"{key}: ")
        pprint.pprint(obj)


def int_sqrt_binary_search(n: int) -> int:
    assert 0 <= n < 1 << 64
    lo, hi = 0, min(1 << 32, n + 1)
    while hi - lo > 1:
        x = (lo + hi) >> 1
        if x * x <= n:
            lo = x
        else:
            hi = x
    return lo


def floor_sqrt(n: int) -> int:
    return int_sqrt_binary_search(n)


def prime_pi_fast(n: int) -> int:
    import numpy as np

    if n < 2:
        return 0
    sqrt = floor_sqrt(n)
    j = np.arange(sqrt) + 1
    small = np.zeros(sqrt + 1, np.int64)
    large = np.zeros(sqrt + 1, np.int64)
    small[1:] = j - 1
    large[1:] = n // j - 1
    for i in range(2, sqrt + 1):
        if small[i] == small[i - 1]:
            continue
        pi = small[i - 1]
        border = sqrt // i
        n_i = n // i
        k = np.arange(1, border + 1)
        large[k] -= large[k * i] - pi
        k = np.arange(border + 1, min(sqrt, n_i // i) + 1)
        large[k] -= small[n_i // k] - pi
        j = np.arange(i * i, sqrt + 1)
        small[j] -= small[j // i] - pi
    return int(large[1])


def prime_pi_fast_optimized(n: int) -> int:
    if n < 2:
        return 0
    if n == 2:
        return 1

    def half(i: int) -> int:
        return (i - 1) >> 1

    sqrt = floor_sqrt(n)
    size = (sqrt + 1) >> 1
    small = list(range(size))
    large = [half(n // (i << 1 | 1)) for i in range(size)]
    unsieved_nums = [i << 1 | 1 for i in range(size)]
    checked_or_sieved = [False] * size
    pi = 0
    for i in range(3, sqrt + 1, 2):
        if checked_or_sieved[half(i)]:
            continue
        i2 = i * i
        if i2 * i2 > n:
            break
        checked_or_sieved[half(i)] = True
        for j in range(i2, sqrt + 1, i << 1):
            checked_or_sieved[half(j)] = True
        ptr = 0
        for k in range(size):
            j = unsieved_nums[k]
            if checked_or_sieved[half(j)]:
                continue
            border = j * i
            large[ptr] = large[k] + pi
            large[ptr] -= (
                large[small[border >> 1] - pi]
                if border <= sqrt
                else small[half(n // border)]
            )
            unsieved_nums[ptr] = j
            ptr += 1
        size = ptr
        j = half(sqrt)
        k = sqrt // i - 1 | 1
        while k >= i:
            c = small[k >> 1] - pi
            e = k * i >> 1
            while j >= e:
                small[j] -= c
                j -= 1
            k -= 2
        pi += 1

    large[0] += (size + ((pi - 1) << 1)) * (size - 1) >> 1
    large[0] -= sum(large[1:size])
    for k in range(1, size):
        q = unsieved_nums[k]
        n_q = n // q
        e = small[half(n_q // q)] - pi
        if e < k + 1:
            break
        t = sum(small[half(n_q // unsieved_nums[l + 1])] for l in range(k, e))
        large[0] += t - (e - k) * (pi + k - 1)

    return large[0] + 1


# mypy: ignore-errors
def prime_pi_fast_optimized_np(n: int) -> int:
    import numpy as np

    if n < 2:
        return 0
    if n == 2:
        return 1

    def half(i: int) -> int:
        return (i - 1) >> 1

    sqrt = floor_sqrt(n)
    size = (sqrt + 1) >> 1
    small = np.arange(size)
    large = half(n // (np.arange(size) << 1 | 1))
    unsieved_nums = np.arange(size) << 1 | 1
    checked_or_sieved = np.zeros(size, np.bool8)
    pi = 0
    for i in range(3, sqrt + 1, 2):
        half_i = half(i)
        if checked_or_sieved[half_i]:
            continue
        i2 = i * i
        if i2 * i2 > n:
            break
        checked_or_sieved[half_i] = True
        checked_or_sieved[half(np.arange(i2, sqrt + 1, i << 1))] = True
        k = np.arange(size)
        j = unsieved_nums[k]
        k = k[~checked_or_sieved[half(j)]]
        j = j[k]

        size = k.size
        border = j * i
        flg = border <= sqrt
        x = np.empty(size, np.int64)
        x[flg] = large[small[border[flg] >> 1] - pi]
        x[~flg] = small[half(n // border[~flg])]
        large[:size] = large[k] - x + pi
        unsieved_nums[:size] = j

        j = half(sqrt)
        for k in range(sqrt // i - 1 | 1, i - 1, -2):
            c = small[k >> 1] - pi
            e = k * i >> 1
            small[e : j + 1] -= c
            j = e - 1

        pi += 1

    large[0] += (size + ((pi - 1) << 1)) * (size - 1) >> 1
    large[0] -= large[1:size].sum()

    k = np.arange(1, size)
    q = unsieved_nums[k]
    n_q = n // q
    e = small[half(n_q // q)] - pi
    t = np.array(
        [
            np.sum(small[half(n_q[j] // unsieved_nums[np.arange(k[j] + 1, e[j] + 1)])])
            for j in range(size - 1)
            if e[j] >= k[j] + 1
        ]
    )
    s = t.size
    large[0] += np.sum(t - (e - k)[:s] * (pi + k - 1)[:s])
    return large[0] + 1


def sieve_of_eratosthenes(sieve_size: int) -> list[int]:
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


def prime_pi_table(size: int) -> list[int]:
    pi = [0] * size
    for p in sieve_of_eratosthenes(size):
        pi[p] = 1
    for i in range(size - 1):
        pi[i + 1] += pi[i]
    return pi


import typing

PRIME_PI_POWER_OF_10 = [
    0,
    4,
    25,
    168,
    1229,
    9592,
    78498,
    664579,
    5761455,
    50847534,
    455052511,
    4118054813,
    37607912018,
    346065536839,
    3204941750802,
    29844570422669,
    279238341033925,
    2623557157654233,
    24739954287740860,
    234057667276344607,
    2220819602560918840,
    21127269486018731928,
    201467286689315906290,
]


def test_fast_prime_counting(pi: typing.Callable[[int], int]) -> None:
    N = 1 << 10
    ans = prime_pi_table(N)
    for i in range(N):
        assert pi(i) == ans[i]

    for i in range(11):
        assert pi(10**i) == PRIME_PI_POWER_OF_10[i]


test_fast_prime_counting(prime_pi_fast_optimized_np)
test_fast_prime_counting(prime_pi_fast_optimized)
test_fast_prime_counting(prime_pi_fast)


def main() -> None:
    ...
    # n = int(input())
    # # print(prime_pi_fast(n))
    # print(prime_pi_fast_optimized(n))
    # # print(prime_pi_fast_optimized_np(n))


if __name__ == "__main__":
    main()
