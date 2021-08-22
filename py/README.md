# CP with Python 


# [My Package](https://github.com/kagemeka/py)


# AOT Compilation
- [sample submission(ARC116C)](https://atcoder.jp/contests/arc116/submissions/24436702)


# run
- enable clipboard by `xhost +`
- run by the command like below.
```sh
$ xsel | python3 <problem>.py
```



# tips


## pypy
- not good at DFS
- not good at string


## numba
- not good at DFS 
- cannot define DFS as closure 
- unsupported numpy functions
  - np.cumsum(a, out=a)
  - np.ufunc
    - np.maximum()
    - np.minimum()
    - axis
  - np.pad()


- supported numpy feature
  - np.argsort()
  - np.cumsum(a)
  - np.eye()
  - np.flatnonzero()
  - np.full()
  - np.int64
  - np.ones()
  - np.searchsorted()
  - np.unique(a)
  - np.where()
  - np.zeros()
  - ndarray.all()
  - ndarray.any()
  - ndarray.argmin()
  - ndarray.cumsum()
  - ndarray.max()
  - ndarray.min()
  - ndarray.reshape()
  - ndarray.shape


- supported standard feature 
  - min
  - max


- unsupported standart feature
  - dict
  - set
  - itertools module
  - math module 
  - functools module
  - collections module


- strict dtype
