

def test():
  n: int = 10 
  for i in range(n):
    print(i)
  
  import numpy as np
  a = np.arange(1 << 26)
  print(a)



if __name__ == '__main__':
  test()

