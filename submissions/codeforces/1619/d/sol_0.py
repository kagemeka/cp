    import typing


    def solve() -> typing.NoReturn:
        m, n = map(int, input().split())
        p = [list(map(int, input().split())) for _ in range(m)]


        def possible(x: int) -> bool:
            ok = [False] * n
            ok2 = False
            for i in range(m):
                cnt = 0
                for j in range(n):
                    ok[j] |= p[i][j] >= x
                    cnt += p[i][j] >= x
                ok2 |= cnt >= 2
            return all(ok) and ok2

        def binary_search() -> int:
            lo, hi = 0, 1 << 30
            while hi - lo > 1:
                x = (lo + hi) >> 1
                if possible(x):
                    lo = x
                else:
                    hi = x
            return lo
        print(binary_search())


    def main() -> typing.NoReturn:
        t = int(input())
        for _ in range(t):
            input()
            solve()

    main()
