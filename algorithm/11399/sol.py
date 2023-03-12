import sys
sys.stdin = open("input.txt")

n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)

sum_ = 0
for i in range(n+1):
    for j in range(i):
       sum_ += arr[j]

print(sum_)