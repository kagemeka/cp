# [AtCoder Typical90 009 - Three Point Angle（★6）](https://atcoder.jp/contests/typical90/tasks/typical90_i)



# keywords 
- geometry
- triangle
- degree $\degree$ 
- argument
- fix target point 
- sort by radian or degree.
- shakutori method 
- binary search 



# summary 
- fix $P_j$
  - sort other points with degree of vector $P_i - P_j$ ($0 \le deg \lt 360$)
  - calc $\max_{deg_k - deg_i \le 180, i \lt k}{deg_k - deg_i}$ with shakutori method $O(N)$ (or binary search $O(N\log{N}))$.
- total to $O(N^2\log{N})$



# code 
## sol_0
- numba (JIT)
- shakutori method


# similar 
- [AtCoder ABC033 D - 三角形の分類](https://atcoder.jp/contests/abc033/tasks/abc033_d)