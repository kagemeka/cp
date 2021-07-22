import typing 
import sys





def solve(
  s: str,
  t: str,
) -> typing.NoReturn:
  i = j = 0 
  n, m = len(s), len(t)
  w = ''
  while 1:
    # if j == m:
    #   print('YES')
    #   return
    ri, rj = n - i, m - j
    if ri < rj:
      print('NO')
      return 
    if (ri - rj) & 1:
      i += 1
      continue
    if j == m:
      print(
        'YES' if w == t
        else 'NO',
      )
      return 
    if s[i] == t[j]:
      j += 1
      w += s[i]
    i += 1
    

      

    


def main():
  q = int(input())
  for _ in range(q):
    s = input()
    t = input()
    solve(s, t)


main()