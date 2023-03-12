import sys
sys.stdin = open("input.txt")

result = 'Impossible'
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [0 for _ in range((N * M) + M + 1)]
    P = list(map(int, input().split()))
    P = sorted(P)


    print(f'#{tc} {result}')
