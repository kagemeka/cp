# [AtCoder ABC048 D - An Ordinary Game](https://atcoder.jp/contests/abc048/tasks/arc064_b)


# keywords 
- math 
- consider final situation


# summary 
- consider final situation
- there are only two kind of letters in final situation 
  - e.g. 'abab'
- otherwise
  - if there are more than two kind of letters it's still can be operated.
    - e.g. abc -> ac, cbcba -> cbca -> cba -> ca
- at last, the length of final string must be odd if $S_1 = S_N$ else even.
- therefore, 
$$
\text{answer} = 
\begin{cases}
First & (|S| \& 1 = 1) \oplus (S_1 = S_{|S|}) = 1 \\
Second & \text{otherwise} \\
\end{cases}
$$



# code 
## sol_0
- python

# similar 
