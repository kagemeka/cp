from collections import (
  Counter,
)


def main():
  t = int(input())
  for _ in range(t):
    s = input()
    c = Counter(s)
    c = Counter(c.values())
    for x in range(3, 51):
      c[2] += c[x]
    c[2] += c[1] // 2 
    print(c[2])


main()