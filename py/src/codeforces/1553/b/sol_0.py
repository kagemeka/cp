import typing
import sys
sys.setrecursionlimit(1 << 20)



def solve(
  s: str,
  t: str,
) -> typing.NoReturn:

  def dfs(
    i: int,
    j: int,
    d: int,
  ) -> bool:
    if j == len(t):
      return True
    if i < 0 or len(s) <= i:
      return False
    if s[i] != t[j]:
      return False
    ok = dfs(i - 1, j + 1, 0)
    if d == 0: return ok
    ok |= dfs(i + 1, j + 1, 1)
    return ok
  
  for i in range(len(s)):
    ok = dfs(i, 0, 1)
    if ok: print('YES'); break
  else:
    print('NO')
    
  

def main() -> typing.NoReturn:
  q = int(input())
  for _ in range(q):
    s = input()
    t = input()
    solve(s, t)


main()