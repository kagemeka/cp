import typing 
import sys 
import numpy as np




q = np.empty(
  (1 << 20, 3),
  dtype=np.int64,
)
qn = 0
def swap(i, j):
  tmp = q[i].copy()
  q[i] = q[j]
  q[j] = tmp


def heappush(
  h: typing.List,
  x: typing.Any,
) -> typing.NoReturn:
  i = qn
  q[i] = x
  while i > 0:
    j = (i - 1) // 2
    if q[i][0] >= q[j][0]:
      break
    swap(i, j)
    i = j


def heappop():
  n = qn - 1
  swap(0, n)
  i = 0
  while 1:
    j = i * 2 + 1
    if j >= n: break
    dj = q[j, 0]
    if j < n - 1:
      j += q[j + 1][0] < q[j][0]
    dj = q[j][0]
    if q[i][0] <= dj: break
    swap(i, j)
    i = j
  return q[n]



def solve(
  l: np.ndarray,
  r: np.ndarray,
) -> typing.NoReturn:
  n = l.size
  idx = np.argsort(l)
  l = l[idx]
  r = r[idx]


  h = []
  i, j = 0, 1
  for _ in range(n):
    if i < n and l[i] == j:
      while i < n and l[i] == j:
        heapq.heappush(h, r[i])
        i += 1
    elif not h:
      j = l[i] 
      while i < n and l[i] == j:
        heapq.heappush(h, r[i])
        i += 1
    if heapq.heappop(h) < j:
      print('No')
      return 
    j += 1
  print('Yes')
    

def main() -> typing.NoReturn:
  t = int(input())
  
  for _ in range(t):
    n = int(input())
    lr = [
      [int(x) for x in sys.stdin.readline().split()]
      for _ in range(n)
    ]
    l, r = np.array(lr).T
    solve(l, r)


main()