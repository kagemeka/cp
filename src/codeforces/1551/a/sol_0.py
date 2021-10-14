def main():
  t = int(input())
  for _ in range(t):
    n = int(input())
    q, r = divmod(n, 3)
    x = y = q 
    if r == 0: pass 
    elif r == 1: x += 1
    else: y += 1
    print(x, y)


main()
    