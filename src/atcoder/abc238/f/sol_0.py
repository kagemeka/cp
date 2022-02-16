import typing


def main() -> None:
    n, k = map(int, input().split())
    p = list(map(lambda x: int(x) - 1, input().split()))
    q = list(map(lambda x: int(x) - 1, input().split()))
    MOD = 998_244_353
    
    # O(NK)
    
    dp = [0] * (k + 1)
    dp[0] = 1
    


if __name__ == "__main__":
    main()
