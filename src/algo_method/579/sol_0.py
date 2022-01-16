import typing 


def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    
    p = 1
    for x in a:
        p = p * x % 10
    
    print(p)

main()