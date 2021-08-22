import typing 




def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  *s, = map(int, input().split())
  *t, = map(int, input().split())

  l = None
  for i in range(-1, 0, -1):
    if s[i] != s[0]  

  # l_zero = [None] * n
  # l_one = [None] * n 
  # r_zero = [None] * n
  # r_one = [None] * n
  # for i in range(0, -n, -1):
  #   if s[i] == 0:
  #     l_zero[0] = i
  #     break
  # for i in range(0, -n, -1):
  #   if s[i] == 1:
  #     l_one[0] = i
  #     break
  
  # for i in range(n):
  #   if s[i] == 0:
  #     r_zero = i
  #     break 
  
  # for i in range(n):
  #   if s[i] == 1:
  #     r_one = i
  #     break 
  
  # for i in range(1, n):
  #   if s[i] == 0:
  #     l_zero[i] = i
  #     l_one[i] = l_one[i - 1]
  #   else:
  #     l_zero[i] = l_zero[i - 1]
  #     l_one[i] = i

  
  # for i in range(n - 2, -1, -1):
  #   if s[i] == 0:
  #     r_zero[i] = i
  #     r_one[i] = r_one[i + 1]
  #   else:
  #     r_zero[i] = l_zero[i + 1]
  #     r_one[i] = i

  
  # res = m
  
  



main() 