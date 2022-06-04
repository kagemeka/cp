import sys
sys.set_recursionlimit(1 << 20)


def main() -> None:
    n, x = map(int, input().split())
    # if not x?, then 4, 5, 3, 6, 2, 7, 1, 8 for example (n = 8).

    # graph dfs?

    visited = [False] * n
    def dfs(u: int, length: int) -> None:
        ...



if __name__ == "__main__":
    main()
