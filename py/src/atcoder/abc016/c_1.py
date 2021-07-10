# res = [
#   bit_count(
#     cumor(f[j] 
#     for j in range(n) 
#     if f[i] >> j & 1
#   ) & ~(f[i] | 1 << i)) for i in range(n)
# ]
# print(*res, sep='\n')