import typing 
import sys
sys.setrecursionlimit(1 << 20)


def main() -> typing.NoReturn:
    # compute Ex in case that any paths are not blocked.
    # for each edge e, 
    # Ex = probability(pass through e) * Ex(in case pass through e) + probability(not pass through e) * Ex(in case not pass through e)
    # preprocess the probability passing through each node. 
    n, m = map(int, input().split())

    g = [[] for _ in range(n)]
    rev_g = [[] for _ in range(n)]
    in_deg = [0] * n
    out_deg = [0] * n
    
    st = []
    for _ in range(m):
        s, t = map(int, input().split())
        s -= 1
        t -= 1
        st.append((s, t))
        g[s].append(t)
        in_deg[t] += 1
        rev_g[t].append(s)
        out_deg[s] += 1
    
    prob = [[0] * n for _ in range(n)]
    for i in range(n):
        k = len(g[i])
        for j in g[i]:
            prob[i][j] = 1 / k
    
    inf = 1 << 60
    count = [inf] * n
    count[-1] = 0
    def dfs(u: int) -> typing.NoReturn:
        if count[u] != inf: return count[u]
        ex = 0
        for v in g[u]:
            ex += prob[u][v] * (dfs(v) + 1)
        count[u] = ex
        return ex
    for i in range(n): dfs(i)
    
    count_rev = [inf] * n
    count_rev[0] = 0
    def rev_dfs(u: int) -> typing.NoReturn:
        if count_rev[u] != inf: return count_rev[u]
        ex = 0
        for v in rev_g[u]:
            ex += prob[u][v] * (rev_dfs(v) + 1)
        count_rev[u] = ex
        return ex
    for i in range(n - 1, -1, -1): rev_dfs(i)


    prob_node = [0] * n
    prob_node[0] = 1
    que = [i for i in range(n) if in_deg[i] == 0]
    for u in que:
        for v in g[u]:
            prob_node[v] += prob_node[u] * prob[u][v]
            in_deg[v] -= 1
            if in_deg[v] == 0: que.append(v)
    
    
    mn = count[0]
    for i, j in st:
        print(prob[i][j])
        if prob[i][j] == 0: continue
        p = prob_node[i] * prob[i][j] # pass through edge (i, j)
        if p == 1: continue
        # print(p)
        ex = (count[0] - (count[j] + 1 + count_rev[i]) * p) / (1 - p)
        mn = min(mn, ex)
    print(mn)

            
        
            

main()
    
    
    
    
    
    
