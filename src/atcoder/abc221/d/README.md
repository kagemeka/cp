# [AtCoder ABC221 D - Online games](https://atcoder.jp/contests/abc221/tasks/abc221_d)


# keywords 
- array compression
- imos method
- cumsum 


# summary
- $\forall{i}\ B_i := B_i + A_i$
- apply array compression to $A, B$
- initialize an array $S$ for imos method.
- $\forall{i}\ S_{A_i} := S_{A_i} + 1, S_{B_i} := S_{B_i} - 1$
- $S := \text{cumsum}(S)$
- initialize result $C$
- $\forall{0 \le i \lt |S| - 1}$ 
  - let $l := \text{retrieve}(i), r := \text{retrieve}(i + 1)$
  - $C_{S_i} := C_{S_i} + r - l$
- $\forall{1 \le i \le N}$ 
  - print $C_i$

# code 
## sol_0
- numba (JIT)


# similar 
