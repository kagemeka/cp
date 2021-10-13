class Solution:
  def canBeTypedWords(
    self, 
    text: str, 
    brokenLetters: str,
  ) -> int:
    self.__b = set(
      brokenLetters,
    )
    return sum(
      self.__check_word(w)
      for w in text.split()
    )


  def __check_word(
    self,
    w: str,
  ) -> bool:
    b = self.__b
    for c in w:
      if c in b: return False
    return True
    
        