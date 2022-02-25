import typing


def solve() -> typing.NoReturn:
    a, s = map(int, input().split())
    b = []
    while a:
        x = a % 10
        y = s % 10
        if y >= x:
            b.append(y - x)
            a //= 10
            s //= 10
            continue
        else:
            y = s % 100
            d = y - x
            if not 0 < d < 10:
                print(-1)
                return
            b.append(d)
            a //= 10
            s //= 100
    b.append(s)
    b = ''.join(map(str, b[::-1]))
    print(int(b))

def main() -> typing.NoReturn:
    t = int(input())
    for _ in range(t):
        solve()

main()
