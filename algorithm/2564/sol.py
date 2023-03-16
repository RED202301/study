import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
T = int(input())
arr = [[0 for _ in range(N)] for _ in range(M)]
for _ in range(T):
    x, y = map(int, input().split())

    arr[x][y] = 2

x1, y1 = map(int, input().split())

arr[x1][y1] = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            a, b = i, j
        if arr[i][j]