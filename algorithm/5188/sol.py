import sys
sys.stdin = open("input.txt")


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


