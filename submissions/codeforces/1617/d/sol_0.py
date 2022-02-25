import typing 
import sys

def solve(last: bool) -> typing.NoReturn:
    n = int(input())
    res0 = [-1] * n
    res1 = [-1] * n
    for i in range(n):
        a = i + 1
        b = (i + 2) % n
        if b == 0: b += n
        c = (i + 3) % n
        if c == 0: c += n
        assert a != b and b != c and c != a
        s = f'? {a} {b} {c}'
        print(s, flush=True)
        v = int(input())
        if v == -1:
            raise
        res0[i] = v
        b = c
        c = (i + 4) % n
        if c == 0: c += n
        assert a != b and b != c and c != a
        s = f'? {a} {b} {c}'
        print(s, flush=True)
        v = int(input())
        if v == -1:
            raise
        res1[i] = v
    res = [-1] * n
    uncertain = [False] * n
    for i in range(n):
        if res0[(i + 1) % n] == 0:
            if res0[i] == 1 or res1[i] == 1:
                res[i] = 1
            else:
                res[i] = 0
                uncertain[i] = True
        else:
            if res0[i] == 0 or res1[i] == 0:
                res[i] = 0
            else:
                res[i] = 1
                uncertain[i] = True
    
    res = [i + 1 for i in range(n) if res[i] == 0 and not uncertain[i]]
    k = len(res)
    if k <= n // 3:
        for i in range(n):
            if res[i] == 0 and uncertain[i]:
                res.append(i + 1)
                k += 1
            if k > n // 3: break
        else:
        # if k <= n // 3:
            for i in range(n):
                if res[i] == 1 and uncertain[i]:
                    res.append(i + 1)
                    k += 1
                if k > n // 3: break
    # elif k >= n // 3 * 2:
        
        
    res = ' '.join(map(str, res))
    s = f'! {k} {res}'
    if last:
        print(s)
    else:
        print(s, flush=True)

             

def main() -> typing.NoReturn:
    t = int(input())
    for i in range(t):
        solve(last=i == t - 1)
    # print()

main()