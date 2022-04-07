# non adjacent flips 

def main() -> None:
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        if s.count('1') == 0:
            print(0)
            continue
        for i in range(n - 1):
            if s[i] == s[i + 1] == '1':
                print(2)
                break
        else:
            print(1)


if __name__ == "__main__":
    main()
