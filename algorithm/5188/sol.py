import sys
sys.stdin = open("input.txt")


dx = [0, -1]
dy = [1, 0]
def lowsum(i, j):
    global result
    for k in range(2):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            i, j = nx, ny
            if nx != N-1 and ny != N-1:
                result += arr[nx][ny]
            else:
                return result








T = int(input())
for tc in range(1, T+1):
    result = 0
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                lowsum(i, j)

    print(result)