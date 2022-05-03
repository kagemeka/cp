import math

def main() -> None:

    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    xy.sort()
    def area_is_integer(i: int, j: int, k: int) -> bool:
        xi, yi = xy[i]
        xj, yj = xy[j]
        xk, yk = xy[k]
        if xi == xk:
            return False
        if (yj - yi) * (xk - xj) == (yk - yj) * (xj - xi):
            return False
        
    
        
        


if __name__ == "__main__":
    main()
