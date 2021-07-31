# [P - Independent Set](https://atcoder.jp/contests/dp/tasks/dp_p)


# keywords 
- Directed Tree is DAG
- DP on Tree 
- coloring (2 color)
- count up 
- DFS 
- BFS
- childs give to their parent.
- parent receieve from the childs.
- $$ dp_{u,b} = \prod_{v\in{child_u}} dp_{v, w}$$
- $$ dp_{u,w} = \prod_{v\in{child_u}} {dp_{v, w} + dp_{v, b}}$$


## sol_0
- DFS
- standard 



## sol_1
- find route with stack and receive in reverse order.
- standard



## sol_2
- find depth of each node and give bottom up with BFS.
- standard


## sol_3
