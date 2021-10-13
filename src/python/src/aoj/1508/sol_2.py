# from __future__ import (
#   annotations,
# )
# import typing 
# from typing import (
#   Optional,
# )
# import sys 
# sys.setrecursionlimit(1 << 20)
# import dataclasses



# T = typing.TypeVar('T')
# V = typing.TypeVar('V')
# @dataclasses.dataclass 
# class Node(
#   typing.Generic[T, V],
# ):
#   size: int = 1
#   left: Optional[Node] = None
#   right: Optional[Node] = None
#   value: Optional[V] = None
#   mn: V = 1 << 50

  
#   def update(
#     self,
#   ) -> typing.NoReturn:
#     m = self.value
#     s = 1
#     if self.left:
#       m = min(m, self.left.mn)
#       s += self.left.size
#     if self.right:
#       m = min(m, self.right.mn)
#       s += self.right.size
#     self.mn = m



# T = typing.TypeVar('T')
# V = typing.TypeVar('V')
# @dataclasses.dataclass 
# class SplayArray(
#   typing.Generic[T, V]
# ):
#   root: typing.Optional[
#     Node[T, V]
#   ] = None

#   def rotate(
#     self,
#   ) -> typing.NoReturn:
#     u = self.root
#     if self.__state() < 0:
#       v = u.left
#       u.left = v.right
#       v.right = u  
#     else:
#       v = u.right 
#       u.right = v.left
#       v.left = u 
#     self.root = v
#     u.update()
#     v.update()


#   def splay(
#     self,
#     i: T,
#   ) -> typing.NoReturn:
#     self.__i = i
#     us = self.__state()
#     if not us: return
#     u = self.root
#     j = (
#       u.left.size if u.left
#       else 0
#     )
#     k = i
#     if us < 0:
#       v = u.left
#     else:
#       v = u.right
#       k -= j + 1
#     self.__i = k
#     self.root = v
#     vs = self.__state()
#     if not vs:
#       self.root = u
#       self.__i = i
#       self.rotate()
#       return
#     j = (
#       v.left.size if v.left
#       else 0
#     )
#     l = k
#     if vs < 0:
#       self.root = v.left
#     else:
#       self.root = v.right
#       l -= j + 1
#     self.splay(l)
#     if vs < 0:
#       v.left = self.root
#     else:
#       v.right = self.root
#     if us == vs:
#       self.root = u
#       self.__i = i
#       self.rotate()
#     else:
#       self.root = v
#       self.__i = k   
#       self.rotate()
#       if us < 0:
#         u.left = self.root
#       else:
#         u.right = self.root
#       self.root = u

#     self.rotate()


#   def __state(
#     self,
#   ) -> int:
#     u = self.root
#     if not u: return 0
#     j = (
#       u.left.size if u.left
#       else 0
#     )
#     i = self.__i
#     if i == j: return 0
#     if i < j:
#       return (
#         -1 + 1 * (not u.left)
#       )
#     return (
#       1 - 1 * (not u.right)
#     )


#   def __getitem__(
#     self,
#     key: T,
#   ) -> V:
#     self.splay(key)
#     return self.root.value


#   def __setitem__(
#     self,
#     key: T,
#     v: V,
#   ) -> typing.NoReturn:
#     self.splay(key)
#     self.root.value = v
#     self.root.upate()
  


#   def max_key(
#     self,
#   ) -> T:
#     u = self.root
#     while u.right:
#       u = u.right
#     return u.key


#   def join(
#     self,
#     rhs: SplayArray[T, V],
#   ) -> typing.NoReturn:
#     u = self.root
#     v = rhs.root
#     if not u:
#       self.root = v
#       return 
#     if not v: return
#     self.splay(self.max_key())
#     u.right = v
#     v.parent = u
#     u.update()
#     self.root = u
  


# def main() -> typing.NoReturn:
#   n = 1 << 18
#   a = [
#     Node(key=i)
#     for i in range(n)
#   ]
#   for i in range(n - 1):
#     a[i].right = a[i + 1]
  
#   st = SplayArray(a[0])
  
#   n = int(input())
#   i = 0
#   for _ in range(n):
#     *q, = map(
#       int, input().split(),
#     )
#     if q[0] == 0:
#       st[i] = q[1]
#       i += 1
#       continue
#     if q[0] == 1:
#       print(st[q[1]])
#       continue
#     i -= 1


# main()