import typing 
import sys 



def main() -> typing.NoReturn:
    s = list(input())
    k = int(input())
    n = len(s)
    a = set()
    a.add(tuple(s))
    for _ in range(min(k, 1000)):
        b = set()
        for t in a:
            t = list(t)
            for i in range(n - 1):
                t[i], t[i + 1] = t[i + 1], t[i]
                b.add(tuple(t))
                t[i], t[i + 1] = t[i + 1], t[i]
        a |= b 
    print(len(a))


main() 