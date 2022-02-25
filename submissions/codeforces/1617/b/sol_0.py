import typing 

def main() -> typing.NoReturn:
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n % 2 == 0:
            c = 1
            n -= 1
            a, b = (n + 1) // 2, n // 2
        else:
            c = 1
            n -= 1
            h = n // 2
            if h & 1:
                a, b = h + 2, h - 2
            else:
                a, b = h + 1, h - 1
        print(a, b, c)
    
main()