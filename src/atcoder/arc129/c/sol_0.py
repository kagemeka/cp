import typing 
import bisect



def main() -> typing.NoReturn:
    n = int(input())
    a = [i * (i + 1) // 2 for i in range(1, 10000)]
    s = []
    n0 = n
    while n:
        i = bisect.bisect_right(a, n)
        n -= a[i - 1]
        s.append('7' * i)
    s = '1'.join(s)
    print(s)

    cnt = 0
    for l in range(len(s)):
        for r in range(l + 1, len(s) + 1):
            if int(s[l:r]) % 7 == 0:
                cnt += 1
                assert not '1' in s[l:r]
    print(cnt)



main()