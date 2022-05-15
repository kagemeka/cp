def main() -> None:
    n, m = map(int, input().split())

    edges = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
    

    # T1

    g = [[] for _ in range(n)]
    for i in range(m):
        u, v = edges[i]
        g[u].append((v, i, 0)) # if not added, u must be ancestor of v
        g[v].append((u, i, 1))

    
    on_stack = [False] * n
    stack = [0]
    on_stack[0] = True
    added = [False] * m
    # visited = [False] * n
    added_to_stack = [False] * m
    added_to_stack[0] = True
    while stack:
        u = stack.pop()
        if u < 0:
            on_stack[~u] = False
            continue
        # if visited[u]:
        #     continue
        # visited[u] = True
        stack.append(~u)
        for v, i, j in g[u]:
            if not added_to_stack[v] and j == 1:
                stack.append(v)
                on_stack[v] = True
                added_to_stack[v] = True
                added[i] = True

    print(added_to_stack)
    rev_g = [[] for _ in range(n)]
    for i in range(m):
        u, v = edges[i]
        rev_g[v].append((u, i))
    que = [u for u in range(n) if added_to_stack[u]]
    for u in que:
        for v, i in rev_g[u]:
            if added_to_stack[v]:
                continue
            added[i] = True
            added_to_stack[v] = True
            que.append(v)
    print(added_to_stack)
    print(added)

        
    



    # T2


if __name__ == "__main__":
    main()
