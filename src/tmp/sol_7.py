def main() -> None:
    n, k = map(int, input().split())
    if 2 <= k == n:
        print("No")
        return

    if n == 1:
        print("Yes")

    # if k == 1
    # change bit sequence as follows
    # 0 -> 1(2^1 th) -> 0 -> 2(2^2 th) -> 0 -> 1 -> 0 -> 3(2^3 th)
    # -> 0 -> 1 -> 0 -> 2 -> 0 -> 1 -> 0 -> 4(2^4 th)
    # -> 0 -> 1 -> 0 -> 2 -> 0 -> 1 -> 0 -> 3 -> ...

    # 0 -> 1 -> 3 -> 2 -> 6 -> 7 -> 5 -> 4 -> 12 -> 13 -> 15
    # -> 14 -> 10 -> 11 -> 9 -> 8 -> 16 -> 17 -> 19 -> 18 -> 22
    # -> 23 -> 25 ...

    # if k == 2
    # 0 -> 3 -> 6 -> 5 -> 12 -> 15 -> 10 -> 13 -> 4 -> 7 -> 2 -> 1 -> 16 -> 19
    # -> ...

    # k == 3
    # 0 -> 7 -> 12 -> 11 ->


    # k == 1
    # change 0th bit per 2 turn
    # change 1th bit per 4 turn
    # change 2nd bit per 8 turn
    # change 3rd bit per 16 turn

    # if k >= 2
    # change 0th bit per turn
    # change 1th bit per 2 turn
    # change 2nd bit per 4 turn
    # change 3rd bit per 8 turn
    # ...

    sequence = []
    x = 0
    for i in range(1 << n):


    # if k == 1:
    #     ...
    #     return


if __name__ == "__main__":
    main()
