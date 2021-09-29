# [AtCoder ABC047 B - すぬけ君の塗り絵 2 イージー](https://atcoder.jp/contests/abc047/tasks/abc047_b)


# keywords 
- greedy 


# summary
- initialize
  - $x_{mn} := 0$
  - $x_{mx} := w$
  - $y_{mn} := 0$
  - $y_{mx} := h$
- if $a = 1$, $x_{mn} := \max{(x_{mn}, x)}$
- if $a = 2$, $x_{mx} := \min{(x_{mx}, x)}$
- if $a = 3$, $y_{mn} := \max{(y_{mn}, y)}$
- if $a = 4$, $y_{mx} := \min{(y_{mx}, y)}$

# code 
## sol_0
- python 



# similar