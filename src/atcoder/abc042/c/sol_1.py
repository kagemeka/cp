import sys 
import string
import itertools 
from bisect import bisect_left as bi_l

n, k, *d = sys.stdin.read().split()
l = len(n)
ok = sorted(set(string.digits)-set(d))
cand = [int(''.join(p)) for p in itertools.product(ok, repeat=l)] + [int(min(x for x in ok if x > '0')+min(ok)*l)]
print(cand[bi_l(cand, int(n))])
