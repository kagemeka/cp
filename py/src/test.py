

import dataclasses
import typing



class A():
  def __init__(
    self,
  ):
    self.v = 0



def test():
  a = A()
  b = [A()] * 10 
  print(b[0].v)
  b[1].v += 1
  print(b[0].v)



if __name__ == '__main__':
  test()