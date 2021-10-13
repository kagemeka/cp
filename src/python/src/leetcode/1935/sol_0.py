class Solve():
  def __call__(
    self,
    text: str,
    broken_letters: str,
  ) -> int:
    s = text.split()
    b = set(broken_letters)
    cnt = 0
    for w in s:
      w = set(w)
      cnt += w == w - b
    return cnt


class Solution:
  def canBeTypedWords(
    self, 
    text: str, 
    brokenLetters: str,
  ) -> int:
    s = Solve()
    return s(
      text,
      brokenLetters,
    )
        