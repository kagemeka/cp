# [E - Amusement Park](https://atcoder.jp/contests/abc216/tasks/abc216_e)


# keywords 
- greedy 
- binary search 
- scanline algorithm 



# summary
## scanline
- $O(N\log{N})$ (sort is bottoleneck)
- sort A in descending order
- sol_0



## binary search
- $O(N\log{\max{A}})$
- find $x$ such that Takahashi can ride all the attractions which satisfaction are more than or equal to $x$
- sol_1
- similar 
  - [ABC149 E - Handshake](https://atcoder.jp/contests/abc149/tasks/abc149_e)