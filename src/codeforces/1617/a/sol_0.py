import typing 
import collections 
import string

def main() -> typing.NoReturn:
    t = int(input())
    for _ in range(t):
        a = input()
        b = input()
        alp = list(string.ascii_lowercase)
        if b == 'abc' and 'a' in a:
            alp[1], alp[2] = alp[2], alp[1]
        cnt = collections.Counter(a)
        res = ''
        for x in alp:
            res += cnt[x] * x
        print(res)

main()
            