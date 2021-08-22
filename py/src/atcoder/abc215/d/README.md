# [D - Coprime 2](https://atcoder.jp/contests/abc215/tasks/abc215_d)




# keywords 
- prime factorization
- harmonic series
- hash set



# summary
- at first, prime factorize $A_i\ \forall{i}$ and find all prime factors in $A$
  - $O(N\log{\max{A}})$ by preprocessing LPF(Least Prime Factor) or GPF(Greatest Prime Factor)
  - $O(N\sqrt{\max{A}})$ by preprocessing prime numbers or calculating naively.
- second, remove $x \in {1..m}$ if $\exists{p} | x$, where $p \in$ prime factors in $A$
  - $O(M\sqrt{M})$ by using hash set and prime factorize $x\ \forall{x}$
  - $O(M\log{\log{M}})$ by removing x like Sieve of Eratosthenes.



## sol_0 
- $O(N\sqrt{\max{A}} + M\sqrt{M}$



## sol_1
- naive prime factorize
- $O(N\sqrt{\max{A}} + M\log{\log{M}})$



## sol_2
- naive prime factorize
- $O(N\sqrt{\max{A}} + M\log{\log{M}})$
- numba (JIT)


## sol_3
- prime factorize with prime numbers with sieve of eratosthenes.
- $O(\max{A}\log{\log{\max{A}}} + N\sqrt{\max{A}} + M\log{\log{M}})$



## sol_4
- prime factorize with prime numbers with sieve of eratosthenes.
- $O(\max{A}\log{\log{\max{A}}} + N\sqrt{\max{A}} + M\log{\log{M}})$
- numba (JIT)



## sol_5
- prime factorize with lpf with sieve of eratosthenes.
- $O(\max{A}\log{\log{\max{A}}} + N\log{\max{A}} + M\log{\log{M}})$


## sol_6
- prime factorize with lpf with sieve of eratosthenes.
- $O(\max{A}\log{\log{\max{A}}} + N\log{\max{A}} + M\log{\log{M}})$
- numba (JIT)



## sol_7
- $O(N + (\max{A} + M)\log{M})$



## sol_8
- $O(N + (\max{A} + M)\log{M})$
- numba (JIT)