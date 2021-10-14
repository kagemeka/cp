# [AtCoder ABC218 C - Shapes](https://atcoder.jp/contests/abc218/tasks/abc218_c)



# keywords
- matrix rotation 
- string 
- grid 
- compare matrix


# summary 
- trim each shape for $S, T$
- for 4 times
  - rotate T by 90 $\degree{C}$
  - check whether S equal T
  - if equal, print 'Yes'


# tips
- rotate numpy 2D array
  - right: `a = a[::-1].T`
  - left: `a = a.T[::-1]`