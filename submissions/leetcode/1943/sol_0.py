import typing
import numpy as np

from typing import List


class Solution:
  def splitPainting(
    self,
    segments: List[List[int]],
  ) -> List[List[int]]:
    n = 1 << 17
    s = np.zeros(
      n,
      dtype=np.int64,
    )
    l, r, c = np.array(
      segments,
    ).T
    np.add.at(s, l, c)
    np.add.at(s, r, -c)
    np.cumsum(s, out=s)
    b = sorted(
      set(l) | set(r),
    )
    b = np.array(b)
    l = b[:-1]
    r = b[1:]
    c = s[l]
    i = np.argwhere(c != 0)
    i = i.ravel()
    res = zip(l[i], r[i], c[i])
    res = [
      [l, r, c]
      for l, r, c in res
    ]
    return res
