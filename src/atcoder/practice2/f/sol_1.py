import typing 

ROOT = 3
MOD = 998244353
roots  = [pow(ROOT,(MOD-1)>>i,MOD) for i in range(24)] # 1 の 2^i 乗根
iroots = [pow(x,MOD-2,MOD) for x in roots] # 1 の 2^i 乗根の逆元
 

print(roots)
print(iroots)
print(roots[1] * roots[1] % MOD)



class NTT():
  def __call__(
    self,
    a: typing.List[int],
  ) -> typing.NoReturn:
    ...

  

  def __init__(
    self,
    prime: int=998_244_353,
    primitive_root: int=3,
    max_size: int=1 << 23,
  ) -> typing.NoReturn:
    self.__p = prime 
    self.__g = primitive_root
    self.__m = max_size
    self.__preprocess()
  

  def __preprocess(
    self,
  ) -> typing.NoReturn:
    p, g = self.__p, self.__g
    n = self.__m.bit_length() 
    roots = [pow(g, (p - 1) >> i, p) for i in range(n)]
    iroots = [pow(x, p - 2, p) for x in roots]
    self.__roots = roots
    self.__iroots = iroots
    print(roots)
    print(iroots)
      
  

  def inv(
    self,
  ) -> typing.NoReturn:
    ... 



ntt = NTT()