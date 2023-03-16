import sys

sys.stdin = open("input.txt")

N = int(input())
cnt = 1
for i in range(N):
    for j in range(N):
        if i * j < N:
            cnt += 1
    print(cnt)
