# growing rivalry


def main() -> None:
    n = int(input())
    print("Alice" if input().count("A") > n // 2 else "Bob")


main()
