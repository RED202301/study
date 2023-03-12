import sys
sys.stdin = open("input.txt")

arr = []
ar = [0 for _ in range(42)]
for _ in range(10):
    N = int(input())
    arr.append(N%42)
    for i in range(42):

        if i == arr[_]:
            ar[i] += 1
print(ar)
cnt = 0
for j in range(42):
    if ar[j] != 0:
        cnt += 1
print(cnt)