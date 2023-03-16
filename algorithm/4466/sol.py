import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    arr = arr[::-1]
    sum_ = 0
    for i in range(K):
        sum_ += arr[i]
    print(f'#{tc} {sum_}')
