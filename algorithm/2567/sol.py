import sys
sys.stdin = open("input.txt")

N = int(input())
arr = [[0 for _ in range(1001)] for _ in range(101)]
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[x + i][y + j] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 0 and arr[i+1][j] == 1:
            cnt += 1
        if arr[i][j] == 0 and arr[i][j+1] == 1:
            cnt += 1
        if arr[i][j] == 1 and arr[i-1][j] == 0:
            cnt += 1
        if arr[i][j] == 1 and arr[i][j-1] == 0:
            cnt += 1
print(cnt)
