def main() -> None:
    # for each pair of cells, how many times the pair would be choosed?
    # compute pairs altogether by their distance.
    # (n * m) choose (k - 2) \sum_d{count_pairs(d) * d}

    # inclusion exclusion principle
    n, m, k = map(int, input().split())

    K = 1 << 18
    fact = list(range(K))
    fact[0] = 1
    MOD = 10**9 + 7
    for i in range(K - 1):
        fact[i + 1] = fact[i] * fact[i + 1] % MOD

    ifact = list(range(1, K + 1))
    ifact[-1] = pow(fact[-1], -1, MOD)
    for i in range(K - 1, 0, -1):
        ifact[i - 1] = ifact[i - 1] * ifact[i] % MOD

    def choose(n: int, k: int) -> int:
        if not 0 <= k <= n:
            return 0

        return fact[n] * ifact[k] % MOD * ifact[n - k] % MOD

    # i * min(d - i, n)
    # \sum_i=1^{d-1} {min(i, n) * min(d - i, m)}
    
    a = [min(i, n) * min(
    tot = 0
    for d in range(1, K):
        count = 0
        count += n * m * 4 * d
        # nd = min(d, n)
        # md = min(d, n)
        count -= 2 * (min(d, n) * m + min(d, m) * n)
        count -= 2 * 2 * (
            (1 + min(d - 1, n)) * min(d - 1, n) // 2 * m
            + (1 + min(d - 1, m)) * min(d - 1, m) // 2 * n
        )
        


if __name__ == "__main__":
    main()
