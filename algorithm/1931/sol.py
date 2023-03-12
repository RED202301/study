import sys
sys.stdin = open("input.txt")

T = int(input())
arr = [[] for _ in range(25)]
for _ in range(T):
    n, k = map(int, input().split())
    arr[n].append(k)
k = []
print(arr)
for i in range(25):
    try:
        if i+1 < arr[i][0]:
            k.append(i+1)
            k.append(arr[i][0])
    except IndexError:
        pass
print(k)