def solve() -> None:
    n = int(input())
    parent = [-1] + list(map(lambda x: int(x) - 1, input().split()))

    child_count = [0] * n
    for i in range(n):
        if parent[i] != -1:
            child_count[parent[i]] += 1

    child_count.sort(reverse=True)

    def possible(t: int) -> bool:
        rem = t
        rem -= 1  # for root, at last
        # for others than root
        for turn in range(n):
            if child_count[turn] == 0:
                break
            if child_count[turn] > t - turn:
                rem -= child_count[turn] - (t - turn)
            rem -= 1
        return rem >= 0

    def binary_search() -> int:
        lo, hi = 1, n  # impossible, possible
        while hi - lo > 1:
            t = (lo + hi) >> 1
            if possible(t):
                hi = t
            else:
                lo = t
        return hi

    print(binary_search())


def main() -> None:
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
