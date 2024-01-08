import sys
sys.stdin = open("input.txt")

N, K  = map(int, input().split())

# N = > += 1 -= 1 순간이동 하면 2X

def HS(N, K):
    if N == K:
        print(N)
        True
        
    else:
        if N < 2*K: 
            N += 1
        elif N > 2*K:
            N -= 1
        elif N >= 2*K:
            N = N * 2
        print(N)


HS(N, K)