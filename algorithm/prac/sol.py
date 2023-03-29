import sys
sys.stdin = open("input.txt")

# print(visited)

# def dfs():
#     if len(arr) == N:
#         print(*arr)
#         return
#     for i in range(1, M + 1):
#         if visited[i]:
#             continue
#         else:
#             if i not in arr:
#                 visited[i] = True
#                 arr.append(i)
#                 dfs()
#                 arr.pop()
#                 visited[i] = False
#
#
#
# dfs()

















#
def dfs():
    if len(arr) == N:
        print(*arr)
        return
    for i in range(1, N + 1):
        if i not in arr:
            arr.append(i)
            dfs()
            arr.pop()

N = int(input())
arr = []
dfs()






# for i in range(1, N+1):
#     for j in range(1, N+1):
#         for k in range(1, N+1):
#             if i != j and i != k and j != k and i != j != k:
#                 print(i, j, k)