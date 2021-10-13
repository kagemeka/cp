# [AtCoder ABC008 D - 金塊ゲーム](https://atcoder.jp/contests/abc008/tasks/abc008_4)



# keywords 
- count up 
- greedy
- memorized DP
- divide and conquer method
- array compr ession


# summary 
- $dp_{l, r, d, u} :=$ maximum count of golds from $\text{grid}[l:r, d:u]$
- define 
  $$S(x, y) = 
    r - l + u - d + 1
    + dp_{l, x, d, y}
    + dp_{l, x, y + 1, u}
    + dp_{x + 1, r, d, y}
    + dp_{x + 1, r, y + 1, u}
  $$
- transition
  - let $dp_{l, r, d, u} = 0$
  $$dp_{l, r, d, u} = \max{(dp_{l, r, d, u}, \max_{i, l \le X_i \lt r \land d \le Y_i \lt u}{S(X_i, Y_i)})}
  $$

- answer = $dp_{0, W, 0, H}$

# code 
## sol_0, sol_1
- python 
- recursive 


# similar 
