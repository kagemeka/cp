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
- using recursive function and enabling cache with numba might occurs segmentation fault.
- recursive function also too slow.
- strict dtype



### unsupported numpy functions
- np.cumsum(a, out=a)
- np.ufunc
  - np.maximum()
  - np.minimum()
  - axis
- np.pad()
- np.resize()
- ndarray.resize()
- ndarray.tolist()


### supported numpy feature
- np.arctan2()
- np.argmax()
- np.argmin()
- np.argsort()
- np.bincount()
- np.cos()
- np.cumsum(a)
- np.deg2rad()
- np.eye()
- np.flatnonzero()
- np.full()
- np.int64
- np.mean()
- np.ones()
- np.pi
- np.prod()
- np.rad2deg()
- np.real()
- np.rint()
- np.searchsorted()
- np.sin()
- np.sum()
- np.unique(a)
- np.where()
- np.zeros()
- ndarray.all()
- ndarray.any()
- ndarray.argmin()
- ndarray.astype()
- ndarray.cumsum()
- ndarray.max()
- ndarray.min()
- ndarray.reshape()
- ndarray.shape
- ndarray.sum()



### supported standard feature 
- min
- max


### unsupported standart feature
- dict
- set
- itertools module
- math module 
- functools module
- collections module


