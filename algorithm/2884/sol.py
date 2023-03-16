import sys
sys.stdin = open("input.txt")
T = int(input())
for _ in range(T):
    n = int(input())
    num = []
    k = []
    for i in range(2, n):
        cnt = 0
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
        if cnt == 0:
            num.append(i)


    result = n
    for l in range(len(num)):
        for p in range(len(num)):
            if num[p]+num[l] == n:
                if num[p] == num[l] == 0:
                    k = num[p], num[l]
                else:
                    if result > abs(num[p]-num[l]):
                        result = abs(num[p]-num[l])
                        k = num[l], num[p]


    print(*k)