def main() -> None:
    MOD = 32768

    # bfs
    count = [-1] * MOD
    count[0] = 0

    for j in range(100):
        que = []
        for i in range(MOD):
            if count[i] != -1:
                continue
            if count[(i + 1) % MOD] != -1 or count[i * 2 % MOD] != -1:
                que.append(i)
        for i in que:
            count[i] = j + 1

    n = int(input())

    a = list(map(int, input().split()))
    res = [count[x] for x in a]
    print(*res)


if __name__ == "__main__":
    main()
