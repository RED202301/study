import sys
sys.stdin = open("input.txt")

T = int(input())

for i in range(1, T+1):
    N, M = input().split()
    M = int(M)
    M_ = 0
    ar = list(N)

    arr = sorted(N)
    arr = arr[::-1]
    if len(ar) < M:
        M_ = M - len(ar)
    # print(ar)
    print(M_)
    if M_ != 0:
        k = 0
        for j in range(len(ar)):
            if arr[k] == N[j]:
                while k != M//2:
                    ar[k], ar[j] = ar[j], ar[k]
                    k += 1
#
    #
    print(ar)


