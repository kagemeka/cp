# broken life


def solve() -> None:
    n, m = map(int, input().split())
    s = list(input())
    a = input()

    # dp
    # at most how much same

    dp = [0] * (n + 1)
    dp[0] == 0
    for i in range(n):
        j = dp[i]
        if s[i] == "?":
            if a[j] == "a":
                s[i] = "b"
            else:
                s[i] = "a"
            dp[i + 1] = dp[i]
        else:
            dp[i + 1] = dp[i] + (a[j] == s[i])
        if dp[i + 1] == m:
            print(-1)
            return
    print("".join(s))


def main() -> None:
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
