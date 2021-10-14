# [D. Diane](https://codeforces.com/contest/1554/problem/D)



# summary
- consider use 'a' as many as possible
- 'a' * k + ('b' | 'bc') + 'a' * (k - 1) satisfy the answer condition.
  - in 'a' * k substring, 'a' occurs odd number of times if k is odd, or occurs even number of times if k is even.
  - and 'aa' occurs even, 'aaa' occurs odd, ... 'a' * (k - 1) occurs even , 'a' * k occurs odd in 'a' * k string if k is odd.
  - OTOH, 'a' occurs even, 'aa' occurs 'odd', ... 'a' * (k - 1) occurs odd in 'a' * (k - 1) string if k is odd.
  - for each length of 'a...', odd + even = odd.
  - so we can fix k = floor(n / 2)
  - if n is even, join two 'a...' string with 'b'
  - if n is odd, join two 'a...' string with 'bc'
- O(N)


# keywords 
- string 
- greedy





# tips 
- how to check whether the arbitral answer satisfy the condition?
- keywords: `suffix automaton` data structure see [wiki](https://en.wikipedia.org/wiki/Suffix_automaton)
- odd + even = odd 
- even + even = even
- odd + odd = even