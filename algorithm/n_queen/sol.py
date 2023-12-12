import sys
sys.stdin = open("input.txt")

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

def queen(x, y):
    global cnt
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            x, y = nx, ny
            arr[nx][ny] += 1
            if arr[nx][ny] > 1:
                ny += 1
                continue

            elif arr[nx][ny] == 1:
                nx += 1

            cnt += 1
    for o in arr:
        print(o)
    print()





N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]




cnt = 0

for i in range(N):
    for j in range(N):
        queen(i, j)
        print(cnt)