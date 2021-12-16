import typing 


def main() -> typing.NoReturn:
    k = int(input())
    x, y = map(int, input().split())
    if k % 2 == 0 and (abs(x) + abs(y)) & 1:
        print(-1)
        return 
    
    res = []
    x0, y0 = 0, 0
    rev_x = rev_y = False
    if x < 0:
        x = -x
        rev_x = True
    if y < 0:
        y = -y
        rev_y = True
    
    while x0 + k <= 