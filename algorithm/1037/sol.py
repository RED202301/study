import sys
sys.stdin = open("input.txt")

K = int(input())
arr = list(map(int,input().split()))
answer = 0

if K >= 2:
    answer = min(arr) * max(arr)
else:
    answer = min(arr) * max(arr)

print(answer)