import typing 
import math



def compute(sx: int, dx: float, a: int, r: int) -> float:
    reverse = False 
    if dx < 0:
        sx = a - sx
        reverse = True
        dx *= -1
    t = int(math.floor((sx - r + dx) / (a - 2 * r)))
    gx = (sx + dx + 2 * r * t) % a
    if t & 1 ^ reverse: 
        gx = a - gx
    return gx 


def solve(
    a: int, 
    b: int, 
    x: int, 
    y: int, 
    r: int, 
    theta: int, 
    l: int,
) -> typing.NoReturn:
    rad = math.tau * theta / 360
    dx = math.cos(rad) * l
    dy = math.sin(rad) * l
    gx = compute(x, dx, a, r)
    gy = compute(y, dy, b, r)
    print(gx, gy)


def main() -> typing.NoReturn:
    a, b, x, y, r, theta, l = map(int, input().split())
    solve(a, b, x, y, r, theta, l)


main()