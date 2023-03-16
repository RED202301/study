import sys
sys.stdin = open("input.txt")


N = int(input())
k = 3
u = 0
r = 0
result = 0
for i in range(N):
    if N % 5 == 0:
        r = N // 5
    if N % 3 == 0:
        u = N//3
        if N % 5  == 0:
            r = N // 5
        else:
            if ((N - (k))) % 5 == 0:
                k = k * i
                r = (N//5) + (i + 1)
        if u >= r:
            result = r
    else:
        result = -1

print(result)