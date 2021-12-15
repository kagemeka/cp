import typing 
import itertools 

def main() -> typing.NoReturn:
    n, m, q = map(int, input().split())
    abcd = [tuple(map(int, input().split())) for _ in range(q)]
    
    mx = 0
    
    def repeated_combinations(n: int, r: int, j: int=0) -> typing.Iterator[typing.Tuple[int]]:
        assert n >= 0 and r >= 0
        if n == 0 or r == 0:
            yield tuple()
            return
        for i in range(j, n):
            for arr in repeated_combinations(n, r - 1, i):
                yield (i, ) + arr
        
        
    # for arr in itertools.product(range(1, m + 1), repeat=n):
    for arr in repeated_combinations(m, n):
        print(arr)
        arr = [x + 1 for x in arr]
        s = 0 
        for a, b, c, d in abcd:
            a -= 1
            b -= 1
            s += d * (arr[a] - arr[b] == c)
        mx = max(mx, s)
    print(mx)

main()
            
    
    