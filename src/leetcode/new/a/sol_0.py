import typing 

class Solution:
  def reversePrefix(
    self, 
    s: str, 
    ch: str,
  ) -> str:
    i = s.find(ch)
    s = list(s)
    if i != -1:
      s[:i + 1] = s[i::-1]
    
    return ''.join(s)
      
    
        