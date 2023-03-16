# import sys
# sys.stdin = open("input.txt")
#
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# def snail(i, j, N):
#     arr[i][j] = 1
#     idx = 0
#     cnt = 2
#     while cnt <= N**2:
#         nx = i + dx[idx]
#         ny = j + dy[idx]
#         if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
#             arr[nx][ny] = cnt
#             i, j = nx, ny
#             cnt += 1
#         elif idx == 3:
#             idx = 0
#         else:
#             idx += 1
#
#
#
#
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     # print(N)
#     arr = [[0 for _ in range(N)] for _ in range(N)]
#     snail(0, 0, N)
#     print(f'#{tc}')
#     for i in range(N):
#         for j in range(N):
#             print(arr[i][j], end = ' ')
#         print()
# import sys
# sys.stdin = open("input.txt")
#
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# def butter(N, M, x, y):
#     global tcnt
#     x, y = 0, 0
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0 <= nx < N and 0 <= ny < M:
#             x, y = nx, ny
#             if arr[nx][ny] == 1:
#                 pass
#             elif arr[nx][ny] == 0:
#                 continue
#             tcnt += 1
#                 # k = 0
#     return tcnt
#
# T = int(input())
# for _ in range(1, T + 1):
#     N, M, K = map(int, input().split())
#     arr = list([[0 for _ in range(M)] for _ in range(N)])
#     tcnt = 0
#     for _ in range(K):
#         x, y = map(int, input().split())
#         arr[x][y] = 1
#     print(butter(N, M, x, y))

import sys
sys.stdin = open("input.txt")

dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, 1, -1, -1, 1]
def galaxy(i, j):
    global tcnt
    cnt = 0

    for k in range(8):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if arr[i][j] > arr[nx][ny]:
                cnt += 1
    if cnt >= 4:
        tcnt += 1
    return tcnt


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tcnt = 0
    for i in range(N):
        for j in range(M):
            galaxy(i, j)
    print(f'{tc} {tcnt}')