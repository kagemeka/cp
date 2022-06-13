# # mypy: ignore-errors


def debug(*objects: object, **kwargs: object) -> None:
    import os
    import pprint

    if os.environ.get("PYTHON_DEBUG") is None:
        return

    for obj in objects:
        pprint.pprint(obj)

    for key, obj in kwargs.items():
        print(f"{key}: ")
        pprint.pprint(obj)


def main() -> None:
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c, d = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append((b, c, d))
        g[b].append((a, c, d))

    # c is constant
    # arrive at node_i at time t,
    # then leave at t + dt
    # cost = c + dt + [d / (t + dt)]
    # find minimum of dt + [d / (t + dt)]
    # t + dt is approximately \sqrt(d)


if __name__ == "__main__":
    main()
