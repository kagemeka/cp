import typing 


def main() -> typing.NoReturn:
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(1 if sum(a) % n else 0)
    
main()