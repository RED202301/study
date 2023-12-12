import sys
sys.stdin = open("input.txt")


<<<<<<< HEAD
T = int(input())
for _ in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1, N):



























#
#
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     for i in range(1, N):
#         arr[0][i] += arr[0][i-1]
#         arr[i][0] += arr[i-1][0]
#     for y in range(1, N):
#         for x in range(1, N):
#             if arr[y-1][x] < arr[y][x-1]:
#                 arr[y][x] += arr[y-1][x]
#             else:
#                 arr[y][x] += arr[y][x-1]
#
#
#     print(f'#{tc} {arr[N-1][N-1]}')
#


=======
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
>>>>>>> a2b5278db16a1aed3ed4828b2ca1092861a53b15
