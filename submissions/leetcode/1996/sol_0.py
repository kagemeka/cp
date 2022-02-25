import typing
import numpy as np


class Solution:
  def numberOfWeakCharacters(
    self,
    a: typing.List[typing.List[int]],
  ) -> int:
    inf = 1 << 30
    a.append([inf, -1])
    a, d = np.array(a).T
    sort_idx = np.argsort(a, kind='mergesort')
    a, d = a[sort_idx], d[sort_idx]
    cum_mx_d = np.maximum.accumulate(d[::-1], axis=0)[::-1]
    idx = np.searchsorted(a, a[:-1], side='right')
    tot = cum_mx_d[idx] > d[:-1]
    return tot.sum()
