package main

import (
	"container/list"

)



// AtCoder .
var AtCoder = proconSite{
	Contests: map[string]Contest{

		"ABC034": {
			"A": func() {
				var x, y int 
				fmt.Scan(&x, &y)
				var ans string 
				if y>x {ans = "Better"} else {ans = "Worse"}
				fmt.Println(ans)	
			},

			"B": func() {
				n := ScanInt() 
				if n&1==1 {fmt.Println(n+1)} else {fmt.Println(n-1)}
			},

			"C": func() {
				cn := Combinatorics{}; cn.Init(2e6,Mod)
				var w, h int 
				fmt.Scan(&w, &h)
				fmt.Println(cn.ChooseMod(w+h-2, h-1))

			},


		"ABC035": {
			"A": func() {
				var w, h int 
				fmt.Scan(&w, &h)
				if w*3==h*4 {fmt.Println("4:3")} else {fmt.Println("16:9")}
			},

			"B": func() {
				s, t := Scan(), ScanInt() 
				z, y, x := 0, 0, 0 
				for _, c := range s {
					if c == '?' {z++}
					if c == 'U' {y++}
					if c == 'D' {y--}
					if c == 'L' {x--}
					if c == 'R' {x++}
				}
				a := AbsInt(y) + AbsInt(x)
				if t == 1 {fmt.Println(a+z)} else {fmt.Println(MaxInt(a-z, (a-z)&1))}
			},

			"C": func() {
				var n, q int
				fmt.Scan(&n, &q)
				s := make([]int, n+1)
				for i := 0; i < q; i++ {
					l, r := ScanInt(), ScanInt(); l--; r--
					s[l]++; s[r+1]--
				}
				
				res := make([]string, n)
				for i := 0; i < n; i++ {
					s[i+1] += s[i]
					res[i] = strconv.Itoa(s[i]&1)
				}
				fmt.Println(strings.Join(res, ""))
			},

		
		},

		"ABC036": {
			"A": func() {
				var a, b int; fmt.Scan(&a, &b)
				fmt.Println((b+a-1)/a )
			},

			"B": func() {
				n := ScanInt()
				s := make([][]rune, n)
				for i := 0; i < n; i++ {
					s[i] = []rune(Scan())
				}
				t := make([][]rune, n)
				for i := 0; i < n; i++ {
					t[i] = make([]rune, n)
				}
				for i := 0; i < n; i++ {
					for j := 0; j < n; j++ {
						t[i][j] = s[n-1-j][i]
					}
				}
				for i := 0; i < n; i++ {fmt.Println(string(t[i]))}
			},

			"C": func() {
				n := ScanInt() 
				a := make([]int, n); for i := 0; i < n; i++ {a[i] = ScanInt()}
				tmp := make([][2]int, n)
				for i := 0; i < n; i++ {tmp[i] = [2]int{i, a[i]}}
				sort.SliceStable(tmp, func(i, j int) bool {return tmp[i][1] <= tmp[j][1]})
				b := make([]string, n)
				prev := -1
				for i, j := 0, -1; i < n; i++ {
					k, x := tmp[i][0], tmp[i][1]
					if x != prev {j++}
					b[k] = strconv.Itoa(j)
					prev = x
				}
				writer.WriteString(strings.Join(b, "\n")); writer.Flush()
			},
	

		"ABC037": {
			"A": func() {
				var a, b, c int 
				fmt.Scan(&a, &b, &c)
				fmt.Println(c/MinInt(a,b))
			},

			"B": func() {
				n, q := ScanInt(), ScanInt() 
				a := make([]int, n)
				for i := 0; i < q; i++ {
					l, r, t := ScanInt(), ScanInt(), ScanInt() 
					l--; r--
					for j := l; j < r+1; j++ {a[j] = t}
				}
				for i := 0; i < n; i++ {fmt.Println(a[i])}
			},

			"C": func() {
				n, k := ScanInt(), ScanInt()
				a := make([]int, n+1)
				for i := 1; i < n+1; i++ {a[i] = ScanInt()}
				for i := 0; i < n; i++ {a[i+1] += a[i]}
				s := 0
				for i := k; i < n+1; i++ {s += a[i]-a[i-k]}
				fmt.Println(s)
			},


		"ABC038": {
			"A": func() {
				s := Scan() 
				if s[len(s)-1] == 'T' {fmt.Println("YES")} else {fmt.Println("NO")}
			},

			"B": func() {
				var h1, w1, h2, w2 int 
				fmt.Scan(&h1, &w1, &h2, &w2)
				ans := "NO"
				if h1==h2 || h1==w2 || w1==h2 || w1==w2 {ans = "YES"}
				fmt.Println(ans)
			},
			"C": func() {
				n := ScanInt() 
				a := make([]int, n+1)
				for i := 0; i < n; i++ {a[i] = ScanInt()}
				

				tot := n
				cnt := 0
				prev := Inf 
				for i := 0; i < n+1; i++ {
					if a[i] <= prev {tot += cnt*(cnt-1)/2; cnt=1} else {cnt++}
					prev = a[i]	
				}
				fmt.Println(tot)
			},

		"ABC039": {
			"A": func() {
				var a, b, c int 
				fmt.Scan(&a, &b, &c)
				fmt.Println(2*(a*b+b*c+c*a))
			},
			"B": func() {
				x := ScanInt() 

				binarySearch := func() int {
					lo, hi := 1, 200
					for lo+1 < hi {
						n := (lo+hi)/2
						if Pow(n, 4) <= x {lo=n} else {hi=n}

					}
					return lo
				}
				fmt.Println(binarySearch())
			},

			"C": func() {
				board := strings.Repeat("WBWBWWBWBWBW", 3)
				conv := strings.Split("Do, *, Re, *, Mi, Fa, *, So, *, La, *, Si", ", ")
				s := Scan()
				fmt.Println(conv[strings.Index(board, s)])
			},

			"D": func() {
				h, w := ScanInt(), ScanInt() 
				var s string 
				for i := 0; i < h; i++ {s += Scan()}

				f := func(x int) (u, d, l, r int) {
					i, j := Divmod(x, w)
					if i > 0 {u = -w}
					if i < h-1 {d = w}
					if j > 0 {l = -1}
					if j < w-1 {r = 1}
					return 
				}

				white := make([]bool, h*w)
				for i := 0; i < h*w; i++ {
					if s[i]=='#' {continue}
					u, d, l, r := f(i)
					for dy := u; dy < d+1; dy+=w {
						for dx := l; dx < r+1; dx++ {
							white[i+dy+dx] = true
						}
					}
				}
				black := make([]bool, h*w)
				for i := 0; i < h*w; i++ {
					if white[i]==true {continue}
					u, d, l, r := f(i)
					for dy := u; dy < d+1; dy+=w {
						for dx := l; dx < r+1; dx++ {
							black[i+dy+dx] = true
						}
					}
				}

				for i := 0; i < h*w; i++ {
					if s[i]=='#' && !black[i] {fmt.Println("impossible"); return}
				}
				fmt.Println("possible")
				for i := 0; i < h; i++ {
					row := make([]rune, w)
					for j := 0; j < w; j++ {
						if white[i*w+j] {row[j] = '.'} else {row[j] = '#' }
					}
					fmt.Println(string(row))
				}
			},
		},

		"ABC040": {
			"A": func() {
				n, x := ScanInt(), ScanInt() 
				fmt.Println(MinInt(x-1, n-x))
			},

			"B": func() {
				n := ScanInt()
				
				res := Inf
				for i := 1; i*i <= n; i++ {
					j, r := Divmod(n, i)
					res = MinInt(res, j-i+r)
				}
				fmt.Println(res)

					
			},

			"C": func() {
				n := ScanInt() 
				a := make([]int, n+1)
				for i := 1; i < n+1; i++ {a[i] = ScanInt()}
				a[0] = a[1]
				dp := make([]int, n+1)
				cost := func(i,j int) int {return dp[j]+AbsInt(a[i]-a[j])}
				for i := 2; i < n+1; i++ {
					dp[i] = MinInt(cost(i, i-2), cost(i, i-1))
				}
				fmt.Println(dp[n])
			},

			"D": func() {
				n, m := ScanInt(), ScanInt()
				uf := new(UnionFind); uf.Init(n)
				q := make([][3]int, 0)
				for i := 0; i < m; i++ {
					a, b, y := ScanInt(), ScanInt(), ScanInt(); a--; b--
					q = append(q, [3]int{2*y, a, b})
				}

				r := ScanInt() 
				for i := 0; i < r; i++ {
					u, y := ScanInt(), ScanInt(); u--
					q = append(q, [3]int{2*y+1, u, i})
				}

				sort.SliceStable(q, func(i,j int) bool {return q[i][0] > q[j][0]})

				// fmt.Println(q)
				res := make([]int, r)
				for _, tmp := range q {
					y, i, j := tmp[0], tmp[1], tmp[2]
					if y&1==1 {res[j] = uf.size[uf.Find(i)]} else {uf.Unite(i, j)}
				}
				for _, i := range res {fmt.Println(i)}
			
			},
		},

		"ABC041": {
			"A": func() {
				s, i := Scan(), ScanInt() 
				fmt.Println(string(s[i-1]))
			},

			"B": func() {
				var a, b, c int 
				fmt.Scan(&a, &b, &c)
				fmt.Println(a*b%Mod*c%Mod)
			},

			"C": func() {
				n := ScanInt() 
				a := make([][2]int, n)
				for i := 0; i < n; i++ {a[i][0], a[i][1] = i+1, ScanInt()}
				sort.Slice(a, func(i, j int) bool {return a[i][1] > a[j][1]})
				for i := 0; i < n; i++ {fmt.Println(a[i][0])}
			},

			"D": func() {
				n, m := ScanInt(), ScanInt() 
				g := make([]int, n)
				for i := 0; i < m; i++ {
					x, y := ScanInt(), ScanInt(); x--; y--
					g[x] |= 1<<y
				}
				
				res := make([]int, 1<<n); res[0] = 1 
				for i := 0; i < 1<<n; i++ {
					for j := 0; j < n; j++ {
						if i>>j&1==0 || g[j]&i!=0 {continue}
						res[i] += res[i&BitwiseNot(1<<j)]
					}
				}
				fmt.Println(res[1<<n-1])
			},
		},

		"ABC042": {
			"A": func() {
				const n = int(3)
				a := make([]int, n)
				for i := 0; i < n; i++ {a[i]= ScanInt()}
				sort.Slice(a, func(i, j int) bool {return a[i] < a[j]})
				ans := "NO"; if a[0]==5 && a[1]==5 && a[2]==7 {ans = "YES"}
				fmt.Println(ans)
			},

			"B": func() {
				n, _ := ScanInt(), ScanInt() 
				s := make([]string, n)
				for i := 0; i < n; i++ {s[i] = Scan()}
				sort.Strings(s)
				fmt.Println(strings.Join(s, ""))
			},

			"C": func() {
				n, m := []rune(Scan()), ScanInt()
				n = append(make([]rune, 1), n...)

				d := make(map[rune]bool)
				for i := 0; i < m; i++ {d[[]rune(Scan())[0]] = true}
				l := len(n)
				
				a := make([]rune, l)
				flg := false
				for i := 1; i < l; i++ {
					if flg {
						for j := '0'; j <= '9'; j++ {if !d[j] {a[i] = j; break}}
					}	else {
						if !d[n[i]] {a[i] = n[i]; continue}
						for j := n[i]+1; j <= '9'; j++ {
							if !d[j] {a[i] = j; flg=true; break}
						}
						if flg {continue}
						for j := '0'; j < n[i]; j++ {if !d[j] {a[i] = j; break}}
						for k := i-1; k > 0; k-- {
							for j := n[k]+1; j <= '9'; j++ {
								if !d[j] {a[k] = j; flg=true; break}
							}
							if flg {break}
							for j := '0'; j < n[k]; j++ {if !d[j] {a[k] = j; break}}
						}
						if flg {continue}
						for j := '1'; j <= '9'; j++ {if !d[j] {a[0] = j; flg=true; break}}
					}
				} 
				
				if a[0]==0 {fmt.Println(string(a[1:]))} else {fmt.Println(string(a))}
			},

			"D": func() {
				var h, w, a, b int 
				fmt.Scan(&h, &w, &a, &b)
				cn := Combinatorics{}; cn.Init(2e5, Mod)
				ng := 0
				for i := 0; i < a; i++ {
					ng += cn.ChooseMod(b-1+h-1-i, b-1) * cn.ChooseMod(i+w-1-b, i)
					ng %= Mod 
				}
				fmt.Println(((cn.ChooseMod(h+w-2, h-1)-ng)%Mod+Mod)%Mod)

			},
		},

		"ABC043": {
			"A": func() {
				n := ScanInt() 
				fmt.Println((1+n)*n/2)
			},

			"B": func() {
				s := Scan()

				t := "" 
				for _, c := range s {
					if c!='B' {t += string(c); continue}
					if len(t)==0 {continue}
					t = t[:len(t)-1]
				}
				fmt.Println(t)
			},

			"C": func() {
				n := ScanInt() 
				a := make([]int, n)
				for i := 0; i < n; i++ {a[i] = ScanInt()}
				m := int(math.Round(float64(SumInt(a...))/float64(n)))
				tot := 0
				for _, x := range a {tot += Pow(m-x, 2)}
				fmt.Println(tot)

			},

			"D": func() {
				s := Scan()
				n := len(s)
				for i := 0; i < n-1; i++ {
					if s[i]==s[i+1] {fmt.Println(i+1, i+2); return}
				}
				for i := 1; i < n-1; i++ {
					if s[i-1]==s[i+1] {fmt.Println(i, i+2); return}
				}
				fmt.Println(-1, -1)
			},
		},

		"ABC044": {
			"A": func() {
				var n, k, x, y int
				fmt.Scan(&n, &k, &x, &y)
				fmt.Println(MinInt(n,k)*x + MaxInt(0,n-k)*y)
			},

			"B": func() {
				s := Scan()
				cnt := make(map[rune]int)
				for _, c := range s {cnt[c] ^= 1}
				for _, v := range cnt {
					if v==1 {fmt.Println("No"); return}
				}
				fmt.Println("Yes")
			},

			"C": func() {
				n, a := ScanInt(), ScanInt() 
				x := make([]int, n)
				for i := 0; i < n; i++ {x[i] = ScanInt()}
				dp := make([][]int, n+1)
				for i := 0; i < n+1; i++ {dp[i] = make([]int, 2501)}
				dp[0][0] = 1
				for _, v := range x {
					for i := n; i > 0; i-- {
						for j := v; j < 2501; j++ {
							dp[i][j] += dp[i-1][j-v]
						}
					}
				}
				s := 0
				for i := 1; i < n+1; i++ {s += dp[i][i*a]}
				fmt.Println(s)
			},
		},


		"ABC045": {
			"A": func() {
				var a, b, h int 
				fmt.Scan(&a, &b, &h)
				fmt.Println((a+b)*h/2)
			},

			"B": func() {
				var a, b, c string
				fmt.Scan(&a, &b, &c)
				d := make(map[rune][]rune);
				d['a'] = []rune(ReversedString(a))
				d['b'] = []rune(ReversedString(b))
				d['c'] = []rune(ReversedString(c))
				nx := 'a';
				for {
					l := len(d[nx])
					if l==0 {fmt.Printf("%c\n", unicode.ToUpper(nx)); return}
					d[nx], nx = d[nx][:l-1], d[nx][l-1]
				}
			},

			"C": func() {
				s := Scan(); l := len(s)

				tot := 0
				c := func(l int) int {return 1<<MaxInt(0,l-1)}
				for i := 0; i < l; i++ {
					for j := i; j < l; j++ {
						n, _ := strconv.Atoi(s[i:j+1])
						tot += n * c(i) * c(l-1-j)
					}
				}
				fmt.Println(tot)
			},

			"D": func() {
				var h, w, n int
				fmt.Scan(&h, &w, &n)
				cnt := make(map[[2]int]int)
				for k := 0; k < n; k++ {
					y, x := ScanInt()-1, ScanInt()-1
					for dy := -1; dy < 2; dy++ {
						for dx := -1; dx < 2; dx++ {
							i, j := y+dy, x+dx 
							if !(0<i && i<h-1 && 0<j && j<w-1) {continue}
							cnt[[2]int{i,j}]++
						}
					}
				}
				var res [10]int; res[0] = (h-2)*(w-2)
				for _, c := range cnt {res[c]++; res[0]--}
				for i := 0; i < 10; i++ {fmt.Println(res[i])}
			},
		},

		"ABC046": {
			"A": func() {
				s := make(map[int]bool)
				for i := 0; i < 3; i++ {
					s[ScanInt()] = true  
				}
				fmt.Println(len(s))
			},

			"B": func() {
				n, k := ScanInt(), ScanInt() 
				fmt.Println(k*Pow(k-1, n-1))
			},
			"C": func() {
				n := ScanInt() 
				x, y := 1, 1
				for i := 0; i < n; i++ {
					a, b := ScanInt(), ScanInt() 
					m := MaxInt((x+a-1)/a, (y+b-1)/b)
					x, y = a*m, b*m
				}
				fmt.Println(x+y)
			},

			"D": func() {
				s := Scan() 
				c := 0
				for i := 0; i < len(s); i++ {c += Booltoi(s[i]=='p')}
				fmt.Println(len(s)/2 - c)
			},
		},

		"ABC047": {
			"A": func() {
				a := make([]int, 3)
				for i := 0; i < 3; i++ {a[i] = ScanInt()}
				sort.Ints(a)
				if a[0]+a[1]==a[2] {fmt.Println("Yes")} else {fmt.Println("No")}
			},

			"B": func() {
				var w, h, n int 
				fmt.Scan(&w, &h, &n)

				l, r, u, d := 0, w, h, 0
				for i := 0; i < n; i++ {
					x, y, a := ScanInt(), ScanInt(), ScanInt() 
					switch a {
					case 1: l = MaxInt(l, x)
					case 2: r = MinInt(r, x)
					case 3: d = MaxInt(d, y)
					case 4: u = MinInt(u, y)
					}
				}
				fmt.Println(MaxInt(0,r-l)*MaxInt(0,u-d))
			},

			"C": func() {
				s := Scan()
				c := 0 
				for i := 0; i < len(s)-1; i++ {c += Booltoi(s[i]!=s[i+1])}
				fmt.Println(c)
			},

			"D": func() {
				n, _ := ScanInt(), ScanInt() 
				a := make([]int, n)
				for i := 0; i < n; i++ {a[i] = ScanInt()}
				mx := 0
				mn := a[0]
				cnt := 0
				for i := 1; i < n; i++ {
					d := a[i] - mn 
					if d > mx {mx, cnt = d, 1} else if d == mx {cnt++}
					mn = MinInt(mn, a[i])
				}
				fmt.Println(cnt)
			},
		},

		"ABC048": {
			"A": func() {
				s := make([]byte, 3)
				for i := 0; i < 3; i++ { s[i] = Scan()[0]}
				fmt.Println(string(s))
			},

			"B": func() {
				a, b, x := ScanInt(), ScanInt(), ScanInt() 
				f := func(n int) int {if n==-1 {return -1}; return n/x}
				fmt.Println(f(b)-f(a-1))
			},

			"C": func() {
				n, x := ScanInt(), ScanInt() 
				a := make([]int, n+1)
				for i := 0; i < n; i++ {a[i+1] = ScanInt()}
				c := 0 
				for i := 1; i < n+1; i++ {
					d := a[i-1]+a[i]-x
					if d <= 0 {continue}
					a[i] -= d; c += d
				}
				fmt.Println(c)
				
			},

			"D": func() {
				s := Scan() 
				l := len(s)
				ans := "First" 
				if  ((l&1) ^ Booltoi(s[0]==s[l-1])) == 0 {ans = "Second"}
				fmt.Println(ans)
			},
		},

		"ABC049": {
			"A": func() {
				vowel := make(map[rune]bool)
				for _, c := range "aeiou" {vowel[c] = true}
				c := Scan()
				if vowel[[]rune(c)[0]] {fmt.Println("vowel")} else {fmt.Println("consonant")}
			},

			"B": func() {
				h, _ := ScanInt(), ScanInt() 
				for i := 0; i < h; i++ {
					s := Scan()
					for i := 0; i < 2; i++ {fmt.Println(s)}
				}

			},

			"C": func() {
				s := Scan() 
				c := map[string]bool{
					"dream": true,
					"dreamer": true,
					"erase": true,
					"eraser": true,
				}

				for len(s)>0 {
					l := len(s)
					if c[s[l-5:]] {
						s = s[:l-5]
					} else if c[s[l-6:]] {
						s = s[:l-6]
					} else if c[s[l-7:]]{
						s = s[:l-7]
					} else {
						fmt.Println("NO"); return
					}
				}
				fmt.Println("YES")
			},

			"D": func() {
				var n, k, l int 
				fmt.Scan(&n, &k, &l)
				uf1 := new(UnionFind); uf1.Init(n)
				uf2 := new(UnionFind); uf2.Init(n)
				for i := 0; i < k; i++ {
					uf1.Unite(ScanInt()-1, ScanInt()-1)
				}
				for i := 0; i < l; i++ {
					uf2.Unite(ScanInt()-1, ScanInt()-1)
				}
				c := make(map[[2]int]int)
				for i := 0; i < n; i++ {
					c[[2]int{uf1.Find(i), uf2.Find(i)}]++
				}
				a := make([]int, n)
				for i := 0; i < n; i++ {a[i] = c[[2]int{uf1.Find(i), uf2.Find(i)}]}
				fmt.Fprintln(writer, strings.Trim(fmt.Sprint(a), "[]"))
				writer.Flush()

			},
		},

		"ABC050": {
			"A": func() {
				a, op, b := ScanInt(), Scan(), ScanInt() 
				if op=="+" {fmt.Println(a+b)} else {fmt.Println(a-b)}
			},

			"B": func() {
				n := ScanInt() 
				t := make([]int, n); s := 0
				for i := 0; i < n; i++ {
					t[i] = ScanInt(); s += t[i]
				}
				m := ScanInt() 
				for i := 0; i < m; i++ {
					p, x := ScanInt()-1, ScanInt() 
					fmt.Println(s+(x-t[p]))
				}
			},

			"C": func() {
				n := ScanInt() 
				a := make([]int, n)
				c := make(map[int]int)
				for i := 0; i < n; i++ {
					a[i] = ScanInt(); c[a[i]]++
				}
				if n&1==1 {
					if c[0] != 1 {fmt.Println(0); return}
					for i := 2; i < n/2; i+=2 {if c[i]!=2 {fmt.Println(0); return}}
				} else {
					for i := 1; i < n/2; i+=2 {if c[i]!=2 {fmt.Println(0); return}}
				}
				fmt.Println(Pow(2, n/2, Mod))
			},

			"D": func() {

			},
		},

		"ABC051": {
			"A": func() {
				s := Scan()
				fmt.Println(strings.ReplaceAll(s, ",", " "))
			},
			
			"B": func() {
				k, s := ScanInt(), ScanInt()
				c := 0 
				for x := 0; x <= k; x++ {
					if s-x < 0 {break}
					if s-x > 2*k {continue}
					if s-x <= k {c += s-x+1} else {c += 2*k-(s-x)+1}
				}
				fmt.Println(c)
			},

			"C": func() {
				var sx, sy, tx, ty int 
				fmt.Scan(&sx, &sy, &tx, &ty)
				x, y := tx-sx, ty-sy
				t := ""
				t += strings.Repeat("U", y)
				t += strings.Repeat("R", x+1)
				t += strings.Repeat("D", y+1)
				t += strings.Repeat("L", x+1)
				t += "UL"
				t += strings.Repeat("U", y+1)
				t += strings.Repeat("R", x+1)
				t += strings.Repeat("D", y+1)
				t += strings.Repeat("L", x)
				fmt.Println(t)
			},

			"D": func() {
				n, m := ScanInt(), ScanInt() 
				a, b, c := make([]int, m), make([]int, m), make([]int, m)
				g := new(Graph); g.Init(n)
				for i := 0; i < m; i++ {
					a[i], b[i], c[i] = ScanInt()-1, ScanInt()-1, ScanInt()
					g.AddEdge(a[i], b[i], &Edge{weight:c[i]})
					g.AddEdge(b[i], a[i], &Edge{weight:c[i]})
				}
				d := g.FloydWarshall()
				cnt := m
				for i := 0; i < m; i++ {
					for j := 0; j < n; j++ {
						if d[j][a[i]]+c[i] == d[j][b[i]] {cnt--; break}
					}
				}
				fmt.Println(cnt)
			},
			
		},

		"ABC052": {
			"A": func() {
				var a, b, c, d int 
				fmt.Scan(&a, &b, &c, &d)
				fmt.Println(MaxInt(a*b, c*d))
			},
			"B": func() {
				_, s := ScanInt(), Scan()
				x, mx := 0, 0
				for _, c := range s {
					if c=='I' {x++} else {x--}
					mx = MaxInt(mx, x)
				}
				fmt.Println(mx)
			},
			"C": func() {
				n := ScanInt()
				pn := new(PrimeNumbers); pn.Init(n)
				tot := 1
				for _, c := range pn.FactorizeFactorial(n) {
					tot *= (c+1)
					tot %= Mod 
				}
				fmt.Println(tot)
			},

			"D": func() {
				var n, a, b int 
				fmt.Scan(&n, &a, &b)
				x := make([]int, n)
				for i := 0; i < n; i++ {x[i] = ScanInt()}
				tot := 0
				for i := 0; i < n-1; i++ {tot += MinInt(b, a*(x[i+1]-x[i]))}
				fmt.Println(tot)
			},
		},

		"ABC053": {
			"A": func() {
				x := ScanInt()
				if x < 1200 {fmt.Println("ABC")} else {fmt.Println("ARC")}
			},

			"B": func() {
				s := Scan()
				fmt.Println(strings.LastIndex(s, "Z")-strings.Index(s, "A")+1)
			},

			"C": func() {
				x := ScanInt() 
				q, r := Divmod(x, 11)
				fmt.Println(2*q + (r+5)/6)
			},

			"D": func() {
				n := ScanInt()
				s := make(map[int]bool)
				for i := 0; i < n; i++ {s[ScanInt()] = true}
				fmt.Println(len(s) - (n-len(s))&1)
			},
		},

		"ABC054": {
			"A": func() {
				f := func(x int) int {return (x+11)%13}
				a, b := ScanInt(), ScanInt() 
				ans := "Draw"
				if f(a)>f(b) {ans = "Alice"} else if f(a)<f(b) {ans = "Bob"}
				fmt.Println(ans)
			},

			"B": func() {
				n, m := ScanInt(), ScanInt() 
				a, b := make([]string, n), make([]string, m)
				for i := 0; i < n; i++ {a[i] = Scan()}
				for i := 0; i < m; i++ {b[i] = Scan()}

				f := func(y, x int) bool {
					for i := 0; i < m; i++ {
						for j := 0; j < m; j++ {
							if a[y+i][x+j] != b[i][j] {return false}
						}
					}
					return true
				}

				for y := 0; y < n-m+1; y++ {
					for x := 0; x < n-m+1; x++ {
						if f(y, x) {fmt.Println("Yes"); return}
					}
				}
				fmt.Println("No")
			},

			"C": func() {
				n, m := ScanInt(), ScanInt() 
				g := new(Graph); g.Init(n)
				for i := 0; i < m; i++ {
					a, b := ScanInt()-1, ScanInt()-1
					g.AddEdge(a, b, &Edge{weight:1})
					g.AddEdge(b, a, &Edge{weight:1})
				}

				var dfs func(u, s int) int
				dfs = func(u, s int) int {
					if s == (1<<n)-1 {return 1}
					cnt := 0
					for v := range g.edges[u] {
						if s>>v&1==1 {continue}
						cnt += dfs(v, s|(1<<v))
					}
					return cnt
				}
				fmt.Println(dfs(0, 1))
			},

			"D": func() {
				var n, ma, mb int; fmt.Scan(&n, &ma, &mb)
				m := 400
				dp := make([][]int, m+1)
				for i := 0; i < m+1; i++ {
					dp[i] = make([]int, m+1)
					for j := 0; j < m+1; j++ {dp[i][j] = Inf}
				}
				dp[0][0] = 0
				for k := 0; k < n; k++ {
					var a, b, c int; fmt.Scan(&a, &b, &c)
					for i := m; i > -1; i-- {
						if i<a {continue}
						for j := m; j > -1; j-- {
							if j<b {continue}
							dp[i][j] = MinInt(dp[i][j], dp[i-a][j-b]+c)
						}
					}
				}
				res := Inf
				for i := 1; i < m/MaxInt(ma,mb); i++ {
					res = MinInt(res, dp[i*ma][i*mb])
				}
				if res == Inf {fmt.Println(-1); return}
				fmt.Println(res)
			},
		},

		"ABC055": {
			"A": func() {
				n := ScanInt() 
				fmt.Println(800*n - n/15*200)
			},

			"B": func() {
				n := ScanInt() 
				fac, _ := GenerateFacIFac(n, Mod)
				fmt.Println(fac[n])
			},

			"C": func() {
				n, m := ScanInt(), ScanInt() 
				if n*2 <= m {
					fmt.Println(n+(m-n*2)/4)
				} else {
					fmt.Println(m/2)
				}
			},

			"D": func() {
				n, s := ScanInt(), Scan() 
				a := make([]int, n)
				for i := 0; i < n; i++ {
					if s[i]=='o' {a[i] = 1} else {a[i] = 0}
				}
				impossible := func(b []int) (bool, []int) {
					for i := 1; i < n-1; i++ {b[i+1] = b[i-1]^b[i]^a[i]}
					return (b[0]^a[0]^b[1]^b[n-1])|(b[n-1]^a[n-1]^b[n-2]^b[0])==1, b
				}
				b := make([]int, n)
				for _, x := range [][2]int{{1,0},{0,1},{1,1},{0,0}} {
					b[0], b[1] = x[0], x[1]
					bl, b := impossible(b); if bl {continue}
					res := make([]rune, n)
					for i := 0; i < n; i++ {
						if b[i]==1 {res[i]='S'} else {res[i]='W'}
					}
					fmt.Println(string(res)); return
				}
				fmt.Println(-1)

			},
		},

		"ABC056": {
			"A": func() {
				f := func(x string) int {
					if x=="H" {return 1}
					return 0
				}
				a, b := Scan(), Scan()
				if f(a)^f(b)==0 {fmt.Println("H")} else {fmt.Println("D")}
			},

			"B": func() {
				var w, a, b int 
				fmt.Scan(&w, &a, &b)
				if a>b {a, b = b, a}
				fmt.Println(MaxInt(0, b-w-a))
			},

			"C": func() {
				x := float64(ScanInt())
				fmt.Println(int(math.Ceil(math.Sqrt(2*x+.25)-.5)))
			},

			"D": func() {
				n, k := ScanInt(), ScanInt() 
				a := make([]int, n)
				for i := 0; i < n; i++ {a[i] = MinInt(ScanInt(), k)}
				sort.Ints(a)
				necessary := func(i int) bool {
					dp := make([]int, k); dp[0] = 1
					for j := 0; j < n; j++ {
						if j==i {continue}
						for l := k-1; l > -1; l-- {
							if l-a[j] < 0 {break}
							dp[l] |= dp[l-a[j]]
						}
					}
					for j := k-a[i]; j < k; j++ {if dp[j]==1 {return true}}
					return false
				}

				binarySearch := func() {
					lo, hi := -1, n
					for hi-lo > 1 {
						i := (lo+hi)/2
						if necessary(i) {hi = i} else {lo = i}
					}
					fmt.Println(hi)
				}
				binarySearch()

			},
		},

		"ABC057": {
			"A": func() {
				a, b := ScanInt(), ScanInt() 
				fmt.Println((a+b)%24)
			},

			"B": func() {
				n, m := ScanInt(), ScanInt() 
				a, b := make([][2]int, n), make([][2]int, m)
				for i := 0; i < n; i++ {
					a[i][0], a[i][1] = ScanInt(), ScanInt()
				}
				for i := 0; i < m; i++ {
					b[i][0], b[i][1] = ScanInt(), ScanInt()
				}
				for i := 0; i < n; i++ {
					dist := Inf
					var k int
					for j := 0; j < m; j++ {
						d := AbsInt(b[j][0]-a[i][0]) + AbsInt(b[j][1]-a[i][1])
						if d < dist {dist, k = d, j+1}
					}
					fmt.Println(k)
				}
			},
			"C": func() {
				n := ScanInt() 
				d := FindDivisors(n)
				fmt.Println(len(strconv.Itoa(d[len(d)/2])))
			},

			"D": func() {
				
			},

		},


		"ABC179": {
			"D": func() {
				mod := 998244353
				var n, k int; fmt.Scan(&n, &k);
				l, r := make([]int, k), make([]int, k);
				for i := 0; i < k; i++ {l[i], r[i] = ScanInt(), ScanInt()};
				s := make([]int, n*2); s[0], s[1] = 1, -1;
				for i := 0; i < n-1; i++ {
					s[i+1] = (s[i+1]+s[i])%mod;
					for j := 0; j < k; j++ {
						s[i+l[j]] = (s[i+l[j]]+s[i])%mod;
						s[i+r[j]+1] = ((s[i+r[j]+1]-s[i])%mod+mod)%mod;
					}
				}
				fmt.Println(s[n-1]);
			},

			"E": func() {
				var n, x, m int; fmt.Scan(&n, &x, &m)
				res := make([]int, m); for i := 0; i < m; i++ {res[i] = -1}
				s := 0;
				loop := make([]int, m)
				for i := 0; i < m+1; i++ {
					if i==n {fmt.Println(s); return}
					if res[x] != -1 {
						l := i-res[x]
						loop = loop[res[x]:i]
						q, r := Divmod(n-i, l)
						fmt.Println(s+q*SumInt(loop...)+SumInt(loop[:r]...)); return
					}
					res[x], loop[i] = i, x;
					s += x; x = x*x%m 
				}
			},
		},

		"ABC180": {
			"A": func() {
				var n, a, b int; fmt.Scan(&n, &a, &b)
				fmt.Println(n-a+b)
			},

			"B": func() {
				n := ScanInt()
				x := make([]int, n)
				for i := 0; i < n; i++ {x[i] = AbsInt(ScanInt())}
				fmt.Println(SumInt(x...))
				d := 0
				for i := 0; i < n; i++ {d += x[i]*x[i]}
				fmt.Println(NthRoot(float64(d), 2))

				fmt.Println(MaxInt(x...))
			},

			"C": func() {
				n := ScanInt()
				div := FindDivisors(n);
				for _, d := range div {fmt.Fprintln(writer, d)}
				writer.Flush()
			},

			"D": func() {
				var x, y, a, b int 
				fmt.Scan(&x, &y, &a, &b)
				cnt := 0
				for {
					if y/a < x {break}
					if x*a >= y {break}
					if x*a > x+b {break}
					x *= a; cnt++
				}
				fmt.Println(cnt+(y-x-1)/b)
			},

			"E": func() {
				n := ScanInt() 
				x, y, z := make([]int, n), make([]int, n), make([]int, n)
				for i := 0; i < n; i++ {
					x[i], y[i], z[i] = ScanInt(), ScanInt(), ScanInt() 
				}
				dist := make([][]int, n); for i := 0; i < n; i++ {dist[i] = make([]int, n)}
				for i := 0; i < n; i++ {
					for j := 0; j < n; j++ {
						dist[i][j] = AbsInt(x[j]-x[i])+AbsInt(y[j]-y[i])+MaxInt(0, z[j]-z[i])
					}
				}
				dp := make([][]int, 1<<n); 
				for i := 0; i < 1<<n; i++ {
					dp[i] = make([]int, n)
					for j := 0; j < n; j++ {
						dp[i][j] = Inf
					}
				}
				dp[0][0] = 0;
				for s := 0; s < 1<<n; s++ {
					for i := 0; i < n; i++ {
						for t,j := s|1<<i,0; j < n; j++ {dp[t][i] = MinInt(dp[t][i], dp[s][j]+dist[j][i])}
					}
				}
				fmt.Println(dp[1<<n-1][0])
			},

			"F": func() {
				var n, m, l int; fmt.Scan(&n, &m, &l)
				cn := Combinatorics{}; cn.Init(n, Mod)
				path, cycle := make([]int, n+1), make([]int, n+1)
				path[1], path[2] = 1, 1
				for i := 3; i < n+1; i++ {path[i] = path[i-1]*i%Mod}
				for i := 2; i < n+1; i++ {cycle[i] = path[i-1]}

				f := func (l int) int {
					dp := make([][]int, n+1)
					for i := 0; i < n+1; i++ {dp[i] = make([]int, m+1)}
					dp[0][0] = 1
					for  i := 0; i < n; i++ {
						for j := 0; j < m+1; j++ {
							for k := 1; k <= MinInt(l, n-i, m-j+1); k++ {
								dp[i+k][j+k-1] += dp[i][j]*cn.ChooseMod(n-i-1, k-1)%Mod*path[k]%Mod
								dp[i+k][j+k-1] %= Mod
							}
							for k := 2; k <= MinInt(l, n-i, m-j); k++ {
								dp[i+k][j+k] += dp[i][j]*cn.ChooseMod(n-i-1, k-1)%Mod*cycle[k]%Mod
								dp[i+k][j+k] %= Mod
							}
						}
					}
					return dp[n][m]
				}
				fmt.Println(((f(l)-f(l-1))%Mod+Mod)%Mod)
			},
		},

		"ABC181": {
			"A": func() {
				if ScanInt()&1==1 {fmt.Println("Black")} else {fmt.Println("White")}
			},

			"B": func() {
				n := ScanInt()
				tot := 0
				for n > 0 {
					a, b := ScanInt(), ScanInt() 
					tot += (a+b)*(b-a+1)/2
					n--;
				}
				fmt.Println(tot)
			},

			"C": func() {
				n := ScanInt() 
				x, y := make([]int, n), make([]int, n)
				for i := 0; i < n; i++ {x[i], y[i] = ScanInt(), ScanInt()}
				for i := 0; i < n; i++ {
					for j := i+1; j < n; j++ {
						for k := j+1; k < n; k++ {
							if (x[k]-x[j])*(y[j]-y[i])==(x[j]-x[i])*(y[k]-y[j]) {
								fmt.Println("Yes"); return
							}
						}
					}
				}
				fmt.Println("No")
			},

			"D": func() {
				s := Scan()
				if len(s) < 3 {
					var n int; var bl bool;
					n, _ = strconv.Atoi(s)
					if n%8==0 {bl = true}
					n, _ = strconv.Atoi(ReversedString(s))
					if n%8==0 {bl = true}
					if bl {fmt.Println("Yes")} else {fmt.Println("No")}
					return 
				}
				var cnt, c [10]int 
				for _, d := range s {cnt[d-'0']++}
				for i := 112; i < 1000; i+=8 {
					for j := 0; j < 10; j++ {c[j] = 0}
					for _, d := range strconv.Itoa(i) {c[d-'0']++}
					for j := 0; j < 10; j++ {if c[j] > cnt[j] {goto nxt}}
					fmt.Println("Yes"); return
					nxt:
				}
				fmt.Println("No")
				
			},

			"E": func() {
				n, m := ScanInt(), ScanInt()
				h, w := make([]int, n), make([]int, m)
				for i := 0; i < n; i++ {h[i] = ScanInt()}
				for i := 0; i < m; i++ {w[i] = ScanInt()}
				sort.Ints(h); sort.Ints(w)
				l, r := make([]int, n), make([]int, n)
				for i := 1; i < n-1; i+=2 {l[i] = h[i]-h[i-1]}
				for i := n-2; i > 0; i-=2 {r[i] = h[i+1]-h[i]}
				for i := 0; i < n-1; i++ {l[i+1] += l[i]}
				for i := n-1; i > 0; i-- {r[i-1] += r[i]}
				d := make([]int, n)
				for i := 1; i < n-1; i+=2 {d[i] = h[i+1]-h[i-1]}
				k, mn := 0, Inf 
				for i := 0; i < n; i++ {
					for k < m-1 && AbsInt(w[k+1]-h[i]) <= AbsInt(w[k]-h[i]) {k++}
					mn = MinInt(mn, l[MaxInt(i-1,0)]+r[MinInt(i+1,n-1)]+d[i]+AbsInt(w[k]-h[i]))
				}
				fmt.Println(mn)
			},

			"F": func() {
				n := ScanInt() 
				x, y := make([]int, n), make([]int, n)
				for i := 0; i < n; i++ {
					x[i], y[i] = ScanInt(), ScanInt()
				}
				dist := func(i, j int) float64 {
					dx, dy := x[j]-x[i], y[j]-y[i]
					return float64(dx*dx + dy*dy)
				}
				ok := func(r float64) bool {
					r *= 2
					uf := new(UnionFind); uf.Init(n+2);
					for i := 0; i < n; i++ {
						if float64(100-y[i]) < r {uf.Unite(i, n)}
						if float64(y[i]+100) < r {uf.Unite(i, n+1)}
					}
					for i := 0; i < n; i++ {
						for j := i+1; j < n; j++ {
							if dist(i, j) < r*r {uf.Unite(i, j)}
						}
					}
					return !uf.Same(n, n+1)
				}
				lo, hi := .0, 100.1
				for i := 0; i < 100; i++ {
					r := (lo+hi)/2 
					if ok(r) {lo = r} else {hi = r}
				}
				fmt.Println(lo)

			},
		},

		"ABC183": {
			"A": func() {
				fmt.Println(MaxInt(ScanInt(), 0))
			},

			"B": func() {
				var sx, sy, gx, gy float64
				fmt.Scan(&sx, &sy, &gx, &gy)
				fmt.Println((sx*gy+sy*gx)/(sy+gy))
			},

			"C": func() {
				n, k := ScanInt(), ScanInt() 
				t := make([][]int, n)
				for i := 0; i < n; i++ {t[i] = make([]int, n)}
				for i := 0; i < n; i++ {
					for j := 0; j < n; j++ {
						t[i][j] = ScanInt()
					}
				}
				tot := 0
				a := make([]int, n-1)
				for i := 0; i < n-1; i++ {a[i] = i+1}
				for _, p := range Permutations(n-1, n-1) {
					d := t[0][a[p[0]]]
					for i := 0; i < n-2; i++ {d += t[a[p[i]]][a[p[i+1]]]}
					d += t[a[p[n-2]]][0]
					tot += Booltoi(d==k)
				}
				fmt.Println(tot)
			},

			"D": func() {
				n, w := ScanInt(), ScanInt() 
				m := int(2e5)+10
				a := make([]int, m)
				for i := 0; i < n; i++ {
					s, t, p := ScanInt(), ScanInt(), ScanInt() 
					a[s] += p; a[t] -= p 
				}
				for i := 0; i < m-1; i++ {
					if a[i] > w {fmt.Println("No"); return}
					a[i+1] += a[i]
				}
				fmt.Println("Yes")
			},

			"E": func() {
				h, w := ScanInt(), ScanInt() 
				s := make([]string, h)
				for i := 0; i < h; i++ {s[i] = Scan()}
				x := make([][]int, h)
				y := make([][]int, h)
				z := make([][]int, h)
				c := make([][]int, h)
				for i := 0; i < h; i++ {
					x[i] = make([]int, w)
					y[i] = make([]int, w)
					z[i] = make([]int, w)
					c[i] = make([]int, w)
				}
				c[0][0] = 1
				for i := 0; i < h; i++ {
					for j := 0; j < w; j++ {
						if s[i][j] == '#' {continue}
						if i==0 && j==0 {continue}
						if i>0 {y[i][j] = (y[i-1][j]+c[i-1][j])%Mod}
						if j>0 {x[i][j] = (x[i][j-1]+c[i][j-1])%Mod}
						if i>0&&j>0 {z[i][j] = (z[i-1][j-1]+c[i-1][j-1])%Mod}
						c[i][j] = (x[i][j]+y[i][j]+z[i][j])%Mod
					}
				}
				fmt.Println(c[h-1][w-1])
			},

			"F": func() {
				n, q := ScanInt(), ScanInt()
				c := make([]map[int]int, n)
				for i := 0; i < n; i++ {
					c[i] = make(map[int]int)
					c[i][ScanInt()-1] = 1
				}
				uf := new(UnionFind); uf.Init(n)
				for i := 0; i < q; i++ {
					t, x, y := ScanInt(), ScanInt()-1, ScanInt()-1
					if t==1 {
						if uf.Same(x,y) {continue}
						x, y = uf.Find(x), uf.Find(y)
						if uf.rank[x] < uf.rank[y] {x,y = y,x}
						for k, v := range(c[y]) {
							c[x][k] += v
						}
						uf.Unite(x,y)
					} else {
						fmt.Println(c[uf.Find(x)][y])
					}
				}
			},

		},
	},
}

