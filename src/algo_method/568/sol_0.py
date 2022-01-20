import typing 

def main() -> None:
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(sum(a) * m + sum(b) * n)

main()