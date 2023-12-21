import sys
sys.stdin = open("input.txt")

arr = []
sum_ = 0
for _ in range(9):
    N = int(input())
    arr.append(N)
    sum_ += arr[_]
arr = sorted(arr)
L = 0
K = 0
for i in range(9):
    for j in range(9):
        if i != j:
            if sum_ - arr[i] - arr[j] == 100:
                L = i
                K = j

for m in range(9):
    if m != L and m != K:
        print(arr[m])        
        


