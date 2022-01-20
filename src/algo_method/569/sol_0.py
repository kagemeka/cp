import typing 


def main() -> None:
    n = int(input())
    
    a = list(range(1, n + 1))
    a2 = [x ** 2 for x in a]
    s = sum(a)
    
    print((s ** 2 - sum(a2)) // 2)

main()