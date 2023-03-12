import sys
sys.stdin = open("input.txt")

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]


N, M = map(int, input().split())
arr = [[0 for _ in range(N)] for _ in range(M)]
cnt = 0
result = ''
K = int(input())
for i in range(N):
    for j in range(M):
        arr[M-1][0] = 1
        i, j = M - 1, 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 0:
                while cnt < K:
                    if arr[nx][0] == 0:
                        arr[nx][0] = cnt
                        cnt += 1
                    elif arr[0][ny] == 0:
                        arr[0][ny] = cnt
                        cnt += 1
                if N * M < K:
                    result = '0'
print(*result)
for k in arr:
    print(k)


