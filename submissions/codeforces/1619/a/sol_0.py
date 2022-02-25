import typing


def main() -> typing.NoReturn:
    t = int(input())
    for _ in range(t):
        s = input()
        n = len(s)
        if n & 1:
            print('NO')
            continue
        print('YES' if s[:n // 2] == s[n // 2:] else 'NO')


main()
