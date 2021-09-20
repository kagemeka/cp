# [AtCoder Typical90 017 - Crossing Segments（★7）](https://atcoder.jp/contests/typical90/tasks/typical90_q)


# keywords
- count up 
- remove complementary cases
- cumulative sum
- choose
- Fenwick Tree
- range -> 2d plotting 
- scanning algorithm



# summary
- consider removing complementary cases from all cases.
- all cases $= \displaystyle{M\choose{2}}$
- complementary cases
  - let two segment $s, t$
  1. common end point.
    - count bin of $l, r$. $b$
    - cnt $= \sum_{i=1}^{N}{\displaystyle{b_i\choose{2}}} $
  2. exclusive cases.
    - $s_r \lt t_l$
    - let $s_i := \sum_{j=0}^{i} \text{bin}_r$
      - cumulative sum 
    - cnt $= \sum_{i=1}^{M} s_{l_i}$
  3. inclusive cases.
    - sort $l, r (\forall{i, j, i \lt j}\ l_i \lt l_j \lor l_i = l_j \land r_i \lt r_j)$
    - using fenwick tree
    - range -> 2d plotting 
    - similar
      - [AtCoder ABC174 F - Range Set Query](https://atcoder.jp/contests/abc174/tasks/abc174_f)


# code 
## sol_0
- numba (JIT)


# similar 
- [AtCoder ABC174 F - Range Set Query](https://atcoder.jp/contests/abc174/tasks/abc174_f)