import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        wcnt = 0
        bcnt = 0
        rcnt = 0
        for j in range(M):
            if arr[i][j] == 'W':
                wcnt += 1
            elif arr[i][j] == 'B':
                bcnt += 1
            elif arr[i][j] == 'R':
                rcnt += 1

        print(wcnt)
        print(bcnt)
        print(rcnt)
        print('#'*7)
