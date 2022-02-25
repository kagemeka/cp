import typing

def main() -> typing.NoReturn:
    t = int(input())
    # freedom, unfreedom
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = [0] * (n + 1)
        c = [0] * (n + 1)
        for x in a:
            if x <= n:
                b[x] += 1
            else:
                c[min((x + 1) // 2 - 1, n)] += 1
        cnt = 0
        for i in range(n, 0, -1):
            if b[i] >= 1:
                c[(i + 1) // 2 - 1] += b[i] - 1
                c[i - 1] += c[i]
                continue
            elif c[i] >= 1:
                c[i - 1] += c[i] - 1
                cnt += 1
                continue
            print(-1)
            break
        else:
            print(cnt)

main()
