import typing
import copy


def main() -> None:
    n, m = map(int, input().split())
    MOD = 998_244_353
    K = 3
    dp = [[0] * (m + 1) for _ in range(K + 1)]
    dp[0][0] = 1
    for _ in range(n):
        ndp = [[0] * (m + 1) for _ in range(K + 1)]
        ndp[0][0] = 1
        for i in range(1, K + 1):  # length of lis in ndp.
            for j in range(1, m + 1):  # last element in ndp.
                if j < i:
                    continue
                ndp[i][j] += dp[i][j] * (j if j >= 1 else 0) % MOD
                for k in range(i - 1, j):
                    ndp[i][j] += dp[i - 1][k]
                    ndp[i][j] %= MOD
        dp = ndp
        print(dp)


if __name__ == "__main__":
    main()
