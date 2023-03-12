import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    sum_ = 0
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    m = N // 2
    # for i in range(N):
    #     for j in range(abs(m-i), N - abs(m-i)):
    #         sum_ += arr[i][j]


    s = e = m
    for i in range(N):
        for j in range(s, e + 1):
            sum_ += arr[i][j]
        if i < m:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    print(f'#{tc} {sum_}')
