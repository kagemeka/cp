

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
