import sys
sys.stdin = open("input.txt")

N = int(input())
arr = list(input())
cnt = 0
scnt = N
for i in arr:
    if i == 'S':
        cnt += 1
    if i == 'L':
        cnt += 0.5

if cnt < N:
    cnt += 1

print(int(cnt))


# if arr[-1] == 'L':
#     cnt += 1
# if arr[0] == 'L':
#     cnt += 1
# if arr[-1] == 'S' and arr[0] == 'S':
#     cnt += 1
# if arr[-1] == 'L' and arr[0] == 'L':
#     cnt -= 1
# *LL*S*LL*S*LL*LL*