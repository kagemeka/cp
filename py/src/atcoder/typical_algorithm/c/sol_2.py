import typing 


class TSP():
  def __call__(
    self,
    g: typing.List[typing.List[int]],
    src: int,
  ) -> int:
    n = len(g)
    assert len(g[0]) == n
    inf = 1 << 60
    assert inf > sum(map(sum, g))
    dist = [[inf] * n for _ in range(1 << n)]
    dist[1 << src][src] = 0 
    for s in range(1 << n):
      for i in range(n):
        if ~s >> i & 1: continue
        for j in range(n):
          if s >> j & 1: continue
          u = s | 1 << j 
          dist[u][j] = min(
            dist[u][j], 
            dist[s][i] + g[i][j],
          )
    return min(
      dist[-1][i] + g[i][src] 
      for i in range(n)
    )



def solve(
  a: typing.List[typing.List[int]],
) -> typing.NoReturn:
  print(TSP()(a, 0))


def main() -> typing.NoReturn:
  n = int(input())
  a = [
    list(map(int, input().split()))
    for _ in range(n)
  ]
  solve(a)


main()


