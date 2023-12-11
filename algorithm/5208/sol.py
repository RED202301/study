import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]
    M = arr[1:]
    # print(N)
    # print(M)
    arr_ = [0 for _ in range(N)]
    for i in range(len(M)):
        arr_[i] = M[i]
    cnt = -1
    k = 0
    while k != N:
        if k < N:
            result = arr_[k]
            k += arr_[result]
            cnt += 1
        elif k == N:
            print(cnt)

        elif k > N:
            cnt -= 1
            break


    print(cnt)
