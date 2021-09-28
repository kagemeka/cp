from scipy.sparse.csgraph import (
  maximum_flow, 
)
from scipy.spatial import ConvexHull
from scipy import optimize
from scipy.special import comb
import networkx as nx
    



  
  class ABC022:
    @staticmethod 
    def a():
      n, s, t, *a = map(int, sys.stdin.read().split())
      a = np.array(a)
      np.cumsum(a, out=a)
      print(((s<=a) & (a<=t)).sum())

    @staticmethod 
    def b():
      n, *a = map(int, sys.stdin.read().split())
      c = Counter(a)
      print(sum(c.values())-len(c))

    @staticmethod
    def c():
      n, m, *uvl = map(int, sys.stdin.read().split())
      u, v, l = np.array(uvl).reshape(m, 3).T
      u -= 1; v -= 1 
      g = csgraph_to_dense(csr_matrix((l, (u,v)), (n,n)))
      g += g.T
      g[g==0] = np.inf
      dist0 = g[0].copy()
      g[0] = 0; g[:, 0] = 0
      dist = shortest_path(g, method='FW', directed=False)
      u, v = np.array([*itertools.combinations(range(1,n), 2)]).T 
      res = (dist0[u]+dist[u,v]+dist0[v]).min()
      print(-1 if res==np.inf else int(res))
    


  class ABC023:
    @staticmethod 
    def a():
      print(sum(divmod(int(sys.stdin.readline().rstrip()), 10)))

    @staticmethod 
    def b():
      n, s = sys.stdin.read().split()
      n = int(n)
      t = 'b'
      for i in range(n//2):
        if i%3==0: t = 'a'+t+'c'
        elif i%3==1: t = 'c'+t+'a'
        else: t = 'b'+t+'b'
      print(n//2 if t==s else -1)
    
    @staticmethod 
    def b_2():
      n, s = sys.stdin.read().split() 
      n = int(n)
      if n&1^1: print(-1); return 
      a = list('abc')
      i = (1-n//2)%3
      for c in s:
        if c != a[i]:
          print(-1); return 
        i = (i+1) % 3
      print(n//2)

    @staticmethod 
    def c():
      h, w, k, n, *rc = map(int, sys.stdin.read().split())
      r, c = np.array(rc).reshape(n,2).T - 1
      rb = np.bincount(r, minlength=h)
      cb = np.bincount(c, minlength=w)
      rbb = np.bincount(rb, minlength=k+1)
      cbb = np.bincount(cb, minlength=k+1)
      tot = (rbb[:k+1]*cbb[k::-1]).sum()
      real = np.bincount(rb[r]+cb[c]-1, minlength=k+1)
      print(tot-real[k-1]+real[k])


  class ABC024:
    @staticmethod 
    def a():
      a, b, c, k, s, t = map(int, sys.stdin.read().split())
      print(a*s + b*t - c*(s+t)*(s+t>=k)) 

    @staticmethod 
    def b():
      n, t, *a = map(int, sys.stdin.read().split())
      a = np.array(a)
      print(np.minimum(a[1:]-a[:-1], t).sum() + t)

    @staticmethod 
    def c():
      n, d, k, *lrst = map(int, sys.stdin.read().split())
      lrst = np.array(lrst)
      lr = lrst[:2*d].reshape(d,2) 
      s, t = lrst[2*d:].reshape(k,2).T
      day = np.zeros((k,),dtype=np.int32)
      for i in range(d):
        l, r = lr[i]
        move = (l<=s)&(s<=r)&(s!=t)
        reach = move&(l<=t)&(t<=r)
        s[move&(s<t)] = r 
        s[move&(s>t)] = l
        s[reach] = t[reach]; day[reach] = i+1
      print(*day, sep='\n')



  class ABC025:
    @staticmethod 
    def a():
      s, n = sys.stdin.read().split()
      n = int(n)
      i, j = divmod(n-1, 5)
      print(s[i]+s[j])

    @staticmethod 
    def b():
      n, a, b = map(int, sys.stdin.readline().split())
      res = defaultdict(int)
      for _ in range(n):
        s, d = sys.stdin.readline().split()
        d = int(d)
        res[s] += min(max(d,a),b)
      res = res['East'] - res['West']
      if res == 0: ans = 0 
      elif res > 0: ans = f'East {res}'
      else: ans = f'West {-res}'
      print(ans)

    @staticmethod 
    def c():
      b = [0] * 6
      for i in range(2):
        *row, = map(int, sys.stdin.readline().split())
        for j in range(3):
          b[i*3+j] = row[j]
      c = [0] * 8
      for i in range(3):
        *row, = map(int, sys.stdin.readline().split())
        for j in range(2):
          c[i*3+j] = row[j]
      tot = sum(b) + sum(c) 

      @lru_cache(maxsize=None)
      def f(s=tuple(0 for _ in range(9))):
        if all(s):
          res = 0
          for i in range(6): res += (s[i]==s[i+3])*b[i]
          for i in range(8): res += (s[i]==s[i+1])*c[i]
          return res
        cand = [i for i in range(9) if not s[i]]
        flg = len(cand)&1
        s = list(s)
        res = []
        for i in cand:
          s[i] = (flg^1)+1
          res.append(f(tuple(s)))
          s[i] = 0
        return sorted(res, reverse=flg)[0]

      a = f(); b = tot-a
      print(a)
      print(b)

      

  class ABC026:
    @staticmethod 
    def a():
      a = int(sys.stdin.readline().rstrip())
      print(a//2 * (a-a//2))

    @staticmethod 
    def b():
      n, *r = map(int, sys.stdin.read().split())
      s = np.pi * np.array([0]+r)**2; s.sort()
      res = s[n::-2].sum() - s[n-1::-2].sum()
      print(res)     

    @staticmethod 
    def c():
      n, *b = map(int, sys.stdin.read().split())
      g = GeometryTopology.Graph()
      for i in range(1, n): g.add_edge(b[i-1]-1, i, weight=1)

      def f(u=0):
        if not g.edges[u]: return 1 
        s = [f(v) for v in g.edges[u]]
        return max(s) + min(s) + 1

      print(f())

  
  class ABC027:
    @staticmethod 
    def a():
      l = [int(l) for l in sys.stdin.readline().split()]
      l.sort()
      print(l[2] if l[0]==l[1] else l[0])

    @staticmethod 
    def b():
      n, *a = map(int, sys.stdin.read().split())
      m, r = divmod(sum(a), n)
      if r: print(-1); return 
      population = 0 
      towns = 0
      cnt = 0
      for x in a:
        population += x 
        towns += 1 
        if population/towns != m: cnt+=1; continue 
        population, towns = 0, 0
      print(cnt)

    @staticmethod 
    def c():
      n = int(sys.stdin.readline().rstrip())
      flg = n.bit_length()&1^1
      t = 0
      x = 1
      while x <= n:
        t += 1
        x = 2*x+1 if t&1^flg else 2*x
      print('Aoki' if t&1 else 'Takahashi')
  

  class ABC028:
    @staticmethod
    def a():
      n = int(sys.stdin.readline().rstrip())
      print('Bad' if n<60 else 'Good' if n<90 else 'Great' if n<100 else 'Perfect')

    @staticmethod 
    def b():
      s = sys.stdin.readline().rstrip()
      cnt = Counter(s)
      print(*[cnt.get(c, 0) for c in 'ABCDEF']) 

    @staticmethod 
    def c():
      a, b, c, d, e = map(int, sys.stdin.readline().split())
      print(max(b+c+e, a+d+e))


  class ABC029:
    @staticmethod 
    def a():
      print(sys.stdin.readline().rstrip()+'s')

    @staticmethod 
    def b():
      print(sum('r' in s for s in sys.stdin.read().split()))

    @staticmethod 
    def c():
      print(*[''.join(s) for s in itertools.product('abc', repeat=int(sys.stdin.readline().rstrip()))], sep='\n')


  class ABC030:
    @staticmethod 
    def a():
      a, b, c, d = map(int, sys.stdin.readline().split())
      e, f = b*c, d*a 
      print('TAKAHASHI' if e>f else 'AOKI' if f>e else 'DRAW')
      
    @staticmethod 
    def b():
      n, m = map(int, sys.stdin.readline().split())
      n = (n%12 + m/60)*30; m *= 6
      d = abs(n-m)
      print(min(d, 360-d))

    @staticmethod 
    def c():
      n, m = map(int, sys.stdin.readline().split())
      x, y = map(int, sys.stdin.readline().split())
      a = [int(x) for x in sys.stdin.readline().split()]
      b = [int(x) for x in sys.stdin.readline().split()]

      t = 0
      p = 1
      cnt = 0
      while True:
        if p:
          i = bi_l(a, t)
          if i == n: break 
          t = a[i] + x
        else:
          i = bi_l(b, t)
          if i == m: break 
          t = b[i] + y 
          cnt += 1
        p ^= 1
      print(cnt)
    

  class ABC031:
    @staticmethod 
    def a():
      a, d = map(int, sys.stdin.readline().split())
      if a > d: a,d = d,a
      print((a+1)*d)

    @staticmethod 
    def b():
      l, h, n, *a = map(int, sys.stdin.read().split())
      a = np.array(a)
      res = np.maximum(l-a, 0)
      res[a>h] = -1
      print(*res, sep='\n')

    @staticmethod 
    def c():
      n, *a = map(int, sys.stdin.read().split())
      a = np.array(a)
      np.cumsum(a[::2], out=a[::2])
      np.cumsum(a[1::2], out=a[1::2])
      a = list(a) + [0]*2

      def score(i, j):
        if i > j: i, j = j, i
        if (j-i)&1: x, y = a[j-1]-a[i-2], a[j]-a[i-1]
        else: x, y = a[j]-a[i-2], a[j-1]-a[i-1]
        return x, y

      res = -inf 
      for i in range(n):
        s = -inf
        for j in range(n):
          if i==j: continue
          x, y = score(i, j)
          if y>s: s,t = y,x
        res = max(res, t)
      print(res)

    @staticmethod 
    def d():
      k, m = map(int, sys.stdin.readline().split())
      *vw, = zip(*[iter(sys.stdin.read().split())]*2)
      for l in itertools.product((1,2,3), repeat=k):
        s = dict()
        for v, w in vw:
          i = 0
          for d in v:
            d = int(d)-1
            j = i+l[d]
            if j > len(w): break
            t = w[i:j]
            if d in s and s[d] != t: break 
            s[d] = t 
            i = j
          else: 
            if i == len(w): continue
          break
        else:
          for i in range(k): print(s[i])
          return


  class ABC032:
    @staticmethod
    def a():
      a, b, n = map(int, sys.stdin.read().split())
      l = NumberTheory.lcm(a, b)
      print((n+l-1)//l*l)

    @staticmethod
    def b():
      s, k = sys.stdin.read().split()
      k = int(k)
      res = set()
      for i in range(len(s)-k+1):
        res.add(s[i:i+k])
      print(len(res))

    @staticmethod
    def c():
      n, k, *s = map(int, sys.stdin.read().split())
      if 0 in s: print(n); return 
      if k == 0: print(0); return
      res, tmp, l = 0, 1, 0
      for r in range(n):
        tmp *= s[r]
        while tmp > k: tmp //= s[l]; l+=1
        res = max(res, r-l+1)

      print(res)

  class ABC033:
    @staticmethod
    def a():
      print('SAME' if len(set(sys.stdin.readline().rstrip()))==1 else 'DIFFERENT')

    @staticmethod
    def b():
      n = int(sys.stdin.readline().rstrip())
      res = dict()
      for _ in range(n):
        s, p = sys.stdin.readline().split()
        res[s] = int(p) 
      tot = sum(res.values())
      for s, p in res.items():
        if p > tot/2: print(s); return
      print('atcoder')

    @staticmethod
    def c():
      s = sys.stdin.readline().rstrip()
      print(sum(not '0' in f for f in s.split('+')))
    

  class ABC034:
    @staticmethod
    def a():
      x, y = map(int, sys.stdin.readline().split())
      print('Better' if y>x else 'Worse')

    @staticmethod
    def b():
      n = int(sys.stdin.readline().rstrip())
      print(n+1 if n&1 else n-1)

    @staticmethod
    def c():
      h, w = map(int, sys.stdin.read().split())
      choose = Combinatorics.CombinationsMod()
      print(choose(h+w-2, h-1))

    @staticmethod
    def d():
      n, k, *wp = map(int, sys.stdin.read().split())
      w, p = np.array(wp).reshape(-1, 2).T 
      def f(x):
        return np.sort(w*(p-x))[-k:].sum()
      print(optimize.bisect(f, 0, 100))

  class ABC035:
    @staticmethod
    def a():
      w, h = map(int, sys.stdin.readline().split())
      print('4:3' if 4*h==3*w else '16:9')

    @staticmethod
    def b():
      s, t = sys.stdin.read().split()
      y = x = z = 0
      for c in s:
        if c == '?': z += 1
        elif c == 'L': x -= 1
        elif c == 'R': x += 1
        elif c == 'D': y -= 1
        elif c == 'U': y += 1 
      d = abs(y)+abs(x)
      print(d+z if t=='1' else max(d-z, (d-z)&1))

    @staticmethod
    def c():
      n, q, *lr = map(int, sys.stdin.read().split())
      l, r = np.array(lr).reshape(q, 2).T
      res = np.zeros(n+1, dtype=int)
      np.add.at(res, l-1, 1)
      np.subtract.at(res, r, 1)
      np.cumsum(res, out=res)
      res = res&1
      print(''.join(map(str, res[:-1])))

    @staticmethod
    def d():
      n, m, t = map(int, sys.stdin.readline().split())
      point = np.array(sys.stdin.readline().split(), dtype=int)
      a, b, c = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(m, 3).T 
      a -= 1; b -= 1 
      d_1 = shortest_path(csr_matrix((c, (a, b)), (n, n)), method='D', directed=True, indices=0)
      d_2 = shortest_path(csr_matrix((c, (b, a)), (n, n)), method='D', directed=True, indices=0)
      print(int(np.amax((t-(d_1+d_2))*point)))

  class ABC036:
    @staticmethod
    def a():
      a, b = map(int, sys.stdin.readline().split())
      print((b+a-1)//a)

    @staticmethod
    def b():
      n, *s = sys.stdin.read().split()
      n = int(n)
      for j in range(n):
        row = ''
        for i in range(n-1, -1, -1):
          row += s[i][j]
        print(row)
    
    @staticmethod
    def c():
      n, *a = map(int, sys.stdin.read().split())
      b = [None]*n
      prev = None
      j = -1
      for i, x in sorted(enumerate(a), key=lambda x: x[1]):
        if x != prev: j += 1
        b[i] = j
        prev = x     
      print(*b, sep='\n') 
    
    @staticmethod
    def d():
      n, *ab = map(int, sys.stdin.read().split())
      edges = [[] for _ in range(n)]
      for a, b in zip(*[iter(ab)]*2):
        a -= 1; b -= 1
        edges[a].append(b)
        edges[b].append(a)
      parent = [None]*n
      def count(u):
        black, white = 1, 1
        for v in edges[u]:
          if v == parent[u]: continue 
          parent[v] = u
          b, w = count(v)
          black *= w; black %= MOD 
          white *= (b+w)%MOD; white %= MOD
        return black, white
      print(sum(count(0))%MOD)

  class ABC037:
    @staticmethod
    def a():
      a, b, c = map(int, sys.stdin.readline().split())
      print(c//min(a, b))

    @staticmethod
    def b():
      n, q, *lrt = map(int, sys.stdin.read().split())
      a = np.zeros(n, dtype=int)
      for l, r, t in zip(*[iter(lrt)]*3):
        a[l-1:r] = t 
      print(*a, sep='\n')
    
    @staticmethod
    def c():
      n, k, *a = map(int, sys.stdin.read().split())
      a = np.array([0]+a)
      np.cumsum(a, out=a)
      s = (a[k:] - a[:-k]).sum()
      print(s)
    
    @staticmethod
    def d():
      h, w, *a = map(int, sys.stdin.read().split())
      p = [None]*(h*w)
      def paths(k):
        if p[k]: return p[k]
        p[k] = 1
        i, j = divmod(k,w)
        if j>0 and a[k]>a[k-1]: p[k] += paths(k-1)
        if j<w-1 and a[k]>a[k+1]: p[k] += paths(k+1)
        if i>0 and a[k]>a[k-w]: p[k] += paths(k-w)
        if i<h-1 and a[k]>a[k+w]: p[k] += paths(k+w)
        p[k] %= MOD; return p[k] 
      print(sum(paths(i) for i in range(h*w))%MOD)


  class ABC038:
    @staticmethod
    def a():
      s = sys.stdin.readline().rstrip()
      print('YES' if s[-1]=='T' else 'NO')
    
    @staticmethod
    def b():
      a, b, c, d = map(int, sys.stdin.read().split())
      print('YES' if a==c or b==c or a==d or b==d else 'NO')
    
    @staticmethod
    def c():
      n, *a = map(int, sys.stdin.read().split())
      a += [-1]
      cnt = n 
      tmp = 1
      for i in range(n):
        if a[i+1] > a[i]:
          tmp += 1
        else:
          cnt += tmp*(tmp-1)//2
          tmp = 1
      print(cnt)
    
    @staticmethod
    def d():
      n, *wh = map(int, sys.stdin.read().split())
      a = [x[1] for x in sorted(zip(*[iter(wh)]*2), key=lambda x: (x[0], -x[1]))]
      print(bi_l(DP.LIS(a), inf))

  class ABC039:
    @staticmethod
    def a():
      a, b, c = map(int, sys.stdin.readline().split())
      print((a*b+b*c+c*a)*2)
    
    @staticmethod
    def b():
      x = int(sys.stdin.readline().rstrip())
      for n in range(1, int(x**0.5)+1):
        if pow(n, 4)==x:
          print(n); return

    
    @staticmethod
    def c():
      board = 'WBWBWWBWBWBW' * 3
      convert = 'Do, *, Re, *, Mi, Fa, *, So, *, La, *, Si'.split(', ')
      s = sys.stdin.readline().rstrip()
      print(convert[board.index(s)])


    @staticmethod 
    def d():
      h, w = map(int, sys.stdin.readline().split())
      s = ''.join(sys.stdin.read().split())
      white = set()
      for i in range(h*w):
        if s[i]=='#': continue
        l = 0 if i%w==0 else -1
        r = 0 if (i+1)%w==0 else 1
        white |= {i+dy+dx for dy in range(-w, w+1, w) for dx in range(l,r+1)}
      black_before = set(range(h*w)) - white 
      black_after = set()
      for i in black_before:
        l = 0 if i%w==0 else -1
        r = 0 if (i+1)%w==0 else 1
        black_after |= {i+dy+dx for dy in range(-w, w+1, w) for dx in range(l,r+1)}
      black_after &= set(range(h*w))
      for i in range(h*w):
        if s[i]=='#' and not i in black_after: print('impossible'); return
      print('possible')
      for i in range(h):
        print(''.join(['#' if i*w+j in black_before else '.' for j in range(w)]))

        
        
            
  class ABC040:
    @staticmethod
    def a():
      n, x = map(int, sys.stdin.readline().split())
      print(min(x-1, n-x))

    @staticmethod
    def b():
      n = int(sys.stdin.readline().rstrip())
      res = inf 
      for i in range(1, int(n**.5)+1):
        res = min(res, n//i-i+n%i)
      print(res)

    @staticmethod
    def c():
      n, *h = map(int, sys.stdin.read().split())
      h = [h[0]]+h
      cost = [None] * (n+1); cost[0] = cost[1] = 0
      for i in range(2, n+1):
        cost[i] = min(
          cost[i-2] + abs(h[i]-h[i-2]),
          cost[i-1] + abs(h[i]-h[i-1])
        )
      print(cost[n])

    @staticmethod
    def d():
      n, m = map(int, sys.stdin.readline().split())
      uf = GeometryTopology.Graph(n); uf.init_dsu()
      queue = []
      for _ in range(m):
        a, b, y = map(int, sys.stdin.readline().split())
        heappush(queue, (-(2*y), a-1, b-1))
      q = int(sys.stdin.readline().rstrip())
      for i in range(q):
        v, y = map(int, sys.stdin.readline().split())
        heappush(queue, (-(2*y+1), v-1, i))
      res = [None] * q
      while queue:
        y, i, j = heappop(queue)
        if y&1:
          res[j] = uf.size[uf.find(i)]
        else:
          uf.unite(i, j)
      print(*res, sep='\n')


      




  class ABC043:
    @staticmethod
    def a():
      n = int(sys.stdin.readline().rstrip())
      print((1+n)*n//2)
    
    @staticmethod
    def b():
      s = sys.stdin.readline().rstrip()
      t = ''
      for c in s:
        if c == 'B': t = t[:-1]
        else: t += c
      print(t)
    
    @staticmethod
    def c():
      n, *a = map(int, sys.stdin.read().split())
      a = np.array(a)
      x = np.around(a.sum()/n).astype(int)
      print(np.sum((a-x)**2))
    
    @staticmethod
    def d():
      s = sys.stdin.readline().rstrip()
      n = len(s)
      for i in range(n-1):
        if s[i] == s[i+1]: print(i+1, i+2); return 
      for i in range(n-2):
        if s[i] == s[i+2]: print(i+1, i+3); return 
      print(-1, -1)

  class ABC044:
    @staticmethod
    def a():
      n, k, x, y = map(int, sys.stdin.read().split())
      print(min(n,k)*x + max(0,n-k)*y)
    
    @staticmethod 
    def b():
      res = set(c&1 for c in Counter(sys.stdin.readline().rstrip()).values())
      print('Yes' if len(res)==1 and res.pop()==0 else 'No')

    @staticmethod 
    def c():
      n, a, *x = map(int, sys.stdin.read().split())
      dp = np.zeros((n+1, 2501), dtype=np.int64); dp[0,0] = 1 
      for v in x: dp[1:,v:] += dp[:-1,:-v]
      i = np.arange(1, n+1)
      print(dp[i, i*a].sum())

    @staticmethod
    def c_2():
      n, a, *x = map(int, sys.stdin.read().split())
      for i in range(n): x[i] -= a 

      s = defaultdict(int); s[0] = 1
      for i in range(n):
        ns = s.copy()
        for k, v in s.items(): ns[k+x[i]] += v 
        s = ns 
      print(s[0]-1)



    @staticmethod 
    def d():
      pass

  class ABC045:
    @staticmethod 
    def a():
      a, b, h = map(int, sys.stdin.read().split())
      print((a+b)*h//2)
    
    @staticmethod 
    def b():
      a, b, c = sys.stdin.read().split()
      d = {'a': a[::-1], 'b': b[::-1], 'c': c[::-1]}
      nx = 'a'
      while 1:
        if not d[nx]: print(nx.upper()); return 
        d[nx], nx = d[nx][:-1], d[nx][-1]

    @staticmethod 
    def c():
      def c(l): return pow(2, max(0,l-1))
      s = sys.stdin.readline().rstrip()
      n = len(s)
      print(sum(int(s[i:j+1])*c(i)*c(n-1-j) for i in range(n) for j in range(i, n)))

    @staticmethod 
    def d():
      h, w, n, *ab = map(int, sys.stdin.read().split())
      c = defaultdict(int)
      for y, x in zip(*[iter(ab)] * 2):
        y -= 1; x -= 1
        for dy, dx in itertools.product(range(-1, 2), repeat=2):
          i, j = y+dy, x+dx 
          if not(0<i<h-1 and 0<j<w-1): continue
          c[(i,j)] += 1
      c = Counter(c.values())
      c[0] = (h-2)*(w-2)-sum(c.values())
      for i in range(10): print(c[i])    


  class ABC046:
    @staticmethod 
    def a():
      print(len(set(sys.stdin.readline().split())))

    @staticmethod 
    def b():
      n, k = map(int, sys.stdin.readline().split())
      print(k*pow(k-1, n-1))

    @staticmethod 
    def c():
      n, *xy = map(int, sys.stdin.read().split())
      a, b = 1, 1
      for x, y in zip(*[iter(xy)]*2):
        n = max((a+x-1)//x, (b+y-1)//y)
        a, b = n*x, n*y 
      print(a+b)
    
    @staticmethod 
    def d():
      c = Counter(sys.stdin.readline().rstrip())
      print((c['g']-c['p'])//2)



  class ABC048:
    @staticmethod 
    def a():
      def initial(s): return s[0].upper()
      print(''.join(map(initial, sys.stdin.readline().split())))

    @staticmethod 
    def b():
      a, b, x = map(int, sys.stdin.readline().split())
      print(b//x - (a-1)//x) # if a=0, (a-1)/x is rounded down to -1.
    
    @staticmethod 
    def c():
      n, x, *a = map(int, sys.stdin.read().split())
      cnt = prev = 0
      for i in range(n):
        d = prev+a[i] - x
        prev = a[i]
        if d <= 0: continue 
        cnt += d; prev -= d
      print(cnt)

    @staticmethod 
    def d():
      s = sys.stdin.readline().rstrip()
      print('First' if len(s)&1^(s[0]==s[-1]) else 'Second')


      
  class ABC051:
    @staticmethod 
    def a():
      print(' '.join(sys.stdin.readline().rstrip().split(',')))
    
    @staticmethod 
    def b():
      k, s = map(int, sys.stdin.readline().split())
      tot = 0
      for x in range(k+1):
        if s-x < 0: break 
        if s-x > 2*k: continue 
        tot += s-x+1 if s-x<=k else 2*k-(s-x)+1
      print(tot)

    @staticmethod 
    def c():
      x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
      dx, dy = x2-x1, y2-y1
      print('U'*dy+'R'*(dx+1)+'D'*(dy+1)+'L'*(dx+1)+'U'+'L'+'U'*(dy+1)+'R'*(dx+1)+'D'*(dy+1)+'L'*dx)

    @staticmethod 
    def d():
      n, m, *abc = map(int, sys.stdin.read().split())
      x = np.arange(n)
      a, b, c = np.array(abc).reshape(m, 3).T; a -= 1; b -= 1
      d = shortest_path(csr_matrix((c, (a, b)), shape=(n, n)), method='FW', directed=False).astype(np.int64)
      print(m-np.any(d[x,a[:,None]]+c[:,None]==d[x,b[:,None]], axis=1).sum())


  class ABC052:
    @staticmethod 
    def a():
      a, b, c, d = map(int, sys.stdin.readline().split())
      print(max(a*b, c*d))
    
    @staticmethod 
    def b():
      n, s = sys.stdin.read().split()
      n = int(n)
      a = [0] * (n+1)
      for i in range(n):
        a[i+1] = a[i] + (1 if s[i]=='I' else -1) 
      print(max(a))

    @staticmethod 
    def c():
      n = int(sys.stdin.readline().rstrip())
      pn = NumberTheory.PrimeNumbers(n)
      s = 1
      for c in pn.factorize_factorial(n).values():
        s = s*(c+1)%MOD 
      print(s)

    @staticmethod 
    def d():
      n, a, b, *x = map(int, sys.stdin.read().split())
      x = np.array(x)
      print(np.minimum((x[1:]-x[:-1])*a, b).sum())

  class ABC053:
    @staticmethod 
    def a():
      print('ABC' if int(sys.stdin.readline().rstrip())<1200 else 'ARC')
    
    @staticmethod 
    def b():
      s = sys.stdin.readline().rstrip()
      print(len(s)-s.find('A')-s[::-1].find('Z'))
    
    @staticmethod 
    def c():
      x = int(sys.stdin.readline().rstrip())
      q, r = divmod(x, 11)
      print(2*q + (r+5)//6)
    
    @staticmethod 
    def d():
      n, *a = map(int, sys.stdin.read().split())
      print(n-((n-len(set(a))+1)//2*2))

  class ABC054:
    @staticmethod 
    def a():
      def f(x):
        return (x+11)%13
      a, b = map(int, sys.stdin.readline().split())
      print('Alice' if f(a)>f(b) else 'Bob' if f(a)<f(b) else 'Draw')
    
    @staticmethod 
    def b():
      n, m = map(int, sys.stdin.readline().split())
      a = [sys.stdin.readline().rstrip() for _ in range(n)]
      b = [sys.stdin.readline().rstrip() for _ in range(m)]
      
      def f(y, x):
        for i in range(m):
          for j in range(m):
            if a[y+i][x+j] != b[i][j]: return False
        return True 

      for y in range(n-m+1):
        for x in range(n-m+1):
          if f(y, x): print('Yes'); return
      print('No')
    
    @staticmethod 
    def c():
      n, m, *ab = map(int, sys.stdin.read().split())
      g = GeometryTopology.Graph(n)
      for a, b in zip(*[iter(ab)]*2):
        a -= 1; b -= 1
        g.add_edge(a,b); g.add_edge(b,a)
      def f(u, s):
        if s==(1<<n)-1: return 1
        return sum(f(v, s|1<<v) for v in g.edges[u] if ~s>>v&1)
      print(f(0,1))

    @staticmethod 
    def d():
      n, ma, mb, *abc = map(int, sys.stdin.read().split())
      dp = np.full((401, 401), np.inf); dp[0,0] = 0 
      for a, b, c in zip(*[iter(abc)]*3):
        np.minimum(dp[a:, b:], dp[:-a, :-b]+c, out=dp[a:, b:])
      i = np.arange(1, 400//max(ma,mb)+1)
      res = dp[i*ma, i*mb].min()
      print(int(res) if res != np.inf else -1)
      

  class ABC055:
    @staticmethod 
    def a():
      n = int(sys.stdin.readline().rstrip())
      print(800*n - 200*(n//15))
    
    @staticmethod 
    def b():
      n = int(sys.stdin.readline().rstrip())
      fac, _ = Algebra.generate_fac_ifac(n, MOD)
      print(fac[-1])
    
    @staticmethod 
    def c():
      n, m = map(int, sys.stdin.readline().split())
      print(m//2 if m<=2*n else n+(m-2*n)//4)

    @staticmethod 
    def d():
      n, s = sys.stdin.read().split(); n = int(n)
      s = [1 if c=='o' else 0 for c in s]
      def possible(t):
        for i in range(1, n-1): t[i+1] = t[i-1]^t[i]^s[i]
        return ((t[0]^s[0]^t[1]^t[-1])|(t[-1]^s[-1]^t[-2]^t[0]))^1

      for fst in [(1,0), (0,1), (1,1), (0,0)]:
        t = [None]*n; t[0], t[1] = fst[0], fst[1]
        if possible(t): print(''.join('S' if x==1 else 'W' for x in t)); return 
      print(-1)
  


  class ABC059:
    @staticmethod 
    def a():
      def initial(s): return s[0].upper()
      print(''.join(map(initial, sys.stdin.readline().split())))
      

    @staticmethod 
    def b():
      a, b = sys.stdin.read().split() 
      la, lb = len(a), len(b)
      print('GREATER' if la>lb else 'LESS' if la<lb else 'GREATER' if a>b else 'LESS' if a<b else 'EQUAL')

    @staticmethod 
    def c():
      n, *a = map(int, sys.stdin.read().split())
      c = s = 0
      for i in range(n):
        s += a[i]
        if i&1 and s>=0: c += s+1; s=-1
        elif i&1^1 and s<=0: c += 1-s; s=1
      c1 = c
      c = s = 0
      for i in range(n):
        s += a[i]
        if i&1 and s<=0: c += 1-s; s=1 
        elif i&1^1 and s>=0: c += s+1; s=-1 
      c2 = c
      print(min(c1, c2))
        
        
    @staticmethod 
    def d():
      x, y = map(int, sys.stdin.readline().split())
      print('Brown' if abs(x-y)<=1 else 'Alice')


  class ABC060:
    @staticmethod 
    def a():
      a, b, c = sys.stdin.readline().split() 
      print('YES' if a[-1]==b[0] and b[-1]==c[0] else 'NO')

    @staticmethod 
    def b():
      a, b, c = map(int, sys.stdin.readline().split())
      print('NO' if c%NumberTheory.gcd(a,b) else 'YES')


    @staticmethod 
    def c():
      n, t, *a = map(int, sys.stdin.read().split())
      print(sum(min(a[i+1]-a[i], t) for i in range(n-1))+t)
      

    @staticmethod 
    def d():
      n, W, *wv = map(int, sys.stdin.read().split())
      v, w0 = [[] for _ in range(4)], wv[0]
      for a, b in zip(*[iter(wv)]*2): v[a-w0].append(b)
      for i in range(4):
        v[i] = (sorted(v[i])+[0])[::-1]
        *v[i], = itertools.accumulate(v[i])
      global res; res = 0
      @lru_cache(maxsize=None)
      def dfs(i,j,k):
        if i>=len(v[0]) or j>=len(v[1]) or k>=len(v[2]): return 
        w = j+2*k + (i+j+k)*w0
        if w > W: return 
        l = min(len(v[3])-1, (W-w)//(w0+3))
        global res; res = max(res, v[0][i]+v[1][j]+v[2][k]+v[3][l])
        dfs(i+1,j,k); dfs(i,j+1,k); dfs(i,j,k+1)
      dfs(0,0,0)
      print(res)

  class ABC061:
    @staticmethod 
    def a():
      a, b, c = map(int, sys.stdin.readline().split())
      print('Yes' if a <= c <= b else 'No')

    @staticmethod 
    def b():
      n, m, *ab = map(int, sys.stdin.read().split())
      ab = np.array(ab) - 1
      g = np.zeros(n, dtype=np.int32)
      np.add.at(g, ab, 1)
      print(*g, sep='\n')


    @staticmethod 
    def c():
      n, k, *ab = map(int, sys.stdin.read().split())
      ab = np.transpose(np.array(ab).reshape(n,2))
      a, b = ab[:, np.argsort(ab[0])] 
      print(a[np.cumsum(b)>=k][0])
      
    @staticmethod 
    def d():
      n, m, *abc = map(int, sys.stdin.read().split())
      a, b, c = np.array(abc).reshape(m, 3).T; a -= 1; b -= 1; c *= -1
      g = csr_matrix(([1]*(m+1), (np.append(a, n-1), np.append(b, 0))), (n, n))
      _, labels = connected_components(g, connection='strong')
      bl = (labels[a]==labels[0]) & (labels[b]==labels[0])
      g = csr_matrix((c[bl], (a[bl], b[bl])), (n, n))
      try: print(-shortest_path(g, method='BF', directed=True, indices=0)[-1].astype(int))
      except: print('inf')
    
    @staticmethod 
    def d_2():
      n, m, *abc = map(int, sys.stdin.read().split())
      a, b, c = np.array(abc).reshape(m, 3).T; a -= 1; b -= 1; c *= -1
      d = np.full(n, np.inf); d[0] = 0   
      for _ in range(n-1): np.minimum.at(d, b, d[a]+c)
      neg_cycle = np.zeros(n, dtype=np.bool)
      for _ in range(n):
        np.logical_or.at(neg_cycle, b, d[a]+c<d[b])
        np.minimum.at(d, b, d[a]+c)
      print(inf if neg_cycle[-1] else -d[-1].astype(int))

    
  class ABC062:
    @staticmethod 
    def a():
      g = [0, 2, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
      x, y = map(int, sys.stdin.readline().split())
      print('Yes' if g[x-1]==g[y-1] else 'No')

    @staticmethod 
    def b():
      h, w = map(int, sys.stdin.readline().split())
      a = np.array([list(s) for s in sys.stdin.read().split()], dtype='U1')
      a = np.pad(a, pad_width=1, constant_values='#')
      for s in a: print(''.join(s))
      
    @staticmethod 
    def c():
      h, w = map(int, sys.stdin.readline().split())
      if h*w%3==0: print(0); return 
      def minimize(h, w):
        return min(h, *(s[-1]-s[0] for x in range(w//3, w//3+2) for s in (sorted([h*x, h//2*(w-x), (h+1)//2*(w-x)]),)))
      
      print(min(minimize(h,w), minimize(w,h)))


    @staticmethod 
    def d():
      n, *a = map(int, sys.stdin.read().split())
      a = np.array(a)

      def optimize(a):
        a = list(a)
        l, r = a[:n], a[n:]; heapify(l)
        s = [None]*(n+1); s[0] = sum(l)
        for i in range(n):
          x = heappop(l)
          heappush(l, max(x, r[i]))
          s[i+1] = s[i]+max(0, r[i]-x)
        return np.array(s)

      print((optimize(a[:2*n]) + optimize(-a[-1:n-1:-1])[::-1]).max())

  class ABC063:
    @staticmethod 
    def a():
      a = sum(map(int, sys.stdin.readline().split()))
      print('error' if a>=10 else a)
      

    @staticmethod 
    def b():
      s = sys.stdin.readline().rstrip()
      print('yes' if len(set(s))==len(s) else 'no')

    @staticmethod
    def c():
      n, *a = map(int, sys.stdin.read().split())
      a = np.array(a)
      s = a.sum() 
      if s%10: print(s)
      elif not np.count_nonzero(a%10): print(0)
      else: print(s-a[a%10!=0].min())
      


    @staticmethod 
    def d():
      n, a, b, *h = map(int, sys.stdin.read().split())
      h = np.array(h)
      d = a-b

      def possible(c):
        hh = h.copy()
        np.maximum(hh-b*c, 0, out=hh)
        return ((hh+d-1)//d).sum() <= c
      
      def binary_search():
        lo, hi = 0, 10**9
        while hi-lo > 1:
          c = (lo+hi)//2 
          if possible(c): hi = c 
          else: lo = c 
        return hi 
      
      print(binary_search())

  class ABC064:
    @staticmethod 
    def a():
      r, g, b = map(int, sys.stdin.readline().split())
      print('NO' if (10*g+b)%4 else 'YES')
    
    @staticmethod 
    def b():
      n, *a = map(int, sys.stdin.read().split())
      a.sort()
      print(a[-1]-a[0])
    
    @staticmethod 
    def c():
      n, *a = map(int, sys.stdin.read().split())
      a = np.bincount(np.minimum(np.array(a)//400, 8), minlength=9)
      mx = np.count_nonzero(a[:-1]) + a[-1]
      mn = max(mx-a[-1], 1)
      print(mn, mx)

    @staticmethod 
    def d():
      n, s = sys.stdin.read().split() 
      l = r = 0 
      for c in s:
        if c=='(': r += 1
        else:
          if r==0: l += 1
          else: r -= 1
      print('('*l+s+')'*r)
      
  class ABC065:
    @staticmethod 
    def a():
      x, a, b = map(int, sys.stdin.readline().split())
      y = -a+b
      print('delicious' if y<=0 else 'safe' if y<=x else 'dangerous')
      
    @staticmethod 
    def b():
      n, *a = [int(x)-1 for x in sys.stdin.read().split()]
      i = 0
      for c in range(n):
        i = a[i]
        if i == 1: print(c+1); return 
      print(-1)
      
    @staticmethod 
    def c():
      n, m = map(int, sys.stdin.readline().split())
      d = abs(n-m)
      if d >= 2: print(0); return
      fac, _ = Algebra.generate_fac_ifac(10**5)
      print(fac[n]*fac[m]*(1 if d else 2)%MOD)
      
    @staticmethod 
    def d():
      n, *xy = map(int, sys.stdin.read().split())
      x, y = np.array(xy).reshape(n,2).T
      i = np.argsort(x); ax, bx, cx = i[:-1], i[1:], x[i[1:],]-x[i[:-1]]
      i = np.argsort(y); ay, by, cy = i[:-1], i[1:], y[i[1:],]-y[i[:-1]]
      e = np.vstack([np.hstack([ax,ay]),np.hstack([bx,by]),np.hstack([cx,cy])])
      e = e[:,np.argsort(e[-1])]
      _, i = np.unique(e[:-1], return_index=True, axis=1)
      a, b, c = e[:,i]
      print(minimum_spanning_tree(csr_matrix((c,(a,b)), (n,n))).astype(np.int64).sum())

    
    @staticmethod 
    def d_2():
      n, *xy = map(int, sys.stdin.read().split())
      x, y = xy[::2], xy[1::2]
      g = GeometryTopology.Graph(n)
      def make(a):
        b = sorted(enumerate(a), key=lambda x: x[1])
        for i in range(n-1):
          u, v, w = b[i][0], b[i+1][0], b[i+1][1]-b[i][1]
          for u, v in [(v,u), (u,v)]:
            if not v in g.edges[u]: g.add_edge(u, v, weight=w)
            else: g.edges[u][v].weight = min(g.edges[u][v].weight, w)
      make(x); make(y)
      _, d = g.kruskal()
      # _, d = g.prim()
      # _, d = g.boruvka()
      print(d)


      
  class ABC066:
    @staticmethod 
    def a():
      print(sum(sorted(map(int, sys.stdin.readline().split()))[:-1]))

    @staticmethod 
    def b():
      s = sys.stdin.readline().rstrip()
      def f(s):
        n = len(s)//2
        return s[:n] == s[n:]
      for i in range(len(s)-2, 0, -2):
        if f(s[:i]): print(i); return 

    @staticmethod 
    def c():
      n, *a = map(int, sys.stdin.read().split())
      b = deque()
      for i in range(n):
        if i&1: b.appendleft(a[i])
        else: b.append(a[i])
      if n&1: b.reverse()
      print(*b)

    @staticmethod 
    def d():
      n, *a = map(int, sys.stdin.read().split())
      tmp = [None]*(n+1)
      for i in range(n+1):
        if tmp[a[i]] is not None: d=tmp[a[i]]+n-i; break 
        tmp[a[i]] = i
      k = np.arange(1, n+2)
      c = Combinatorics.CombinationsMod(n+1, MOD)
      print(*((c(n+1,k)-c(d,k-1))%MOD), sep='\n')

      
  class ABC067:
    @staticmethod 
    def a():
      a, b = map(int, sys.stdin.readline().split())
      print('Impossible' if a%3 and b%3 and (a+b)%3 else 'Possible')

    @staticmethod 
    def b():
      n, k, *l = map(int, sys.stdin.read().split())
      print(sum(sorted(l)[-k:]))


    @staticmethod 
    def c():
      n, *a = map(int, sys.stdin.read().split())
      a = np.array(a)
      np.cumsum(a, out=a)
      print(np.absolute(a[-1]-2*a[:-1]).min())
      

    @staticmethod 
    def d():
      n, *ab = map(int, sys.stdin.read().split())
      g = GeometryTopology.Graph(n)
      for a, b in zip(*[iter(ab)]*2):
        a -= 1; b -= 1
        g.add_edge(a, b); g.add_edge(b,a)
      d1, d2 = g.bfs(0), g.bfs(n-1)
      print('Fennec' if sum(d1[i]<=d2[i] for i in range(n)) > n//2 else 'Snuke')

  class ABC068:
    @staticmethod 
    def a():
      print('ABC'+sys.stdin.readline().rstrip())
       
    @staticmethod 
    def b():
      print(2**math.floor(math.log2(int(sys.stdin.readline().rstrip()))))

    @staticmethod 
    def c():
      n, m, *ab = map(int, sys.stdin.read().split())
      a, b = np.array(ab).reshape(m, 2).T 
      d = shortest_path(csr_matrix(([1]*m, (a-1, b-1)), (n,n)), method='D', directed=False, indices=0).astype(np.int32)
      print('POSSIBLE' if d[-1]==2 else 'IMPOSSIBLE')

    @staticmethod 
    def d():
      k = int(sys.stdin.readline().rstrip())
      n = 50; print(n)
      q,r = divmod(k,n); a = np.arange(n-1,-1,-1)+q; a[:r]+=1; print(*a)
      
  class ABC069:
    @staticmethod 
    def a():
      n, m = map(int, sys.stdin.readline().split())
      print((n-1)*(m-1))


    @staticmethod 
    def b():
      pass 

    @staticmethod 
    def c():
      pass 


    @staticmethod 
    def d():
      h, w, n, *a = map(int, sys.stdin.read().split())
      c = [i+1 for i in range(n) for j in range(a[i])]
      for i in range(h):
        row = c[i*w:(i+1)*w] 
        if i&1: row = row[::-1]
        print(*row)
      
  class ABC070:
    @staticmethod
    def d():
      n = int(sys.stdin.readline().rstrip())
      g = GeometryTopology.Graph(n)
      for _ in range(n-1):
        a, b, c = map(int, sys.stdin.readline().split()); a-=1; b-=1
        g.add_edge(a, b, weight=c); g.add_edge(b, a, weight=c)
      q, k = map(int, sys.stdin.readline().split())
      d = g.bfs(k-1)
      for _ in range(q):
        x, y = map(int, sys.stdin.readline().split()); x-=1; y-=1
        print(d[x]+d[y])
      
  class ABC071:
    @staticmethod 
    def d():
      n, *s = sys.stdin.read().split(); n = int(n)
      s = list(zip(*s))
      dp = [0]*n; dp[0] = 3 if s[0][0]==s[0][1] else 6
      for i in range(1,n):
        dp[i] = dp[i-1]
        if s[i][0]==s[i-1][0]: continue
        dp[i] *= 2 if s[i-1][0]==s[i-1][1] else 3 if s[i][0]!=s[i][1] else 1
        dp[i] %= MOD 
      print(dp[-1])

  class ABC072:
    @staticmethod 
    def d():
      n, *p = map(int, sys.stdin.read().split())
      p += [-1]
      cnt, i = 0, 0
      while i < n:
        if p[i]==i+1:
          cnt += p[i]==i+1
          if p[i+1]==i+2: i += 1
        i += 1
      print(cnt)


  class ABC073:
    @staticmethod 
    def a():
      pass 

    @staticmethod 
    def b():
      pass 

    @staticmethod 
    def c():
      pass 

    @staticmethod 
    def d():
      n, m, r, *I = map(int, sys.stdin.read().split())
      I = np.array(I)
      a, b, c = I[r:].reshape(m,3).T 
      d = shortest_path(csr_matrix((c, (a-1, b-1)), (n,n)), method='FW', directed=False).astype(np.int32)
      r = np.array([*itertools.permutations(I[:r]-1)])
      print((d[r[:,:-1], r[:,1:]].sum(axis=1)).min())

  class ABC074:
    @staticmethod 
    def a():
      pass 

    @staticmethod 
    def b():
      pass 

    @staticmethod 
    def c():
      pass 

    @staticmethod 
    def d():
      n, *a = map(int, sys.stdin.read().split())
      a = np.array(a, dtype=np.int32).reshape(n,n)
      b = shortest_path(a, method='FW').astype(np.int32)
      if (b < a).any(): print(-1); return 
      np.fill_diagonal(b, 10**9)
      a[np.any(b[:,None]+b<=a[:,:,None], axis=2)] = 0
      print(a.sum()//2)



  class ABC075:
    @staticmethod 
    def a():
      pass 

    @staticmethod 
    def b():
      pass 

    @staticmethod 
    def c():
      pass 
    
    @staticmethod 
    def d():
      n, k, *xy = map(int, sys.stdin.read().split())
      xy = np.array(xy).reshape(n,2) 
      x_y = xy.copy()[np.argsort(xy[:,0])]
      y_x = xy.copy()[np.argsort(xy[:,1])]
      comb = np.array([*itertools.combinations(range(n),2)])
      i1, i2 = comb.T 
      j1, j2 = comb[None,:].T
      s = (y_x[:,1][i2]-y_x[:,1][i1]) * (x_y[:,0][j2]-x_y[:,0][j1])
      c = np.zeros((n+1,n+1), dtype=np.int64)
      for i in range(n): c[i+1, 1:] += c[i, 1:] + (y_x[i,0]<=x_y[:,0])
      a = c[i2+1, j2+1] - c[i2+1, j1] - c[i1, j2+1] + c[i1, j1]
      print(s[a>=k].min())


  class ABC076:
    @staticmethod 
    def d():
      n, *tv = map(int, sys.stdin.read().split())
      t, v = np.array(tv).reshape(2, n)
      t = np.pad(t, pad_width=[2,1], constant_values=0)
      np.cumsum(t, out=t)
      l, r = t[:-1], t[1:]
      v = np.pad(v, pad_width=[1,1], constant_values=0)
      x = np.arange(0, r[-1]+0.1, 0.5, dtype=np.float32)[:,None]
      # y = np.stack([v-(x-l), np.zeros(r[-1]*2+1, dtype=np.float32)[:,None]+v, v+(x-r)]).max(axis=0).min(axis=1)
      mx = v-(x-l); np.maximum(mx, v, out=mx); np.maximum(mx, v+(x-r), out=mx)
      y = mx.min(axis=1)
      print(((y[:-1]+y[1:])/4).sum())


  class ABC077:
    @staticmethod 
    def d():
      k = int(sys.stdin.readline().rstrip())
      g = GeometryTopology.Graph(k)
      for i in range(k):
        g.add_edge(i, i*10%k, weight=0)
        g.add_edge(i, (i+1)%k, update=False, weight=1)
      print(1+g.bfs01(1)[0])

      
  class ABC078:
    @staticmethod 
    def d():
      n, z, w, *a = map(int, sys.stdin.read().split())
      print(abs(a[0]-w) if n==1 else max(abs(a[-1]-w), abs(a[-1]-a[-2])))

  class ABC079:
    @staticmethod 
    def d():
      h, w, *I = map(int, sys.stdin.read().split())
      I = np.array(I)
      c = I[:100].reshape(10,10)
      a = I[100:].reshape(h,w)
      c = shortest_path(c.T, method='D', indices=1).astype(np.int32)
      print(c[a[a!=-1]].sum())

  class ABC080:
    @staticmethod 
    def d():
      n, c, *stc = map(int, sys.stdin.read().split())
      using = np.zeros((c, 10**5+2), dtype=np.int8)
      s, t, c = np.array(stc).reshape(n,3).T
      np.add.at(using, (c-1, s), 1)
      np.subtract.at(using, (c-1, t+1), 1)
      np.cumsum(using, axis=1, out=using)
      print(np.count_nonzero(using, axis=0).max())

  class ABC081:
    @staticmethod 
    def d():
      n, *a = map(int, sys.stdin.read().split())
      a = np.array(a)
      i = np.argmax(np.absolute(a))
      print(2*n-1)
      for j in range(n): print(i+1, j+1)
      if a[i] >= 0: 
        for j in range(n-1): print(j+1, j+2)
      else:
        for j in range(n-1, 0, -1): print(j+1, j)


  class ABC082:
    @staticmethod 
    def d():
      s = [1 if c=='T' else 0 for c in sys.stdin.readline().rstrip()] + [1]
      x, y = map(int, sys.stdin.readline().split())
      i = j = 0 
      while s[i]==0: x -= 1; i +=1 
      d = [[], []]
      while i < len(s):
        if s[i]: j ^= 1; i += 1; continue 
        c = 0
        while s[i]==0: c += 1; i += 1
        d[j].append(c)

      def possible(a, s):
        dp = np.zeros(sum(a)+1, dtype=np.bool)
        if s >= len(dp): return False
        dp[-1] = True 
        for x in a: dp[:-2*x] += dp[2*x:]
        return dp[s]

      print('Yes' if possible(d[0], abs(x)) & possible(d[1], abs(y)) else 'No')


  class ABC083:
    @staticmethod 
    def d():
      s = np.array(list(sys.stdin.readline().rstrip()), dtype=np.int8)
      k = np.argwhere(s[:-1] != s[1:]).ravel()
      if not k.size: print(len(s)); return 
      print(np.maximum(k+1, len(s)-1-k).min())
      

  class ABC084:
    @staticmethod 
    def d():
      pn = NumberTheory.PrimeNumbers()
      n = np.arange(10**5+1)
      cnt = (pn.is_prime[n] & pn.is_prime[(n+1)//2]).astype(np.int32)
      np.cumsum(cnt, out=cnt)
      q, *lr = map(int, sys.stdin.read().split())
      l, r = np.array(lr).reshape(q, 2).T 
      print(*(cnt[r]-cnt[l-1]), sep='\n')
       

  class ABC085:
    @staticmethod 
    def d():
      n, h, *ab = map(int, sys.stdin.read().split())
      a, b = np.array(ab).reshape(n, 2).T
      a = np.sort(a)[-1]; b = np.sort(b[b>=a])[::-1]
      np.cumsum(b, out=b)
      print(np.searchsorted(b, h, side='left')+1 if h<=b[-1] else len(b)+(h-b[-1]+a-1)//a)
  
  class ABC086:
    @staticmethod 
    def d():
      n, k = map(int, sys.stdin.readline().split())
      xy = []
      for _ in range(n):
        a, b, c = sys.stdin.readline().split()
        a, b = int(a), int(b)
        b += k*(c=='W')
        xy.append((a,b))
      x, y = np.array(xy, dtype=np.int32).T % (2*k)
      s = np.zeros((3*k, 3*k), dtype=np.int32)
      np.add.at(s, (y,x), 1); np.add.at(s, (y+k, x+k), 1); np.add.at(s, (y+k, x), -1); np.add.at(s, (y, x+k), -1)
      del x; del y
      s = s.cumsum(axis=0).cumsum(axis=1)
      s[:k] += s[-k:]; s[:, :k] += s[:, -k:]; s = s[:-k, :-k]
      s[:k, :k] += s[-k:, -k:]; s[:k, -k:] += s[-k:, :k]; s = s[:k]
      print(s.max())

  class ABC087:
    @staticmethod 
    def d():
      n, m, *lrd = map(int, sys.stdin.read().split())
      g = GeometryTopology.Graph(n)
      for l, r, d in zip(*[iter(lrd)]*3):
        l -= 1; r -= 1 
        g.add_edge(l, r, weight=d); g.add_edge(r, l, weight=-d)

      x = [None] * n
      @lru_cache(maxsize=None)
      def dfs(u, y):
        if x[u] is not None:
          if x[u] != y: raise Exception('conflict!')  
          return 
        x[u] = y 
        for v, e in g.edges[u].items(): dfs(v, y+e.weight)
      
      for u in range(n):
        if x[u] is not None: continue 
        # try: dfs(u, 0)
        # except: print('No'); return 
        stack = [(u, 0)]
        while stack:
          u, y = stack.pop()
          if x[u] is not None:
            if x[u] != y: print('No'); return 
            continue 
          x[u] = y 
          for v, e in g.edges[u].items(): stack.append((v, y+e.weight))
      print('Yes')

  class ABC088:
    @staticmethod 
    def d():
      h, w = map(int, sys.stdin.readline().split())
      s = ''.join(sys.stdin.read().split())
      g = GeometryTopology.Graph(h*w)
      cnt = h*w
      for u in range(h*w):
        if s[u] == '#': cnt -= 1; continue 
        i, j = divmod(u, w)
        if i>0 and s[u-w]=='.': g.add_edge(u, u-w, weight=1)
        if i<h-1 and s[u+w]=='.': g.add_edge(u, u+w, weight=1)
        if j>0 and s[u-1]=='.': g.add_edge(u, u-1, weight=1)
        if j<w-1 and s[u+1]=='.': g.add_edge(u, u+1, weight=1)
      d = g.bfs(0)
      print(-1 if d[-1]==inf else cnt-d[-1]-1)

  class ABC089:
    @staticmethod 
    def d():
      h, w, d, *I = map(int, sys.stdin.read().split())
      I = np.array(I)
      a = I[:h*w].reshape(h,w)
      l, r = I[h*w+1:].reshape(-1,2).T - 1
      yx = np.pad(np.argwhere(a)[np.argsort(a.ravel())], pad_width=[(0,d), (0,0)], constant_values=0)
      a = np.zeros(h*w+d, dtype=np.int32)
      for i in range(0, h*w-d, d):
        a[i+d:i+2*d] = a[i:i+d] + np.absolute(yx[i+d:i+2*d]-yx[i:i+d]).sum(axis=1)
      print(*(a[r]-a[l]), sep='\n')
 
  class ABC090:
    @staticmethod 
    def d():
      n, k = map(int, sys.stdin.readline().split())
      b = np.arange(k+1, n+1)
      print((n//b*(b-k) + np.maximum(0, (n%b)-k+1*(k!=0))).sum())

  class ABC091:
    @staticmethod 
    def d():
      n, *ab = map(int, sys.stdin.read().split())
      c = 2**np.arange(30)
      a, b = np.sort(np.array(ab).reshape(2,n)[:, None] % (2*c)[:,None])
      res = 0
      for i in range(30):
        j = np.searchsorted(b[i], np.arange(1, 5)[:,None]*c[i]-a[i]).sum(axis=1)
        j[1::2] *= -1 
        res += (j.sum()&1) * c[i]
      print(res)

  class ABC092:
    @staticmethod 
    def d():
      a, b = map(int, sys.stdin.readline().split())
      def make(color, cnt):
        g = [[color^1]*100 for _ in range(21)]
        for i in range(1, 21, 2):
          for j in range(0, 100, 2):
            if not cnt: return g 
            g[i][j] = color; cnt -= 1
      g = make(0,a-1) + make(1,b-1)
      def convert(s): return ''.join('#' if c else '.' for c in s)
      print(42, 100)
      print(*map(convert, g), sep='\n')

  class ABC093:
    @staticmethod 
    def d():
      q, *ab = map(int, sys.stdin.read().split())
      a, b = np.sort(np.array(ab).reshape(q,2)).T
      x = np.sqrt(a*b).astype(int)
      x[x*x==a*b] -= 1
      res = a-1
      res += (a-1) * (b-a<=1)
      res += (x+np.minimum(x-a-1*(x*(x+1)>=a*b), b-x-1)) * (b-a>=2)

      # res = 0
      # res += 2*(a-1) * (b-a<=1)
      # res += (2*x-1 - 1*(x*(x+1)>=a*b)) * (b-a >= 2)

      print(*res, sep='\n')

      

  class ABC094:
    @staticmethod 
    def d():
      n, *a = map(int, sys.stdin.read().split())
      a.sort()
      print(a[-1], end=' ')
      b = (a[-1]+1)//2
      i = bi_l(a, b)
      print(a[-2] if i==n-1 else a[i-1] if b-a[i-1]<=a[i]-b else a[i])
      
      

  class ABC095:
    @staticmethod 
    def d():
      n, c, *xv = map(int, sys.stdin.read().split())

      def make(xv):
        x, v = xv.T
        s = np.cumsum(v)-x; rs = s-x
        np.maximum.accumulate(s, out=s)
        np.maximum.accumulate(rs, out=rs)
        return s, rs 

      xv = np.pad(np.array(xv).reshape(n,2), pad_width=[(1,0), (0,0)], constant_values=0)
      ls, lrs = make(xv)
      xv[1:, 0] = c-xv[1:, 0]; xv[1:] = xv[-1:0:-1]
      rs, rrs = make(xv)
      print(np.maximum(ls+rrs[::-1], rs+lrs[::-1]).max())

  class ABC096:
    @staticmethod 
    def d():
      n = int(sys.stdin.readline().rstrip())
      pn = NumberTheory.PrimeNumbers()
      a = [p for p in pn if p%5==1]
      print(*a[:n])      
      

  class ABC097:
    @staticmethod 
    def d():
      n, m = map(int, sys.stdin.readline().split())
      p = [int(x)-1 for x in sys.stdin.readline().split()]
      uf = GeometryTopology.Graph(n); uf.init_dsu()
      for x, y in zip(*[map(int, sys.stdin.read().split())]*2): uf.unite(x-1, y-1)
      groups = [set(p[u] for u in g) for g in uf.groups()]
      print(sum(i in groups[uf.find(i)] for i in range(n)))      
      
  class ABC098:
    @staticmethod 
    def d():
      n, *a = map(int, sys.stdin.read().split())
      r = s = cnt = 0
      for l in range(n):
        while r<n and not(s&a[r]): s ^= a[r]; r += 1
        cnt += r-l; s ^= a[l]
      print(cnt)
        
 
  class ABC099:
    @staticmethod 
    def d():
      n, c, *I = map(int, sys.stdin.read().split())
      I = np.array(I)
      d = I[:c*c].reshape(c,c)
      r = np.arange(n*n); r = (r//n + r%n)%3
      a = d[I[c*c:]-1, np.arange(c)[:,None]]
      r = np.arange(n*n); r = (r//n + r%n)%3 == np.arange(3)[:,None]
      a = np.vstack([a[:,r[i]].sum(axis=1) for i in range(3)])
      p = np.array([*itertools.permutations(range(c), 3)])
      print(a[np.arange(3),p].sum(axis=1).min())


  class ABC100:
    @staticmethod 
    def d():
      n, m, *xyz = map(int, sys.stdin.read().split())
      xyz = np.array(xyz).reshape(n,3)
      op = np.array([*itertools.product((-1,1), repeat=3)])
      print(np.sort((op[:,None]*xyz).sum(axis=-1), axis=-1)[:,n-m:].sum(axis=-1).max())

  class ABC101:
    @staticmethod 
    def d():
      def s(n): return sum(int(d) for d in str(n))
      def f(n):
        return sorted([pow(10,d)*(n//pow(10,d)+2)-1 for d in range(int(math.log10(n))+2)], key=lambda x: x/s(x))[0]
      k = int(sys.stdin.readline().rstrip())
      n = 1
      for _ in range(k): print(n); n = f(n)
    
  class ABC102:
    @staticmethod 
    def d(): # two pointers (online)
      n, *a = map(int, sys.stdin.read().split())
      mn = inf
      i, k = 0, 2
      p,q,r,s = a[0], 0, a[1]+a[2], sum(a[3:])
      for j in range(1,n-2):
        q += a[j]; r -= a[j]
        while i < j-1:
          if abs(q-p-2*a[i+1]) <= abs(q-p):
            q -= a[i+1]; p += a[i+1]
            i += 1; continue
          break
        while k < n-2:
          if abs(s-r-2*a[k+1]) <= abs(s-r):
            s -= a[k+1]; r += a[k+1]
            k += 1; continue 
          break 
        tmp = sorted([p,q,r,s])
        mn = min(mn, tmp[-1]-tmp[0])
      print(mn)
    
    @staticmethod 
    def d_2(): # binary_search (offline)
      n, *a = map(int, sys.stdin.read().split())
      a = np.array(a)
      def f(a):
        s = np.cumsum(a)
        i = np.searchsorted(s, s/2)
        l, r = s[i], s-s[i]
        bl = np.abs(r-l) > np.abs(r-l+2*a[i])
        l -= a[i]*bl; r += a[i]*bl
        return l, r
      (p,q), (s,r) = f(a), f(a[::-1])
      a = np.sort(np.vstack((p[:-1], q[:-1], r[-2::-1], s[-2::-1])), axis=0)[:,1:-1]
      print((a[-1]-a[0]).min())

  class ABC103:
    @staticmethod 
    def d():
      n, m, *ab = map(int, sys.stdin.read().split())
      cnt = prev = 0
      for a, b in sorted(zip(*[iter(ab)]*2), key=lambda x: x[1]):
        a -= 1; b -= 1
        if a < prev: continue 
        prev = b; cnt += 1
      print(cnt)

  class ABC104:
    @staticmethod 
    def d():
      s = sys.stdin.readline().rstrip()[::-1]
      a = b = c = 0; d = 1
      for i in range(len(s)):
        if s[i]=='?': a,b,c,d = 3*a+b, 3*b+c, 3*c+d, 3*d
        elif s[i] == 'A': a += b 
        elif s[i] == 'B': b += c 
        elif s[i] == 'C': c += d
        a %= MOD; b %= MOD; c %= MOD; d %= MOD 
      print(a)

  class ABC105:
    @staticmethod 
    def d():
      n, m, *a = map(int, sys.stdin.read().split())
      c = Counter(np.array(a).cumsum()%m)
      print(c[0] + sum([v*(v-1)//2 for v in c.values()]))

  class ABC106:
    @staticmethod 
    def d():
      n, m, q, *I = map(int, sys.stdin.read().split())
      I = np.array(I).reshape(-1,2) - 1
      (l,r), (p,q) = I[:m].T, I[-q:].T
      c = np.zeros((n+1, n+1), dtype=np.int64)
      np.add.at(c, (0,r), 1); np.add.at(c, (l+1,-1), 1)
      np.add.at(c, (l+1,r), -1); c[0,-1] -= m
      c = c.cumsum(axis=0).cumsum(axis=1)
      print(*c[p,q], sep='\n')

  class ABC107:
    @staticmethod 
    def d():
      n, *a = map(int, sys.stdin.read().split())
      h = (n*(n+1)//2 + 1)//2

      def f(x):
        *b, = itertools.accumulate([0]+[-1+2*(v>=x) for v in a])
        mn = min(b)
        b = [v-mn+1 for v in b]
        bit = GeometryTopology.FenwickTree(max(b))
        c = 0
        for v in b: c += bit.sum(1, v); bit.add(v, 1)
        return c >= h

      def f_2(x):
        tot = 0
        s, cs, c = 0, defaultdict(int), 0; cs[0] = 1
        for v in a:
          if v>=x: s += 1; c += cs[s]
          else: c -= cs[s]; s -= 1
          tot += c; cs[s] += 1; c += 1
        # print(tot)
        return tot >= h

      def binary_search():
        lo, hi = 1, 10**9+1
        while hi-lo > 1:
          x = (hi+lo)//2
          # if f(x): lo = x
          if f_2(x): lo = x
          else: hi = x 
        return lo
      print(binary_search())
    
    

  class ABC108:
    @staticmethod 
    def d():
      l = int(sys.stdin.readline().rstrip())
      n = l.bit_length()
      m = 2*(n-1) + bit_count(l)-1
      edges = [(i, i+1, d) for i in range(n-1) for d in [0, 1<<i]]
      d = 1<<(n-1)
      for i in range(n-1):
        if l>>i&1: edges.append((i, n-1, d)); d += 1<<i
      print(n, m)
      for u, v, d in edges: print(u+1, v+1, d)
      

  class ABC109:
    @staticmethod 
    def d():
      h, w, *a = map(int, sys.stdin.read().split())
      a = np.array(a).reshape(h,w)
      res, cnt = [], 0
      for i in range(h-1):
        j = np.argwhere(a[i]&1).ravel()
        a[i,j] -= 1; a[i+1,j] += 1
        l = j.size
        res += list(zip([i+1]*l, j+1, [i+2]*l, j+1))
        cnt += l 
      for j in range(w-1):
        if ~a[-1,j]&1: continue
        a[-1,j+1] += 1; a[-1,j] -= 1
        res.append((h, j+1, h, j+2))
        cnt += 1
      print(cnt)
      for p in res: print(*p)


  class ABC110:
    @staticmethod 
    def d():
      n, m = map(int, sys.stdin.readline().split())
      if m==1: print(1); return 
      c = Combinatorics.CombinationsMod(n=10**6, mod=MOD)
      pn = NumberTheory.PrimeNumbers(10**5)
      f = np.array([*pn.factorize(m).values()])
      print(Algebra.cumprod(c(n+f-1, f), mod=MOD)[-1])

  class ABC111:
    @staticmethod 
    def d():
      n, *xy = map(int, sys.stdin.read().split())

      pass 
    
  class ABC112:
    @staticmethod 
    def d():
      n, m = map(int, sys.stdin.readline().split())
      divs = NumberTheory.find_divisors(m)
      print(m//divs[bi_l(divs, n)])

  class ABC113:
    @staticmethod 
    def d():
      h, w, k = map(int, sys.stdin.readline().split())
      f = np.zeros(w+1, dtype=np.int64); f[1] = 1
      for i in range(2, w+1): f[i] = (f[i-2]+f[i-1]) % MOD
      a = np.zeros((w,w), dtype=np.int64)
      i = np.arange(w); j = w-1-i
      a[i,i] = f[i+1]*f[j+1]
      a[i[1:],i[:-1]] = f[i[1:]]*f[j[1:]+1]
      a[i[:-1],i[1:]] = f[i[:-1]+1]*f[j[:-1]]
      a %= MOD
      print(Algebra.matrix_pow(a, h, mod=MOD)[k-1,0])

  class ABC114:
    @staticmethod 
    def d():
      pn = NumberTheory.PrimeNumbers(100)
      n = int(sys.stdin.readline().rstrip())
      if n==1: print(0); return 
      c = np.bincount(np.array([*pn.factorize_factorial(n).values()]), minlength=75)
      np.cumsum(c[::-1], out=c[::-1])
      print(c[4]*(c[4]-1)//2 * (c[2]-2) + c[14]*(c[4]-1) + c[24]*(c[2]-1) + c[74])

  class ABC115:
    @staticmethod 
    def d():
      n, x = map(int, sys.stdin.readline().split())
      l, p = [None]*(n+1), [None]*(n+1); l[0] = p[0] = 1
      for i in range(n): l[i+1], p[i+1] = 2*l[i]+3, 2*p[i]+1
      def f(i, x):
        if i==0: return 0 if x<=0 else 1
        elif x<=l[i]//2: return f(i-1, x-1)
        else: return p[i-1]+1+f(i-1,x-1-l[i]//2)
      print(f(n, x))

  class ABC116:
    @staticmethod 
    def d():
      n, k, *td = map(int, sys.stdin.read().split())
      td = sorted(zip(*[iter(td)]*2), key=lambda x: -x[1])
      appeared = [False] * n 
      a, b = [], [0]
      for t, d in td:
        if appeared[t-1]: b.append(d)
        else: appeared[t-1] = True; a.append(d)
      *a, = itertools.accumulate(a)
      *b, = itertools.accumulate(b)
      res = 0
      for x in range(min(len(a), k)):
        res = max(res, (x+1)**2 + a[x]+b[min(k-x,len(b))-1])
      print(res)


  class ABC117:
    @staticmethod 
    def d():
      n, k, *a = map(int, sys.stdin.read().split())
      m = 40
      a = (np.array(a)[:,None]>>np.arange(m)&1).sum(axis=0)
      l = k.bit_length()
      mx = (np.maximum(a, n-a) * (1<<np.arange(m))).cumsum()
      s = ((1<<np.arange(l, m)) * a[l:]).sum()
      def dfs(i):
        if i < 0: return 0
        tmp = dfs(i-1)
        s1 = (1<<i)*(n-a[i]) + tmp
        s2 = (1<<i)*a[i] + (0 if i == 0 else mx[i-1])
        s3 = (1<<i)*a[i] + tmp
        return max(s1, s2) if k>>i&1 else s3 
      print(s+dfs(l-1))

  class ABC118:
    @staticmethod 
    def d():
      c = [None, 2, 5, 5, 4, 5, 6, 3, 7, 6]
      n, m, *a = map(int, sys.stdin.read().split())
      a.sort(reverse=True)
      dp = [-inf]*(n+10); dp[0] = 0
      for i in range(n):
        for j in a: dp[i+c[j]] = max(dp[i+c[j]], dp[i]+1)
      d = [None] * dp[n]
      for i in range(dp[n]):
        for j in a:
          if dp[n-c[j]]+1 != dp[n]: continue 
          d[i] = j; n -= c[j]; break
      print(''.join(map(str, d)))
      
  class ABC119:
    @staticmethod 
    def d():
      a, b, q, *I = map(int, sys.stdin.read().split())
      s, t, x = np.array([-inf]+I[:a]+[inf]), np.array([-inf]+I[a:a+b]+[inf]), np.array(I[-q:])
      sl = np.searchsorted(s, x, side='right')-1
      tl = np.searchsorted(t, x, side='right')-1
      sr = np.searchsorted(s, x, side='left')
      tr = np.searchsorted(t, x, side='left')
      sl, sr, tl, tr = x-s[sl], s[sr]-x, x-t[tl], t[tr]-x
      res = np.vstack([
        np.maximum(sl, tl),
        np.maximum(sr, tr),
        sl*2 + tr,
        sl + tr*2,
        sr*2 + tl,
        sr + tl*2,
      ]).min(axis=0).astype(int)
      print(*res, sep='\n')
      
  class ABC120:
    @staticmethod 
    def d():
      n, m, *ab = map(int, sys.stdin.read().split())
      c = [None]*m; c[-1] = n*(n-1)//2
      *ab, = zip(*[iter(ab)]*2)
      uf = GeometryTopology.Graph(n); uf.init_dsu()
      for i in range(m-1, 0, -1):
        a, b = ab[i]; a -= 1; b -= 1
        c[i-1] = c[i]
        if uf.same(a,b): continue 
        c[i-1] -= uf.size[uf.find(a)]*uf.size[uf.find(b)]
        uf.unite(a, b)
      print(*c, sep='\n')

  class ABC121:
    @staticmethod 
    def d():
      def f(n):
        i = 1<<np.arange(n.bit_length())
        a = n//(i<<1)*i + np.maximum(0, n%(i<<1)-i+1)
        return ((a&1)*i).sum()
      a, b = map(int, sys.stdin.readline().split())
      print(f(b)^f(a-1))
    
    @staticmethod 
    def d_2():
      def f(n): return ((n+1)>>1&1) + (~n&1)*n
      a, b = map(int, sys.stdin.readline().split())
      print(f(b)^f(a-1))

  class ABC122:
    @staticmethod 
    def d():
      n = int(sys.stdin.readline().rstrip())
      dp = [defaultdict(int) for _ in range(n+1)]; dp[0][''] = 1

      def ng(s):
        if 'AGC' in s: return True 
        s = list(s)
        for i in range(len(s)-1):
          s[i],s[i+1] = s[i+1],s[i]
          if 'AGC' in ''.join(s): return True 
          s[i],s[i+1] = s[i+1],s[i]
        return False
      
      for i in range(n):
        for s, cnt in dp[i].items():
          for c in 'ACGT':
            t = s+c 
            if ng(t): continue
            t = t[-3:] 
            dp[i+1][t] += cnt 
            dp[i+1][t] %= MOD 
      print(sum(dp[-1].values())%MOD)

  class ABC123:
    @staticmethod 
    def d_1():
      x, y, z, k, *I = map(int, sys.stdin.read().split())
      I = np.array(I)
      a, b, c = I[:x], I[x:x+y], I[x+y:]
      def f(a, b): return np.sort((a[:,None]+b).ravel())[-1:-1-k:-1]
      print(*f(f(a,b), c), sep='\n')

    @staticmethod 
    def d_2():
      x, y, z, K, *I = map(int, sys.stdin.read().split())
      a, b, c = sorted(I[:x], reverse=1), sorted(I[x:x+y], reverse=1), sorted(I[x+y:], reverse=1)
      added = set()
      q = [(-(a[0]+b[0]+c[0]),0,0,0)]; added.add((0,0,0))
      res = []
      for _ in range(K):
        v, i, j, k = heappop(q)
        v = -v; res.append(v)
        if i<x-1 and not (i+1,j,k) in added:
          heappush(q, (-(v-a[i]+a[i+1]),i+1,j,k)); added.add((i+1,j,k))
        if j<y-1 and not (i,j+1,k) in added:
          heappush(q, (-(v-b[j]+b[j+1]),i,j+1,k)); added.add((i,j+1,k))
        if k<z-1 and not (i,j,k+1) in added:
          heappush(q, (-(v-c[k]+c[k+1]),i,j,k+1)); added.add((i,j,k+1))
      print(*res, sep='\n')

    @staticmethod 
    def d_3():
      x, y, z, K, *I = map(int, sys.stdin.read().split())
      a, b, c = sorted(I[:x], reverse=1), sorted(I[x:x+y], reverse=1), sorted(I[x+y:], reverse=1)
      cand = []
      for i in range(1, x+1):
        if i>K: break
        for j in range(1, y+1):
          if i*j > K: break 
          for k in range(1, z+1):
            if i*j*k > K: break 
            cand.append(a[i-1]+b[j-1]+c[k-1])
      print(*sorted(cand, reverse=1)[:K], sep='\n')


  class ABC124:
    @staticmethod 
    def d():
      pass
      
  class ABC125: pass
  class ABC126: pass
  class ABC127: pass
  class ABC128: pass
  class ABC129: pass
  class ABC130: pass
  class ABC131: pass
  class ABC132: pass
  class ABC133: pass
  class ABC134: pass
  class ABC135: pass
  class ABC136: pass
  class ABC137: pass
  class ABC138:
    @staticmethod 
    def d():
      n, q, *I = map(int, sys.stdin.read().split())
      I = list(zip(*[iter(I)]*2))
      c = [0] * n
      for p, x in I[n-1:]: c[p-1] += x 
      parent = [None] * n
      g = [[] for _ in range(n)]
      for a, b in I[:n-1]:
        a -= 1; b -= 1
        g[a].append(b); g[b].append(a)
      def dfs(u):
        for v in g[u]:
          if v == parent[u]: continue 
          parent[v] = u; c[v] += c[u]; dfs(v)
      dfs(0)
      print(*c)

  class ABC139: pass
  class ABC140: pass
  class ABC141: pass
  class ABC142: pass
  class ABC143: pass
  class ABC144: pass
  class ABC145: pass
  class ABC146: pass
  class ABC147: pass
  class ABC148: pass
  class ABC149: pass
  class ABC150: pass
  class ABC151: pass
  class ABC152: pass
  class ABC153: pass
  class ABC154: pass
  class ABC155: pass
  class ABC156: pass
  class ABC157: pass
  class ABC158: pass
  class ABC159: pass
  class ABC160: pass
  class ABC161: pass
  class ABC162: pass
  class ABC163: pass
  class ABC164: pass
  class ABC165: pass
  class ABC166: pass
  class ABC167: pass
  class ABC168: pass
  class ABC169: pass

  class ABC170:
    @staticmethod
    def a():
      x = [int(x) for x in sys.stdin.readline().split()]
      for i in range(5):
        if x[i] != i+1:
          print(i+1)
          break
    
    @staticmethod
    def b():
      x, y = map(int, sys.stdin.readline().split())
      print('Yes' if 2*x <= y <= 4*x and y%2 == 0 else 'No')
    @staticmethod
    def c():
      x, n, *p = map(int, sys.stdin.read().split())
      a = list(set(range(102)) - set(p))
      a = [(abs(y-x), y) for y in a]
      print(sorted(a)[0][1])
    
    @staticmethod
    def d():
      n, *a = map(int, sys.stdin.read().split())
      cand = set(a)
      cnt = 0
      for x, c in sorted(Counter(a).items()):
        cnt += c == 1 and x in cand
        cand -= set(range(x*2, 10**6+1, x))
      print(cnt)

    @staticmethod
    def e():
      n, q = map(int, sys.stdin.readline().split())
      queue = [] 
      m = 2*10**5
      infants = [[] for _ in range(m)]
      highest_rate = [None] * m
      where = [None] * n
      rate = [None] * n

      def entry(i, k):
        where[i] = k
        while infants[k]:
          r, j = heappop(infants[k])
          if where[j] != k or j == i: continue 
          if rate[i] >= -r:
            highest_rate[k] = rate[i]
            heappush(queue, (rate[i], k, i))
          heappush(infants[k], (r, j))
          break
        else:
          highest_rate[k] = rate[i]
          heappush(queue, (rate[i], k, i))
        heappush(infants[k], (-rate[i], i))

      def transfer(i, k):
        now = where[i]
        while infants[now]:
          r, j = heappop(infants[now])
          if where[j] != now or j == i: continue
          if highest_rate[now] != -r:
            highest_rate[now] = -r
            heappush(queue, (-r, now, j))
          heappush(infants[now], (r, j))
          break
        else:
          highest_rate[now] = None
        entry(i, k)

      def inquire():
        while True:
          r, k, i = heappop(queue)
          if where[i] != k or r != highest_rate[k]: continue 
          heappush(queue, (r, k, i))
          return r

      for i in range(n):
        a, b = map(int, sys.stdin.readline().split())
        rate[i] = a 
        entry(i, b-1)
      for _ in range(q):
        c, d = map(int, sys.stdin.readline().split())
        transfer(c-1, d-1)
        print(inquire())
      


  class ABC171:
    @staticmethod
    def a():
      c = sys.stdin.readline().rstrip()
      print('A' if c < 'a' else 'a')
    
    @staticmethod
    def b():
      n, k, *p = map(int, sys.stdin.read().split())
      print(sum(sorted(p)[:k]))
    

    @staticmethod
    def c():
      n = int(sys.stdin.readline().rstrip())
      n -= 1
      l = 1
      while True:
        if n < pow(26, l):
          break 
        n -= pow(26, l)
        l += 1
      res = ''.join([chr(ord('a')+d) for d in NumberTheory.base_convert(n, 26)][::-1])
      res = 'a'*(l-len(res)) + res
      print(res)
    
    @staticmethod
    def d():
      n = int(sys.stdin.readline().rstrip())
      a = [int(x) for x in sys.stdin.readline().split()]
      s = sum(a)
      cnt = Counter(a)
      q = int(sys.stdin.readline().rstrip())
      for _ in range(q):
        b, c = map(int, sys.stdin.readline().split())
        s += (c-b)*cnt[b]
        print(s)
        cnt[c] += cnt[b]; cnt[b] = 0
    
    @staticmethod
    def e():
      n, *a = map(int, sys.stdin.read().split())
      s = 0
      for x in a: s ^= x 
      b = map(lambda x: x^s, a)
      print(*b, sep=' ')


  class ABC172:
    @staticmethod
    def a():
      a = int(sys.stdin.readline().rstrip()); print(a*(1+a+a**2))
    
    @staticmethod
    def b():
      s, t = sys.stdin.read().split(); print(sum(s[i]!=t[i] for i in range(len(s))))
    
    @staticmethod
    def c():
      n, m, k = map(int, sys.stdin.readline().split())
      a = [0] + [int(x) for x in sys.stdin.readline().split()]
      b = [int(x) for x in sys.stdin.readline().split()]
      *sa, = itertools.accumulate(a)
      *sb, = itertools.accumulate(b)
      res = 0
      for i in range(n+1):
        r = k - sa[i]
        if r < 0: break 
        res = max(res, i+bi_r(sb, r))
      print(res)

    @staticmethod 
    def d():
      n = int(sys.stdin.readline().rstrip())
      f = np.zeros(n+1, dtype=np.int64)
      for i in range(1, n+1):
        f[i::i] += 1
      print((np.arange(1, n+1)*f[1:]).sum())


  class ABC173:
    @staticmethod
    def a():
      n = int(sys.stdin.readline().rstrip())
      charge = (n+999)//1000 * 1000 - n
      print(charge)
    
    @staticmethod
    def b():
      n, *s = sys.stdin.read().split() 
      c = Counter(s)
      for v in 'AC, WA, TLE, RE'.split(', '):
        print(f'{v} x {c[v]}')
    

    @staticmethod
    def c():
      h, w, k = map(int, sys.stdin.readline().split())
      c = [sys.stdin.readline().rstrip() for _ in range(h)]
      tot = 0
      for i in range(1<<h):
        for j in range(1<<w):
          cnt = 0
          for y in range(h):
            for x in range(w):
              if i>>y & 1 or j>>x & 1:
                continue 
              cnt += c[y][x] ==  '#'
          tot += cnt == k
      print(tot)

    @staticmethod
    def d():
      n, *a = map(int, sys.stdin.read().split())
      a.sort(reverse=True)
      res = a[0] + sum(a[1:1+(n-2)//2])*2 + a[1+(n-2)//2]*(n & 1)
      print(res)
    
    @staticmethod
    def e():
      MOD = 10**9+7
      n, k, *a = map(int, sys.stdin.read().split())
      minus = [x for x in a if x < 0]
      plus = [x for x in a if x > 0]
      if len(plus) + len(minus)//2*2 >= k: # plus 
        *minus, = map(abs, minus)
        minus.sort(reverse=True)
        plus.sort(reverse=True)
        cand = []
        if len(minus)&1: minus = minus[:-1]
        for i in range(0, len(minus)-1, 2):
          cand.append(minus[i]*minus[i+1]%MOD)
        if k & 1:
          res = plus[0]
          plus = plus[1:]
        else:
          res = 1
        if len(plus)&1: plus = plus[:-1]
        for i in range(0, len(plus)-1, 2):
          cand.append(plus[i]*plus[i+1]%MOD)
        cand.sort(reverse=True)
        for x in cand[:k//2]:
          res *= x
          res %= MOD 
        print(res)
      elif 0 in a:
        print(0)
      else:
        cand = sorted(map(abs, a))
        res = 1
        for i in range(k):
          res *= cand[i]
          res %= MOD
        res = MOD - res
        print(res)
        pass
 

  class ABC174:
    @staticmethod
    def a():
      print('Yes' if int(sys.stdin.readline().rstrip())>=30 else 'No')





  class ABC179:
    @staticmethod 
    def a():
      s = sys.stdin.readline().rstrip()
      print(s+'s' if s[-1]!='s' else s+'es')

    @staticmethod 
    def b():
      n, *d = map(int, sys.stdin.read().split())
      d = np.array(d).reshape(n, 2).T
      d = np.equal(d[0], d[1]).astype(int)
      dd = d.copy()
      dd[1:] += d[:-1]
      dd[:-1] += d[1:]
      print('Yes' if (dd>=3).any() else 'No')
      


    @staticmethod 
    def c():
      n = int(sys.stdin.readline().rstrip())
      res = (n//np.arange(1, n+1)).sum() - len(NumberTheory.find_divisors(n))
      print(res)


    @staticmethod 
    def d():
      mod = 998244353
      n, k, *lr = map(int, sys.stdin.read().split())
      l, r = np.array(lr).reshape(k, -1).T
      @njit((i8, i8[:], i8[:]), cache=True)
      def solve(n, l, r):
        res = np.zeros(n*2, dtype=np.int64); res[0], res[1] = 1, -1
        for i in range(n-1):
          res[i+1] = (res[i+1]+res[i]) % mod
          res[i+l] = (res[i+l]+res[i]) % mod
          res[i+r+1] = (res[i+r+1]-res[i]) % mod
        print(res[n-1])
      solve(n, l, r)
    
    @staticmethod 
    def e():
      n, x, m = map(int, sys.stdin.readline().split())
      res = [-1 for _ in range(m)]
      s = 0
      loop = np.zeros(m, dtype=np.int64)
      for i in range(m+1):
        if i==n: print(s); return 
        if res[x] != -1:
          l, loop = i-res[x], loop[res[x]:i]
          q, r = divmod(n-i, l)
          print(s+q*loop.sum()+loop[:r].sum()); return
        res[x], loop[i] = i, x
        s += x; x = x**2 % m 


  class ABC180:
    @staticmethod 
    def a():
      n, a, b = map(int, sys.stdin.readline().split())
      print(n-a+b)
      
    @staticmethod 
    def b():
      n, *x = map(int, sys.stdin.read().split())
      x = np.absolute(np.array(x))
      print(x.sum())
      print(np.sqrt((x**2).sum()))
      print(x.max())

    @staticmethod 
    def c():
      n = int(sys.stdin.readline().rstrip())
      div = NumberTheory.find_divisors(n)
      print(*div, sep='\n')

    @staticmethod 
    def d():
      x, y, a, b = map(int, sys.stdin.readline().split())
      cnt = 0
      while x*a <= x+b:
        x *= a 
        if x >= y:
          print(cnt); return 
        cnt += 1
      cnt += (y-x-1) // b 
      print(cnt) 

    @staticmethod
    def e():
      n, *xyz = map(int, sys.stdin.read().split())
      
      xyz = list(zip(*[iter(xyz)] * 3))
      dist = [[0] * n for _ in range(n)]
      for i in range(n):
        a, b, c = xyz[i]
        for j in range(n):
          p, q, r = xyz[j]
          dist[i][j] = abs(p-a) + abs(q-b) + max(0, r-c) 

      dp = [[inf] * n for _ in range(1<<n)]
      dp[0][0] = 0 
      for s in range(1<<n):
        for i in range(n):
          t = s|(1<<i)
          for j in range(n):
            dp[t][i] = min(dp[t][i], dp[s][j]+dist[j][i])
      print(dp[-1][0])
      
          

    @staticmethod 
    def f(): # rewrite with jit compiling later.
      n, m, l = map(int, sys.stdin.readline().split())
      c = Combinatorics.CombinationsMod(n, MOD)
      path = np.zeros(n+1, dtype=np.int64); path[1] = path[2] = 1
      for i in range(3, n+1): path[i] = path[i-1]*i%MOD
      cycle = np.zeros(n+1, dtype=np.int64); cycle[1:] = path[:-1]
      dp = np.zeros((n+1, m+1), dtype=np.int64)
      def f(l):
        dp[:,:] = 0; dp[0,0] = 1
        for i in range(n):
          for j in range(m+1):
            k = np.arange(1, min(l, n-i, m-j+1)+1)
            dp[i+k, j+k-1] += dp[i, j]*c(n-i-1, k-1)%MOD*path[k]%MOD 
            dp[i+k, j+k-1] %= MOD 
            k = np.arange(2, min(l, n-i, m-j)+1)
            dp[i+k, j+k] += dp[i, j]*c(n-i-1, k-1)%MOD*cycle[k]%MOD 
            dp[i+k, j+k] %= MOD 
        return dp[n, m]
      print((f(l)-f(l-1))%MOD)

    @staticmethod 
    def f_2(): # PyPy
      n, m, l = map(int, sys.stdin.readline().split())
      c = Combinatorics.CombinationsMod(n, MOD)
      path = [0] * (n+1); path[1] = path[2] = 1
      for i in range(3, n+1): path[i] = path[i-1]*i%MOD 
      cycle = [0] + path[:-1]
      def f(l):
        dp = [[0]*(m+1) for _ in range(n+1)]; dp[0][0] = 1
        for i in range(n):
          for j in range(m+1):
            for k in range(1, min(l, n-i, m-j+1)+1):
              dp[i+k][j+k-1] += dp[i][j]*c(n-i-1, k-1)%MOD*path[k]%MOD 
              dp[i+k][j+k-1] %= MOD 
            for k in range(1, min(l, n-i, m-j)+1):
              dp[i+k][j+k] += dp[i][j]*c(n-i-1, k-1)%MOD*cycle[k]%MOD 
              dp[i+k][j+k] %= MOD
        return dp[n][m]
      print((f(l)-f(l-1))%MOD)

  
  class ABC181:
    @staticmethod 
    def a():
      n = int(sys.stdin.readline().rstrip())
      print('White' if n&1==0 else 'Black')

    @staticmethod 
    def b():
      n, *ab = map(int, sys.stdin.read().split())
      a, b = np.array(ab).reshape(n,2).T 
      print(((a+b)*(b-a+1)//2).sum())

    @staticmethod 
    def c():
      n, *xy = map(int, sys.stdin.read().split())
      i, j, k  = np.array([*itertools.combinations(range(n),3)]).T
      x, y = np.array(xy).reshape(-1,2).T 
      b = (y[j]-y[i])*(x[k]-x[j]) == (y[k]-y[j])*(x[j]-x[i])
      print('Yes' if b.any() else 'No')

    @staticmethod 
    def d():
      n = sys.stdin.readline().rstrip()
      if len(n)<=2:
        print('Yes' if int(n)%8==0 or int(n[::-1])%8==0 else 'No')
        return 
      c = Counter(n)
      for i in range(112, 1000, 8):
        if not Counter(str(i))-c: print('Yes'); return  
      print('No')

    @staticmethod 
    def e():
      n, m, *I = map(int, sys.stdin.read().split())
      I = np.array(I)
      h, w = np.sort(I[:n]), np.sort(I[-m:])
      tmp = np.pad(h[1:]-h[:-1], 1, constant_values=0)
      l = tmp.copy(); l[::2] = 0; np.cumsum(l, out=l)
      r = tmp.copy(); r[1::2] = 0; np.cumsum(r[::-1], out=r[::-1])
      i = np.searchsorted(w, h)
      d = np.pad(h[2:]-h[:-2], 1, constant_values=0); d[::2] = 0
      d += np.minimum(np.abs(h-w[np.maximum(i-1, 0)]), np.abs(h-w[np.minimum(m-1, i)]))
      print((l[:-1]+r[1:]+d).min())

    @staticmethod 
    def f():
      n, *xy = map(int, sys.stdin.read().split())
      xy = np.array(xy).reshape(n,2)
      y = xy[:, 1]
      if n == 1: print(np.maximum(100-y, y+100)[0]/2); return 
      ij = np.array([*itertools.combinations(range(n),2)])
      d = (np.diff(xy[ij], axis=1)**2).sum(axis=-1).ravel()
      def f(r):
        r *= 2
        uf = GeometryTopology.Graph(n+2); uf.init_dsu()
        for i in np.argwhere(y+100<=r).ravel(): uf.unite(i, n)
        for i in np.argwhere(100-y<=r).ravel(): uf.unite(i, n+1)
        for i, j in ij[np.argwhere(d<=r*r).ravel()]: uf.unite(i, j)
        return uf.same(n, n+1)

      def binary_search():
        lo, hi = 0, 200.1
        while hi-lo > 1e-9:
          r = (lo+hi)/2 
          if f(r): hi = r
          else: lo = r 
        return lo 
      print(binary_search())

  class ABC182:
    @staticmethod 
    def a():
      a, b = map(int, sys.stdin.readline().split())
      print(2*a+100-b)

    @staticmethod
    def b():
      n, *a = map(int, sys.stdin.read().split())
      a = np.array(a)
      c = (a[:,None]%np.arange(2, 1001)==0).sum(axis=0)
      i = np.argsort(c)
      print((i[np.searchsorted(c[i], c[i[-1]]):]).max()+2)

    @staticmethod 
    def c():
      *n, = map(int, list(sys.stdin.readline().rstrip()))
      dp = np.full(3, -np.inf); dp[0] = 0
      i = np.arange(3)
      for d in n: dp[i] = np.maximum(dp[i], dp[(i-d)%3]+1)
      print(len(n)-dp[0].astype(int) if dp[0] else -1) 

    @staticmethod 
    def d():
      n, *a = map(int, sys.stdin.read().split())
      a = np.pad(np.array(a).cumsum(), (1,0))
      b = np.maximum.accumulate(a)
      np.cumsum(a, out=a)
      np.maximum(a[1:], a[:-1]+b[1:], out=a[1:])
      print(a.max())

    @staticmethod 
    def e():
      h, w, n, m, *I = map(int, sys.stdin.read().split())
      I = np.array(I)-1
      g = np.zeros((h,w))
      a, b = I[:2*n].reshape(n,2).T; g[a,b] = 1
      c, d = I[2*n:].reshape(m,2).T; g[c,d] = -1
      def f(g):
        g = g.copy()
        for i in range(1,g.shape[0]): bl = g[i]==0; g[i,bl] = g[i-1,bl]
        return g
      print(np.count_nonzero((f(g)==1)|(f(g[::-1])[::-1]==1)|(f(g.T).T==1)|(f(g.T[::-1])[::-1].T==1)))

    @staticmethod 
    def f():
      n, x, *a = map(int, sys.stdin.read().split())

  class ABC183:
    @staticmethod 
    def a():
      print(max(int(sys.stdin.readline().rstrip()), 0))

    @staticmethod
    def b():
      sx, sy, gx, gy = map(int, sys.stdin.readline().split())
      print((sy*gx+sx*gy)/(sy+gy))

    @staticmethod 
    def c():
      n, k, *t = map(int, sys.stdin.read().split())
      t = np.array(t).reshape(n,n)
      routes = np.array([*itertools.permutations(range(1, n))]).T
      routes = np.pad(routes, pad_width=((1,1), (0,0)), constant_values=0)
      c = t[routes[:-1], routes[1:]].sum(axis=0)
      print(np.count_nonzero(c==k))
    
    @staticmethod 
    def d():
      n, w, *stp = map(int, sys.stdin.read().split())
      s, t, p = np.array(stp).reshape(n,3).T 
      a = np.zeros(2*10**5+10)
      np.add.at(a, s, p); np.add.at(a, t, -p); np.cumsum(a, out=a)
      print('Yes' if np.all(a<=w) else 'No')

    @staticmethod 
    def e():
      h, w = map(int, sys.stdin.readline().split())
      s = [sys.stdin.readline().rstrip() for _ in range(h)]
      x = [[0]*w for _ in range(h)]
      y = [[0]*w for _ in range(h)]
      z = [[0]*w for _ in range(h)]
      c = [[0]*w for _ in range(h)]; c[0][0] = 1
      for i in range(h):
        for j in range(w):
          if s[i][j] == '#': continue 
          if i == j == 0: continue 
          if j > 0: x[i][j] = (x[i][j-1] + c[i][j-1]) % MOD 
          if i > 0: y[i][j] = (y[i-1][j] + c[i-1][j]) % MOD
          if i > 0 and j > 0: z[i][j] = (z[i-1][j-1] + c[i-1][j-1]) % MOD 
          c[i][j] = (x[i][j] + y[i][j] + z[i][j]) % MOD
      print(c[-1][-1])

    @staticmethod 
    def f():
      n, q = map(int, sys.stdin.readline().split())
      c = [defaultdict(int) for _ in range(n)]
      for i, x in enumerate(map(int, sys.stdin.readline().split())): c[i][x-1] += 1
      uf = GeometryTopology.Graph(n); uf.init_dsu()
      for _ in range(q):
        t, x, y = map(int, sys.stdin.readline().split())
        x -= 1; y -= 1
        if t == 1:
          if uf.same(x, y): continue 
          x, y = uf.find(x), uf.find(y)
          if uf.rank[x] < uf.rank[y]: x,y = y,x
          for k, v in c[y].items(): c[x][k] += v
          uf.unite(x, y)
        else:
          x = uf.find(x)
          print(c[x][y])


  class ABC184:
    @staticmethod 
    def a():
      a = np.array(sys.stdin.read().split(), dtype=int).reshape(2,2)
      print(np.rint(np.linalg.det(a)).astype(int))

    @staticmethod 
    def b():
      n, x = map(int, sys.stdin.readline().split())
      s = sys.stdin.readline().rstrip() 
      for c in s: x = x+1 if c=='o' else max(0,x-1)
      print(x)

    @staticmethod 
    def c():
      a, b, c, d = map(int, sys.stdin.read().split())
      c, d = abs(c-a), abs(d-b)
      if c==d==0: print(0) 
      elif c+d==0 or c==d or c+d<=3: print(1) 
      elif abs(c-d) <= 3 or c+d<=6 or ~(c+d)&1: print(2) 
      else: print(3)

    @staticmethod 
    def d():
      a, b, c = map(int, sys.stdin.readline().split())
      @lru_cache(None)
      def dfs(i, j, k):
        if i==100 or j==100 or k==100: return i+j+k-a-b-c  
        return (dfs(i+1,j,k)*i + dfs(i,j+1,k)*j + dfs(i,j,k+1)*k)/(i+j+k)
      print(dfs(a,b,c))

    @staticmethod 
    def e():
      h, w = map(int, sys.stdin.readline().split())
      s = sys.stdin.read().split() 
      g = GeometryTopology.Graph(h*w)

      def o(c): return ord(c) - ord('a')

      a = [[] for _ in range(26)] 

      for i in range(h):
        for j in range(w):
          c = s[i][j]
          u = i*w+j 
          if c == '#': continue
          if c.islower(): a[o(c)].append(u)
          if c == 'S': src = u 
          if c == 'G': dst = u
          for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            y, x = i+dy, j+dx 
            if y<0 or y>=h or x<0 or x>=w or s[y][x]=='#': continue 
            g.add_edge(u, y*w+x, weight=1)
      s = ''.join(s)
      
      d = [inf]*(h*w); d[src] = 0
      q = deque(); q.append(src)
      while q: 
        u = q.popleft()
        for v in g.edges[u]:
          if d[v] != inf: continue 
          d[v] = d[u]+1 
          q.append(v)
        if not s[u].islower(): continue 
        for v in a[o(s[u])]:
          if d[v] != inf: continue 
          d[v] = d[u]+1
          q.append(v)
        a[o(s[u])].clear()

      print(-1 if d[dst]==inf else d[dst])

    @staticmethod 
    def f():
      n, t, *a = map(int, sys.stdin.read().split())

      def f(a):
        n = len(a)
        res = []
        for i in range(1<<n):
          s = sum(a[j] for j in range(n) if i>>j&1)
          res.append(s)
        return sorted(res)
    
      m = n//2 
      b = f(a[m:])
      a = f(a[:m])
      res = []
      for x in a: 
        if x > t: break
        i = bi_r(b, t-x)-1
        res.append(x+b[i])
      print(max(res))

  class ARC106:
    @staticmethod 
    def a():
      n = int(sys.stdin.readline().rstrip())
      a = 1
      while pow(3,a)<=n:
        m, b = n-pow(3,a), 1
        while pow(5,b)<=m:
          if pow(5,b)==m: print(a, b); return
          b += 1
        a += 1
      print(-1)
    
    @staticmethod 
    def b():
      n, m = map(int, sys.stdin.readline().split())
      a = [int(x) for x in sys.stdin.readline().split()]
      b = [int(x) for x in sys.stdin.readline().split()]
      uf = GeometryTopology.Graph(n); uf.init_dsu()
      for _ in range(m):
        c, d = map(int, sys.stdin.readline().split()); c -= 1; d -= 1
        uf.unite(c, d)
      ga, gb = [[] for _ in range(n)], [[] for _ in range(n)]
      for i in range(n):
        r = uf.find(i)
        ga[r].append(a[i]); gb[r].append(b[i])
      print('Yes' if all(sum(ga[i])==sum(gb[i]) for i in range(n)) else 'No')
    
    @staticmethod 
    def c():
      n, m = map(int, sys.stdin.readline().split())
      if m < 0: print(-1); return 
      if n == 1:
        if m != 0: print(-1); return 
        print(1, 2); return
      if m >= n-1: print(-1); return 
      l, r = 1, 10**9
      print(l, r) 
      for _ in range(n-2-m):
        l += 1; r -= 1; print(l, r)
      r = l
      for _ in range(m+1):
        l, r = r+1, r+2
        print(l, r)
    
    @staticmethod 
    def d():
      mod = 998244353
      n, k, *a = map(int, sys.stdin.read().split())
      a = np.array(a)
      b = np.zeros((k+1, n), dtype=np.int64)
      b[0] = 1
      for i in range(k): b[i+1] = b[i]*a%mod
      s = b.sum(axis=1) % mod
      inv_2 = pow(2, mod-2, mod)
      c = Combinatorics.CombinationsMod(mod=mod)
      for x in range(1, k+1):
        l = np.arange(x+1)
        print(((c(x, l)*s[l]%mod*s[l][::-1]%mod).sum()%mod - pow(2,x,mod)*s[x])%mod*inv_2%mod)
    
    @staticmethod 
    def e():
      pass 

    @staticmethod 
    def f():
      pass 
  

  class ARC107:
    @staticmethod
    def a():
      a = np.array(sys.stdin.read().split(), dtype=np.int64)
      print(Algebra.cumprod((1+a)*a//2%MOD, mod=MOD)[2])

    @staticmethod
    def b():
      n, k = map(int, sys.stdin.readline().split())
      def c(m): return np.minimum(m-1,2*n-m+1)
      x = np.arange(2, 2*n+1)
      print((c(x)*c(x-k)*((x-k>=2)&(x-k<=2*n))).sum())


    @staticmethod 
    def c():
      n, k, *a = map(int, sys.stdin.read().split())
      a = np.array(a).reshape(n,n)
      fac, _ = Algebra.generate_fac_ifac(n=50, p=MOD)
      def count(a):
        uf = GeometryTopology.Graph(n); uf.init_dsu()
        for i, j in itertools.combinations(range(n),2):
          if (a[i]+a[j] <= k).all(): uf.unite(i,j)
        c = 1
        for g in uf.groups():
          if g: c *= fac[len(g)]; c %= MOD 
        return c 
      print(count(a)*count(a.T)%MOD)

    @staticmethod 
    def d():
      n, k = map(int, sys.stdin.readline().split())
      @njit((i8,i8), cache=True)
      def solve(n, k):
        dp = np.zeros((n+1, 2*n+1), dtype=np.int64); dp[0,0] = 1
        for i in range(1, n+1):
          for j in range(i, 0, -1):
            dp[i,j] = dp[i-1,j-1] + dp[i,2*j]
            dp[i,j] %= MOD
        return dp[-1,k]
      print(solve(n,k))

    @staticmethod 
    def e():
      pass 

    @staticmethod 
    def f():
      pass 

  class ARC108:
    @staticmethod 
    def a():
      s, p = map(int, sys.stdin.readline().split())
      divs = NumberTheory.find_divisors(p)
      for n in divs:
        if p//n == (s-n): print('Yes'); return 
      print('No')

    @staticmethod 
    def b():
      n = int(sys.stdin.readline().rstrip())
      s = sys.stdin.readline().rstrip()
      stack = []
      for c in s:
        if not stack:
          if c != 'f': continue 
          stack.append(c)
        else:
          # if c not in set('fox'): stack=[]; continue
          if stack[-1]=='f':
            if c=='f' or c=='o': stack.append(c)
            else: stack=[]; continue
          elif stack[-1]=='o':
            if c=='f': stack.append(c)
            elif c=='x':
              stack.pop()
              stack.pop()
              n -= 3
            else: stack=[]; continue
      print(n)


    @staticmethod 
    def c():
      pass 


  class ARC110:
    @staticmethod 
    def a():
      n = int(sys.stdin.readline().rstrip())
      pn = NumberTheory.PrimeNumbers()
      res = defaultdict(int)
      for i in range(2, n+1):
        tmp = pn.factorize(i)
        for m, v in tmp.items():
          res[m] = max(res[m], v)

      m = 1 
      for x, c in res.items():
        m *= x**c 
      print(m+1)

    @staticmethod 
    def b():
      n, t = sys.stdin.read().split() 
      n = int(n)
      s = '101' * 3*10**5
      if not t in (s[:n], s[1:n+1], s[2:n+2]): 
        print(0); return 
      l = 3*10**10 
      if n == 1: 
        print(l//3 if t=='0' else l//3*2); return 
      if t[:2] == '11': print((l-n+3)//3)
      if t[:2] == '10': print((l-n+2)//3)
      if t[:2] == '01': print((l-n+1)//3)


    
    @staticmethod 
    def c():
      n, *p = map(int, sys.stdin.read().split())
      lis = DP.LIS(p[::-1])
      l = bi_l(lis, inf)
      if l > 2: print(-1); return
      p = [x-1 for x in p]
      idx = [None] * n 
      for i, x in enumerate(p): idx[x] = i
 
      big_left = [0] * n 
      small_right = [0] * n 
      bit = GeometryTopology.FenwickTree(n)
      for i, x in enumerate(p):
        bit.add(x+1, 1)
        big_left[i] = i+1 - bit.sum(1, x+1)
      
      bit = GeometryTopology.FenwickTree(n)
      for i, x in enumerate(reversed(p)):
        bit.add(x+1, 1)
        small_right[-1-i] = bit.sum(1, x)

      for i, x in enumerate(p):
        if x-i==-big_left[i]+small_right[i]: continue 
        print(-1); return 
      
      res = []
      for i in range(n): 
        while idx[i] > i:
          j = idx[i]
          res.append(j)
          x = p[j-1]
          idx[i], idx[x], p[j], p[j-1] = j-1, j, i, x
      
      if len(res) != n-1: print(-1); return 
      print(*res, sep='\n')




    

      




  class ACL001:
    @staticmethod 
    def a():
      n, *xy = map(int, sys.stdin.read().split())
      *xy, = zip(*[iter(xy)]*2)
      print(xy)
      pass
  


  class TDPC:
    @staticmethod
    def t():
      pass

  
  class ChokudaiSpecialRun001:
    @staticmethod 
    def j():
      n, *a = map(int, sys.stdin.read().split())
      bit = GeometryTopology.FenwickTree(n)
      c = 0 
      for x in a:
        c += bit.sum(1,n) - bit.sum(1,x)
        bit.add(x,1)
      print(c)

  class ALPC: # AtCoder Library Practice Contest\
    @staticmethod 
    def a():
      n, q, *tuv = map(int, sys.stdin.read().split())
      uf = GeometryTopology.Graph(n); uf.init_dsu()
      for t, u, v in zip(*[iter(tuv)]*3):
        if t == 0: uf.unite(u,v)
        else: print(int(uf.same(u,v)))


    @staticmethod 
    def b():
      n, q = map(int, sys.stdin.readline().split())
      a = [int(x) for x in sys.stdin.readline().split()]
      bit = GeometryTopology.FenwickTree(n)
      for i in range(n): bit.add(i+1, a[i])
      for t, i, j in zip(*[map(int, sys.stdin.read().split())]*3):
        if t==0: bit.add(i+1,j)
        else: print(bit.sum(i+1,j))    


    @staticmethod 
    def g():
      n, m, *ab = map(int, sys.stdin.read().split())
      a, b = np.array(ab).reshape(m,2).T
      _, r = connected_components(csr_matrix(([1]*m, (a,b)), (n,n)), connection='strong')
      groups = [[] for _ in range(n)]
      for u in range(n): groups[r[u]].append(u)
      groups = [group for group in groups if group]
      print(len(groups))
      for group in groups[::-1]: print(len(group), *group)


  class MSolutions2020:
    @staticmethod
    def a():
      x = int(sys.stdin.readline().rstrip())
      x -= 400
      print(8-x//200)
    
    @staticmethod
    def b():
      r, g, b, k = map(int, sys.stdin.read().split())
      while k and g <= r:
        g *= 2
        k -= 1
      while k and b <= g:
        b *= 2
        k -= 1
      print('Yes' if r < g < b else 'No')
    
    @staticmethod
    def c():
      n, k, *a = map(int, sys.stdin.read().split())
      for i in range(k, n):
        print('Yes' if a[i] > a[i-k] else 'No')
    
    @staticmethod
    def d():
      n, *a = map(int, sys.stdin.read().split())
      a += [-1]
      m = 1000
      s = 0
      for i in range(n):
        if a[i+1] == a[i]: continue 
        elif a[i+1] > a[i]:
          cnt = m//a[i]
          m -= a[i]*cnt 
          s += cnt 
        else:
          m += a[i]*s
          s = 0
      print(m)

  class AGC040:
    @staticmethod 
    def a():
      s = sys.stdin.readline().rstrip()
      n = len(s)+1
      a = [None] * n; a[0] = 0 
      for i in range(n-1):
        a[i+1] = a[i] + (1 if s[i]=='<' else -1)
      
      
      print(a)


class Codeforces:
  class CR676div2:
    @staticmethod 
    def a():
      t = int(sys.stdin.readline().rstrip())
      for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        print(a^b)

    @staticmethod 
    def b():
      t = int(sys.stdin.readline().rstrip())
      for _ in range(t):
        n = int(sys.stdin.readline().rstrip())
        s = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
        s[0][0] = s[-1][-1] = '0'
        for i in range(n):
          for j in range(n):
            s[i][j] = int(s[i][j])


        def can_goal(g, c=0):
          visited = [0] * n 
          stack = [(0, 0)]
          visited[0] |= 1<<0
          while stack:
            y, x = stack.pop()
            for dy, dx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
              i, j = y+dy, x+dx
              if i<0 or i>=n or j<0 or j>=n: continue
              if i == j == n-1: return True
              if visited[i]>>j&1: continue
              visited[i] |= 1<<j
              if g[i][j] != c: continue 
              stack.append((i, j))
          return False
        
        if not (can_goal(s, 0) or can_goal(s, 1)):
          print(0)       
          continue

        flg = 0
        for i in range(n):
          for j in range(n):
            if i==j==0 or i==j==n-1: continue 
            s[i][j] ^= 1
            if not (can_goal(s, 0) or can_goal(s, 1)): 
              print(1)
              print(i+1, j+1)
              flg = 1
              break 
            s[i][j] ^= 1
          if flg: break 
        if flg: continue

        print(2)
        if s[0][1] == s[1][0]:
          print(n, n-1)
          print(n-1, n)
          continue 

        if s[0][1] == s[-1][-2]:
          print(1, 2)
          print(n-1, n)
        else:
          print(1, 2)
          print(n, n-1)

      

    @staticmethod 
    def c():
      pass 

class ProjectEuler:
  @staticmethod
  def p1():
    def f(n, x):
      return (x + n//x*x) * (n//x) // 2
    n = 1000
    ans = f(n-1, 3)+f(n-1, 5)-f(n-1, 15)
    print(ans)

  @staticmethod
  def p2():
    fib = [1, 2]
    while fib[-1] < 4*10**6:
      fib.append(fib[-1]+fib[-2])
    print(sum(fib[1:-1:3]))

  @staticmethod
  def p3():
    pn = NumberTheory.PrimeNumbers()
    res = pn.factorize(600851475143)
    print(max(res.keys()))

  @staticmethod
  def p4():
    def is_palindrome(n):
      n = str(n)
      return n == n[::-1]
    cand = []
    for a in range(100, 1000):
      for b in range(a, 1000):
        n = a*b 
        if is_palindrome(n): cand.append(n)
    print(max(cand))

  @staticmethod
  def p5():
    pn = NumberTheory.PrimeNumbers()
    res = defaultdict(int)
    for i in range(1, 21):
      for p, c in pn.factorize(i).items():
        res[p] = max(res[p], c)
    ans = 1
    for p, c in res.items(): ans *= pow(p, c)
    print(ans)

  @staticmethod
  def p6():
    a = np.arange(101)
    b = np.cumsum(a**2)
    a = a.cumsum()
    print(a[100]**2 - b[100])

  @staticmethod
  def p7():
    nt = NumberTheory.PrimeNumbers()
    print(sorted(nt)[10000])
  @staticmethod
  def p8():
    n = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    n = [int(d) for d in list(n)]
    res = 0
    for i in range(988):
      x = 1
      for j in range(13):
        x *= n[i+j]
      res = max(res, x)
    print(res)
  @staticmethod
  def p9():
    for a in range(1, 997):
      for b in range(a, 998-a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
          print(a*b*c)
          return
  @staticmethod
  def p10():
    pn = NumberTheory.PrimeNumbers(2*10**6+1)
    print(sum(pn))
  @staticmethod
  def p11():
    grid = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'
    print(grid)
  
  pass

class Yukicoder:
  def __init__(self):
    pass

  def __call__(self):
    print(1)


class AOJ:
  @staticmethod 
  def ALDS1_12_A(): # minimum spanning tree
    n, *a = map(int, sys.stdin.read().split())
    g = GeometryTopology.Graph(n)
    for i in range(n-1):
      for j in range(i+1, n):
        if a[i*n+j] == -1: continue 
        g.add_edge(i,j, weight=a[i*n+j])
        g.add_edge(j,i, weight=a[i*n+j])
    _, d = g.kruskal()
    # _, d = g.prim()
    # _, d = g.boruvka()
    print(d)
  

  @staticmethod 
  def GRL_3_C(): # strongly connected components 
    n, m = map(int, sys.stdin.readline().split())
    _, r = connecte
    g = GeometryTopology.Graph(n)
    for _ in range(m): g.add_edge(*map(int, sys.stdin.readline().split()))
    r = g.scc()
    q, *uv = map(int, sys.stdin.read().split())
    for u, v in zip(*[iter(uv)] * 2): print(int(r[u]==r[v]))

  
  @staticmethod 
  def DSL_2_B(): # Binary Indexed Tree (Fenwick Tree)
    n, q, *txy = map(int, sys.stdin.read().split())
    bit = GeometryTopology.FenwickTree(n)
    for t, x, y in zip(*[iter(txy)]*3):
      if t==0: bit.add(x, y)
      else: print(bit.sum(x,y))


class YosupoJudge:

  @staticmethod 
  def PointAddRangeSum():
    n, q = map(int, sys.stdin.readline().split())
    a = [int(x) for x in sys.stdin.readline().split()]
    bit = GeometryTopology.FenwickTree(n)
    for i in range(n): bit.add(i+1, a[i])
    for t, i, j in zip(*[map(int, sys.stdin.read().split())]*3):
      if t==0: bit.add(i+1,j)
      else: print(bit.sum(i+1,j))
    
  @staticmethod 
  def Directed_MST():
    n, m, s, *abc = map(int, sys.stdin.read().split())
    g = GeometryTopology.Graph(n)
    for a, b, c in zip(*[iter(abc)]*3):g.add_edge(a, b, weight=c)
    _, d, p = g.prim(src=s, return_parent=True)
    print(d)
    print(*p)

  @staticmethod 
  def Manhattan_MST():
      n, *xy = map(int, sys.stdin.read().split())
      g = GeometryTopology.Graph(n)


if __name__ == '__main__':
  AtCoder.ARC110.b() 
  pass
  