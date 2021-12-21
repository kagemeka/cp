import typing 


def base_convert_from_ten(
    base: int, 
    n: int,
) -> typing.List[int]:
    assert abs(base) >= 2
    if n == 0: return [0]
    digits = []
    while n:
        n, r = divmod(n, base)
        if r < 0:
            r -= base
            n += 1
        digits.append(r)
    return digits


def lucas_theorem(p: int, n: int, k: int) -> int:
    r"""Lucas's Theorem.
    references
        - https://en.wikipedia.org/wiki/Lucas%27s_theorem
    """
    if k < 0 or n < k: return 0
    a = base_convert_from_ten(p, n)
    b = base_convert_from_ten(p, k)
    ...
    
    
    
def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input()))
    # odd, even
    a = [x - 1 for x in a]
    def is_odd(a: typing.List[int]) -> bool:
        n = len(a)
        ... 

main()