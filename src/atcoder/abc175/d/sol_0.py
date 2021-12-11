import typing 


def main() -> typing.NoReturn:
    n, k = map(int, input().split())
    p = list(map(lambda x: int(x) - 1, input().split()))
    c = list(map(int, input().split()))
    inf = 1 << 60
    for i in range(n):
        