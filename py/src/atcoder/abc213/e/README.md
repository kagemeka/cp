# [E - Stronger Takahashi](https://atcoder.jp/contests/abc213/tasks/abc213_e)



# keywords
- grid
- graph
- DP
- there two kind of costs(0 or 1).
- 01-BFS
- Dijkstra
- priority queue
- deque(double ended queue)
- greedy



# summary
- consider a shortest_path problem with two kind of moves.
  1. walk
  2. jump
- walk is movement such that 
  $g_{i, j} -> g_{i + di, j + dj}$ with cost 0, where 
  $(di, dj) \in \{(-1, 0), (1, 0), (0, -1), (0, 1)\}$ and
  $g_{i + di, j + dj}$ is not a wall.
- jump is movement such that
  $g_{i, j} -> g_{i + di, j + dj}$ with cost 1, where 
  $-2 \le di, dj \le 2, |di| + |dj| \neq 4, 0$
  $g_{i + di, j + dj}$ is ok wheter it is wall or not.
  if it's a wall, takahashi should punch the area once.
  even if it's not a wall and make a edge with cost 1, it's possible to arrive at goal with minimum cost by using walk,
  as it possible to move $g_{i, j} -> g_{i + di, j + dj}$ with cost 0. 




## sol_0
- 01-BFS


## sol_1 
- Dijkstra 


## sol_2 
- Dijkstra 
- convert char to int





# similar 
- [AtCoder ABC176 D - Wizard in Maze](https://atcoder.jp/contests/abc176/tasks/abc176_d)
- [AtCoder ABC077 D - Small Multiple](https://atcoder.jp/contests/abc077/tasks/arc084_b)