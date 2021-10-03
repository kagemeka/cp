# [AtCoder ABC023 C - 収集王](https://atcoder.jp/contests/abc023/tasks/abc023_c)


# keywords 
- bincounting 
- inclusion exclusion principle 
- calc $x, y$ axes independently. 


# summary
- calc $\text{bin}_x$
- calc $\text{bin}_{\text{bin}_x}$
- also calc $\text{bin}_y, \text{bin}_{\text{bin}_y}$
- let res $:= \sum_{i=0}^{K}\text{bin}_{\text{bin}_x}(i)\text{bin}_{\text{bin}_y}(K - i)$
- this result still wrong because it's containing some actual $K - 1$ patterns but actual $K$




# code 
## sol_0
- numpy


# similar 
