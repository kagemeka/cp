# [LeetCode Weekly Contest 256](https://leetcode.com/contest/weekly-contest-256)



# [LeetCode 1986. Minimum Number of Work Sessions to Finish the Tasks](https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/)



# keywords 
- similar to (TSP)traveling salesperson problem 
- permutation dp -> `group + last one` dp
- greedy
- brute force



# summary 
## like TSP
- $dp_{s, i} := (c, t)$ 
  - where $s$ denotes a group and $i$ denotes the last task. 
  - $c$ is the count of session and the current session time by then.
- at first
  - $dp_{s, i} = (inf, 0)$
  - $\forall{i}\ dp_{\{i\}, i} = (0, a_i)$ where $a_i$ is the time for $task_i$ 
- transition
  - $dp_{s, i} = \min_{j \in s - \{i\}}{dp_{s - \{i\}, j} + (0, a_i)}$
  - $$(c, t) + (0, a_i) = 
    \begin{dcases}
    (c + 1, a_i), & \text{if } t + a_i > t_0(\text{session time})\\ 
    (c, t + a_i), & \text{otherwise} 
    \end{dcases}$$
- $\text{ans} = \min_{i}\lceil{dp_{all, i}}\rceil$
  - $$\lceil{(c, t)}\rceil = 
    \begin{dcases}
    c & \text{if } t = 0\\
    c + 1 & \text{otherwise}
    \end{dcases}$$
- $O(2^NN^2)$

## Actually, it's not needed to record the last task.
- $O(2^NN)$



## sol_0
- buttom up
- for loop 
- $O(2^NN^2)$


## sol_1
- buttom up
- for loop 
- $O(2^NN)$


## sol_1
- top down 
- dfs
- $O(2^NN)$





# similar
- [ABC180 E - Traveling Salesman among Aerial Cities](https://atcoder.jp/contests/abc180/tasks/abc180_e)
- [ABC215 E - Chain Contestant](https://atcoder.jp/contests/abc215/tasks/abc215_e)