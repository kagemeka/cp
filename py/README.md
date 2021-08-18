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
  - np.cumsum(a)
  - np.unique(a)
  - np.zeros()
  - np.full()
  - np.eye()
  - np.int64
  - ndarray.shape
  - ndarray.reshape()
  - ndarray.cumsum()
  - np.ones()
  - np.flatnonzero()
  - ndarray.all()
  - ndarray.any()
  - ndarray.argmin()
  - ndarray.min()
  - ndarray.max()


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
