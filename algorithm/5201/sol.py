import sys
sys.stdin = open("input.txt")


T = int(input())
for _ in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arrw = list(map(int, input().split()))
    k = [0 for _ in range(M)]
    result = 0

    arr = sorted(arr)
    arrw = sorted(arrw)
    arr = arr[::-1]
    arrw = arrw[::-1]
    for i in range(N):
        for j in r





