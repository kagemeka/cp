# [AtCoder ABC056 C - Go Home](https://atcoder.jp/contests/abc056/tasks/arc070_a)


# keywords 
- math
- inequality 
- binary search 

# summary 
- $X \le \sum_{i=1}^{t}i$
- $\exists{S, \forall{j} \in S, 1 \le j \lt t}\ X = \sum_{i=1}^{t}i - \sum_{i \in S}i$
- therefore, answer is minimum $t$ such that $X \le \sum_{i=1}^{t}i$
- $t(t + 1) \ge 2X$
- this can be solved with binary search or directly as $t \ge \sqrt{2x + 1/4} - 1/2$

# code 
## sol_0
- python
- binary search

## sol_1
- python
- calculate directly

# similar 

