import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    result = 'NO'
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    cnt = 0
    arx = [0 for _ in range(N)]
    ary = [0 for _ in range(N)]
    cocnt = 0
    arcor = [0 for _ in range(N)]
    arlow = [0 for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(i, i+5):
                for l in range(j, j+5):
                    if arr[i][j] == 'o':
                        arx[i] += 1
                    if arr[j][i] == 'o':
                        ary[i] += 1
    for i in range(N):
        for j in range(N-1):
            if arr[i][j+1] == 'o':
                arcor[i] += 1
            if arr[j][i-1] == 'o':
                arlow[i] += 1


    for i in range(N):
        if arr[i][i] == 'o':
            cnt +=1

    for i in range(N):
        if arr[i][N-i-1] == 'o':
            cocnt += 1

    for i in range(N):
        if arx[i] >= 5 or ary[i] >= 5 or arcor[i] >= 5 or arlow[i] >= 5:
            result = 'YES'
    if cnt >= 5 or cocnt >= 5:
        result = 'YES'
    print(f'#{tc} {result}')
