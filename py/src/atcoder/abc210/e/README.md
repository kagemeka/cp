# [AtCoder ABC210 E - Ring MST](https://atcoder.jp/contests/abc210/tasks/abc210_e)



# keywords 
- minimum spanning gree (MST)
- kruskal algorithm 
- simulation
- gcd
- sort edges
- greedy 



# summary 
- fast Kruskal algorithm simulation
  - add edges in order of their cost $c_i$ in ascending as much as possible (greedy).
- now, $c_1 \le c_2 \le... \le c_n$
- let $g$ is the number of connected components in the graph. $g_0 = N$
- the number of connected components after $op_i$ is, $g_i = \gcd(g_{i - 1}, a_i)$
- $op_i$ will be conducted the times equal to $g_i - g_{i - 1}$
- $\text{answer}= \begin{cases}
  -1 & \text{if } g_M > 1 \\
  \sum_{i=1}^{M} c_i \times (g_i - g_{i - 1}) & \text{otherwise}
  \end{cases}$
  

# code 

## sol_0, sol_1
- numba (JIT)



# similar