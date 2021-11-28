import typing 
import heapq



def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    connected_0 = [False] * n 
    connected = [False] * n
    # u = -1
    # mx = 0
    hq = []
    for i in range(n):
        heapq.heappush(hq, (-a[i], 0, i + 1))
        # if a[i] > mx:
        #     mx = a[i]
        #     u = i
    
    tot = 0
    while hq:
        d, u, v = heapq.heappop(hq)
        d *= -1
        if u == 0:
            v -= 1
            if connected_0[v]: continue
            nxt = (v + 1)
            pre = (v - 1) % n
            if connected_0[nxt] and connected[v] or connected_0[pre] and connected[pre]:
                continue
            connected_0[v] = True
            tot += a[v]
            heapq.heappush(hq, (-b[v], v, nxt)) 
            heapq.heappush(hq, (-b[pre], v, pre))
            # connected_0[]
        
    
    