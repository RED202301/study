import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T +1):
    N, Q = map(int, input().split())
    arr = [0 for _ in range(N)]
    for _ in range(Q):
        L, R = map(int, input().split())
        for i in range(L, R+1):
            arr[i-1] = (_+1)

    print(f'#{tc}', *arr)