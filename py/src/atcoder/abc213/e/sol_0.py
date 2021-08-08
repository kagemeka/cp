import typing 



def main() -> typing.NoReturn:
  h, w = map(
    int, input().split(),
  )
  s = [
    input()
    for _ in range(h)
  ]
  
  def dfs(i, j, pi, pj) -> int:
    if i == j == 0:
      return 0
    c = s[i][j]
    if c == '#':
      mn = 1 << 30
      for di in range(-2, 3):
        for dj in range(-2, 3):
          if abs(di) + abs(dj) == 4:
            continue
          if di == dj == 0:
            continue
          ni = i + di
          nj = j + dj
          if ni == pi and nj == pj:
            continue
          if ni < 0 or ni >= h or nj < 0 or nj >= w: continue 
          mn = min(mn, dfs(ni, nj, i, j) + 1)
      return mn
    else:
      mn = 1 << 30
      for di, dj in (
        (-1, 0), (1, 0), (0, -1), (0, 1),
      ): 
        ni = i + di
        nj = j + dj
        if ni == pi and nj == pj:
          continue
        if ni < 0 or ni >= h or nj < 0 or nj >= w: continue 
        mn = min(mn, dfs(ni, nj, i, j) + 1)
        return mn
      ... 
    
  

  print(dfs(
    h - 1, w - 1, 
    None, None,
  ))




main()
