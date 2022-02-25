import typing 


class Solution:
  def maxProduct(
    self, 
    s0: str,
  ) -> int:
    n = len(s0)
    
    res = 0 
    for u0 in range(1 << n):
      t0 = ''
      s1 = ''
      for i in range(n):
        if u0 >> i & 1:
          t0 += s0[i]
        else:
          s1 += s0[i]
        if t0 != t0[::-1]: continue
        m = len(s1)
        for u1 in range(1 << m):
          t1 = ''
          for j in range(m):
            if ~u1 >> j & 1: continue 
            t1 += s1[j]
          if t1 != t1[::-1]: continue
          res = max(res, len(t0) * len(t1))
    return res 


# s = input()
# Solution().maxProduct(s)