import typing


def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    
    # def compute_average() -> float:
    #     dp = [(0, 0), (0, 0)] # no_choose, choose
    #     for i in range(n):
    #         ndp = [None, None]
    #         s, c = dp[1]
    #         ndp[0] = (s, c)
    #         ndp[1] = (s + a[i], c + 1)
    #         s, c = dp[0]
    #         if c >= 1:
    #             if (s + a[i]) / (c + 1) > ndp[1][0] / ndp[1][1]:
    #                 ndp[1] = (s + a[i], c + 1)
    #             # if ndp[0][1] == 0 or s / c > ndp[0][0] / ndp[0][1]:
    #             #     ndp[0] = (s, c)
    #         dp = ndp
    #         print(dp)
    #     print(dp)
    
    
    # dp_average()
    # average
    def is_possible(avg: float) -> bool:
        s = 0
        cnt = 0
        is_added = [False] * n
        for i in range(n):
            if a[i] >= avg:
                s += a[i]
                cnt += 1
                is_added[i] = True
                
        for i in range(n):
            x = a[i]
            if x >= avg: continue
            if i > 0:
                
    def binary_search() -> float:
        lo, hi = 0, 1 << 30 # possible, impossible 
        for _ in range(100):
            avg = (lo + hi) / 2
            if is_possible(avg):
                lo = avg
            else:
                hi = avg
            
            
            


if __name__ == "__main__":
    main()
