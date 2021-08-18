import typing 
import numpy as np
import sys


def sa_is(
  a: np.array,
) -> np.array:
  if a.min() <= 0: a += 1
  assert np.all(a > 0)
  a = np.hstack((a, np.array([0])))
  n, m = a.size, a.max() + 1

  is_s = np.ones(n, dtype=np.bool8)
  for i in range(n - 1, 0, -1):
    is_s[i - 1] = (
      is_s[i] if a[i - 1] == a[i] else
      a[i - 1] < a[i] 
    )
  is_lms = np.zeros(n, dtype=np.bool8)
  # is_lms[np.arange(1, n)[~is_s[:-1] & is_s[1:]]] = True
  for i in range(1, n):
    is_lms[i] = is_s[i] & ~is_s[i - 1]
  lms = np.flatnonzero(is_lms)

  b = np.zeros(m, dtype=np.int64)
  for x in a: b[x] += 1

  # def _induce():
  sa = np.full(n, -1, dtype=np.int64)
  sa_idx = b.cumsum()
  for i in lms[::-1]:
    x = a[i]
    sa_idx[x] -= 1
    sa[sa_idx[x]] = i
  
  sa_idx = b.copy()
  s = 0 
  for i in range(m):
    s, sa_idx[i] = s + sa_idx[i], s
  for i in range(n):
    i = sa[i] - 1
    if i < 0 or is_s[i]: continue
    x = a[i]
    sa[sa_idx[x]] = i
    sa_idx[x] += 1

  sa_idx = b.cumsum()
  for i in range(n - 1, -1, -1):
    i = sa[i] - 1
    if i < 0 or not is_s[i]: continue
    x = a[i]
    sa_idx[x] -= 1
    sa[sa_idx[x]] = i

    # return sa


  # sa = _induce()


  # def _correct_lms_order():
  #   nonlocal lms
  lms_idx = sa[is_lms[sa]]
  l = lms_idx.size
  na = np.full(n, -1, dtype=np.int64)
  na[-1] = i = 1
  for j in range(l - 1):
    j, k = lms_idx[j], lms_idx[j + 1]
    for d in range(n):
      j_is_lms = is_lms[j + d]
      k_is_lms = is_lms[k + d]
      if a[j + d] != a[k + d] or j_is_lms ^ k_is_lms: 
        i += 1; break
      if d > 0 and j_is_lms | k_is_lms: break
    na[k] = i
  na = na[na > 0]
  if i == l:
    lms_order = np.full(l, -1, dtype=np.int64)
    for i in range(l):
      lms_order[na[i] - 1] = i
  else:
    lms_order = sa_is(na)
  lms = lms[lms_order]


  # _correct_lms_order()
  # sa = _induce()
  sa = np.full(n, -1, dtype=np.int64)
  sa_idx = b.cumsum()
  for i in lms[::-1]:
    x = a[i]
    sa_idx[x] -= 1
    sa[sa_idx[x]] = i
  
  sa_idx = b.copy()
  s = 0 
  for i in range(m):
    s, sa_idx[i] = s + sa_idx[i], s
  for i in range(n):
    i = sa[i] - 1
    if i < 0 or is_s[i]: continue
    x = a[i]
    sa[sa_idx[x]] = i
    sa_idx[x] += 1

  sa_idx = b.cumsum()
  for i in range(n - 1, -1, -1):
    i = sa[i] - 1
    if i < 0 or not is_s[i]: continue
    x = a[i]
    sa_idx[x] -= 1
    sa[sa_idx[x]] = i

  return sa[1:]


def kasai(
  a: np.array,
  sa: np.array,
) -> np.array:
  n = a.size
  assert n > 0 and sa.size == n
  rank = np.zeros(n, dtype=np.int64)
  rank[sa] = np.arange(n)
  h = np.zeros(n - 1, dtype=np.int64)
  l = 0
  for i in range(n):
    if l > 0: l -= 1
    r = rank[i]
    if r == n - 1: continue
    j = sa[r + 1]
    while i + l < n and j + l < n:
      if a[i + l] != a[j + l]: break 
      l += 1
    h[r] = l
  return h

  
def solve(
  a: np.array,
) -> typing.NoReturn:
  n = a.size
  sa = sa_is(a)
  lcp = kasai(a, sa)

  a = np.arange(n, 0, -1)
  for i in range(2):
    s = 0 
    st = []
    for i in range(n - 1):
      h = lcp[i]
      l = 1
      while st and st[-1][0] >= h:
        x = st.pop()
        l += x[1]
        s -= x[0] * x[1]
      s += h * l
      st.append((h, l))
      a[sa[i + 1]] += s
    sa = sa[::-1]
    lcp = lcp[::-1]

  for i in range(n):
    print(a[i])



def main() -> typing.NoReturn:
  n = int(sys.stdin.buffer.readline().rstrip())
  a = np.frombuffer(
    sys.stdin.buffer.readline().rstrip(),
    dtype='b',
  ).astype(np.int64) - ord(b'a')
  solve(a)


if sys.argv[-1] == 'ONLINE_JUDGE':
  from numba import njit, i8
  from numba.pycc import CC 
  cc = CC('my_module')
  sa_is = njit(sa_is)
  kasai = njit(kasai)

  fn = solve
  sig = (i8[:], )

  cc.export(
    fn.__name__,
    sig,
  )(fn)

  cc.compile()
  exit(0)


from my_module import solve 
main()