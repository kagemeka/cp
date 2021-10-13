# [AtCoder ARC121 B - RGB Matching](https://atcoder.jp/contests/arc121/tasks/arc121_b)



# keywords 
- math 
- shakutori method 
- binary search
- sort 


# summary
- split $A$ into group $R$, $G$, $B$
- if all group sizes are even, answer = 0 
- otherwize, 
  - make |R|$ even
    - if $|R|$ is even, do nothing
    - if $|G|$ is even, swap $R, G$
    - if $|B|$ is even, swap $R, B$
  - answer is connect $GB$ or connect $GR$ and $RB$ 


# code 
## sol_0
- numba (JIT)



# similar 
