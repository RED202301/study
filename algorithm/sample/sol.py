# # import sys
# # sys.stdin = open("input.txt")
# #
# # T = 10
# # for tc in range(1, T +1):
# #     N = int(input())
# #     numbers = list(map(int, input().split()))
# #     for i in range(N):
# #         max_num = max(numbers)
# #         min_num = min(numbers)
# #         index_max_num = numbers.index(max_num)
# #         index_min_num = numbers.index(min_num)
# #         numbers[index_max_num] -= 1
# #         numbers[index_min_num] += 1
# #     print('#{} {}'.format(tc, max(numbers)-min(numbers)))
#
# # N = int(input())
# # count = 0
# # while True:
# #     if N % 5 == 0:
# #         count += (N//5)
# #         print(count)
# #         break
# #     N -= 3
# #     count += 1
# # else:
# #     print(-1)
#
# import sys
# sys.stdin = open('input.txt','r',encoding='utf=8')
#
# def binary_search(start, end, target):
#     start = start
#     end = end
#     count = 1
#     while True:
#         middle = (start + end) // 2
#         if middle == target:
#             return count
#         elif middle > target:
#             end = middle
#         else:
#             start = middle
#         count += 1
#
#     if target == end:
#         return count + 1
#     if target == start:
#         return count
#
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     P, A, B = map(int, input().split())
#     a = binary_search(1, P, A)
#     b = binary_search(1, P, B)
#     if a == b:
#         print(f'#{tc} 0')
#     elif a < b:
#         print(f'#{tc} A')
#     else:
#         print(f'#{tc} B')
#
#
#
#
#
#
#
# # T = int(input())
# # for tc in range(1, T + 1):
# #     N = int(input())
# #     arr = [[0 for _ in range(10)] for _ in range(10)]
# #
# #     result = 0
# #     for _ in range(N):
# #         r1, c1, r2, c2, c = map(int, input().split())
# #         for x in range(r1, r2+1):
# #             for y in range(c1, c2+1):
# #                 arr[x][y] += c
# #                 if arr[x][y] == 3:
# #                     result += 1
# #
#
#     # for i in range(10):
#     #         # print(arr[i])
#     # print(f'#{tc} {result}')
#
#
#
#
#
#
#
#
#

# import sys
# sys.stdin = open("input.txt")
#
# dx = [0, 0, -1, 1, -1, -1, 1, 1]
# dy = [-1, 1, 0, 0, -1, 1, 1, -1]
# def galaxy(x, y):
#     global tcnt
#     cnt = 0
#
#     for k in range(8):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0 <= nx < i and 0 <= ny < j:
#             if arr[x][y] > arr[nx][ny]:
#                 cnt += 1
#
#     if cnt >= 4:
#         tcnt += 1
#     return tcnt
#
# #
# T = int(input())
# for tc in range(1, T + 1):
#     i, j = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(i)]
#     tcnt = 0
#     for x in range(i):
#         for y in range(j):
#             galaxy(x, y)
#     print(f'#{tc} {tcnt}')


# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     max_ = 0
#     for i in range(N-M+1):
#         for j in range(N-M+1):
#             result = 0
#             for k in range(i, i+M):
#                 for l in range(j, j+M):
#                     result += arr[k][l]
#             if result > max_:
#                 max_ = result
#
#     print(f'#{tc} {max_}')

# import sys
# sys.stdin = open("input.txt")
#
# # def cal(n, m):
# #     i = 0
# #     while m - i != 0:
# #         if m - i == 1:
# #             return n
# #         i += 1
# #         return n * cal(n, m - i)
# #
# #
# # for tc in range(1, 11):
# #     N = int(input())
# #     n, m = map(int, input().split())
# #     print(f'#{tc}', cal(n, m))
#
# for tc in range(1, 11):
#     N = int(input())
#     arr = input()
#     stack = []
#     stack_ = []
#     result = 0
#     for i in range(N):
#         stack.append(arr[i])
#         if stack in '+-*/()':
#             stack_ += stack.pop()
#         else:
#             x = int(stack.pop())
#             y = int(stack.pop())
#         # print(stack)
#         if stack == '+':
#             result += y + x
#         elif stack == '-':
#             result += y - x
#         elif stack == '*':
#             result += y * x
#         elif stack == '/':
#             result += y // x
#     print(result)

# import sys
# sys.stdin = open("input.txt")
#
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# def balloon(x, y):
#     global max_
#     result = int(arr[x][y])
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0 <= nx < N and 0 <= ny < M:
#             result += int(arr[nx][ny])
#             if result > max_:
#                 max_ = result
#     return max_
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = [input().split() for _ in range(N)]
#     max_ = 0
#     for x in range(N):
#         for y in range(M):
#             balloon(x, y)
#     print(f'#{tc} {max_}')
# #
# import sys
# sys.stdin = open("input.txt")
# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]
# # T = int(input())
# # for tc in range(1, T + 1):
# def an(x, y):
#     global max_
#     cnt = 0
#     x, y = 0, 0
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#     if 0 <= nx < N and 0 <= ny < M:
#         if arr[nx][ny] == 1:
#             cnt += 1
#         if max_ < cnt:
#             max_ = cnt
#     return max_








# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [input().split() for _ in range(N)]
#     max_ = 0
#     for i in range(N):
#         for j in range(M):
#             an(i, j)
#     print(f'{tc}', max_)
#
# import sys
# sys.stdin = open("input.txt")

# def dfs(S, G):
#     stack.append(S)
#     visited[S] = 1
#     while stack:
#         if S == G:
#             return 1
#         else:
#             for i in node[S]:
#                 if not visited[i]:
#                     stack.append(i)
#                     visited[i] = 1
#             S = stack.pop()
#     return 0
#
# T = int(input())
# for tc in range(1, T + 1):
#     V, E = map(int, input().split())
#     node = [[] for _ in range(V+1)]
#     visited = [0] * (V + 1)
#     stack = []
#     for _ in range(E):
#         u, v = map(int, input().split())
#         node[u].append(v)
#     S, G = map(int, input().split())
#     print(f'#{tc} {dfs(S, G)}')

# N, M = map(int, input().split())
# arr = [input().]

# import sys
# sys.stdin = open("input.txt")
#
# N, M, R = map(int, input().split())
# u = [0 for _ in range(N) for _ in range(N)]
# for i in range(M+1):
#     n, m = map(int, input().split())
#     u[n] = m
#     print(n, m)





# dx = [0, 1]
# dy = [1, 0]
# def ant(i, j):
#     for k in range(2):
#         nx = i + dx[k]
#         ny = j + dy[k]
#         if 0 <= nx < 10 and 0 <= ny < 10:
#             if arr[nx][ny] == 2:
#                 arr[nx][ny] = 9
#                 return
#             elif arr[nx][ny] == 0:
#                 if arr[i+dx[0]][j+dy[0]] == 0:
#                     arr[i+dx[0]][j+dy[0]] = 9
#
#                 else:
#                     arr[i+dx[1]][j+dy[1]] = 9
#                 ant(nx, ny)
#                 break
#         return arr
#
#
#
#
#
#
# arr = [list(map(int, input().split())) for _ in range(10)]
#
# for i in range(10):
#     for j in range(10):
#         i, j = 1, 1
#         arr[i][j] = 9
#         ant(i, j)
# for i in arr:
#     print(i)







#
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# def maze(i, j, depth):
#     global cnt
#     for k in range(4):
#         nx = i + dx
#         ny = j + dy
#         if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 1:
#             if arr[nx][ny] == 3:
#                 cnt = depth
#             elif arr[nx][ny] == 0:
#                 arr[nx][ny] = 1
#                 maze(nx, ny, depth + 1)
#         return 0
#
#
#
#
# # T = int(input())
# # for tc in range(1, T + 1):
# #     N = int(input())
# arr = [input() for _ in range(10)]
# cnt = 0
# for i in range(10):
#     for j in range(10):
#         if arr[i][j] == 2:
#             maze(i, j, 0)
#
#
# print(f'{cnt}')
#

# import sys
# sys.stdin = open("input.txt")

# N,K = map(int, input().split())
# s0 = [0 for _ in range(7)]
# s1 = [0 for _ in range(7)]
# for _ in range(N):
#     S, C = map(int, input().split())
#     if S == 0:
#         s0[C] += 1
#     if S == 1:
#         s1[C] += 1
# cnt = 0
# for u in range(7):
#     if s0[u] == 0:
#         cnt += 0
#     elif s0[u] >= 1:
#         if s0[u] % K == 0:
#             cnt += (s0[u] // K)
#         elif s0[u] % K == 1:
#             cnt += (s0[u] // K) + 1
# cnt_ = 0
# for u in range(7):
#     if s1[u] == 0:
#         cnt_ += 0
#     elif s1[u] >= 1:
#         if s1[u] % K == 0:
#             cnt_ += (s1[u] // K)
#         elif s1[u] % K == 1:
#             cnt_ += (s1[u] // K) + 1
# print(cnt + cnt_)


# 두개의 숫자열
# import sys
# sys.stdin = open("input.txt")

# T = int(input())
# for tc in range(1, T + 1):
#     n, m = map(int, input().split())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#
#     # result = 0
#     # if M < N:
#     #     for i in range(M-N+1):
#     #         tmp = 0
#     #         for j in range(N):
#     #             tmp += a[i + j] * b[j]
#     #         if result < tmp:
#     #             result = tmp
#     # print(result)
#     result = 0
#
#     if n < m:
#         n, m = m, n
#         a, b = b, a
#
#     if n > m:
#         for i in range(n-m+1):
#             tmp = 0
#             for j in range(m):
#                 tmp += a[i + j] * b[j]
#         # print(tmp)
#             if result < tmp:
#                 result = tmp
#     print(result)

import sys
sys.stdin = open("input.txt")
arr = []

for _ in range(9):
    N = int(input())
    arr.append(N)
    arr = sorted(arr)
# print(arr
for i in range(len(arr)):
    sum = arr[i]
    for j in range(i, len(arr)-i-1):
        sum += arr[j]
    print(sum)
                    #     print('A')
                    # elif ark[0] < ark_[0]:
                    #     print('B')
                    # else:
                    #     print('D')


        # if ark[4] > ark_[4]:
        #     print('A')
        # elif ark[4] < ark_[4]:
        #     print('B')
        # else:
        #     if ark[3] > ark_[3]
        #
        # # if ark[]


