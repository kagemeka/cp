import typing 


def main() -> typing.NoReturn:
    h, w, n = map(int, input().split())
    
    x_list = [[] for _ in range(h)]
    y_list = [[] for _ in range(w)]
    for _ in range(n):
        r, c, a = map(int, input().split())
        r -= 1
        c -= 1
        x_list[r].append((c, a))
        y_list[c].append((r, a))
    
    in_deg = [0] * n
    g = [[] for _ in range(n)]
    for xs in x_list:
        xs.sort(key=lambda x: -x[1])