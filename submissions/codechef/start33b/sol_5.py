# max bit sum


def solve() -> None:
    ...

    # split cases by msb.
    # compute all pairs ^ sum
    # subtract & sum

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    k = 20
    cnt_a_by_bitlength = [[0] * k for _ in range(k + 1)]
    cnt_b_by_bitlength = [[0] * k for _ in range(k + 1)]

    cnt_a = [0] * k
    cnt_b = [0] * k

    cnt_a_length = [0] * (k + 1)
    cnt_b_length = [0] * (k + 1)

    for x in a:
        l = x.bit_length()
        cnt_a_length[l] += 1
        for i in range(k):
            cnt_a_by_bitlength[l][i] += x >> i & 1
            cnt_a[i] += x >> i & 1

    for x in b:
        l = x.bit_length()
        cnt_b_length[l] += 1
        for i in range(k):
            cnt_b_by_bitlength[l][i] += x >> i & 1
            cnt_b[i] += x >> i & 1

    tot = 0
    for i in range(k):
        tot += (1 << i) * (cnt_a[i] * (n - cnt_b[i]) + cnt_b[i] * (n - cnt_a[i]))

    for l in range(k + 1):
        for i in range(k):
            tot -= (1 << i) * (
                cnt_a_by_bitlength[l][i] * (cnt_b_length[l] - cnt_b_by_bitlength[l][i])
                + cnt_b_by_bitlength[l][i]
                * (cnt_a_length[l] - cnt_a_by_bitlength[l][i])
            )
            tot += (1 << i) * (cnt_a_by_bitlength[l][i] * cnt_b_by_bitlength[l][i])
    print(tot)


def main() -> None:
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
