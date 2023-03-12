import sys
sys.stdin = open("input.txt")


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    a = N // 50000
    N = N % 50000
    b = N // 10000
    N = N % 10000
    c = N // 5000
    N = N % 5000
    d = N // 1000
    N = N % 1000
    e = N // 500
    N = N % 500
    f = N // 100
    N = N % 100
    g = N // 50
    N = N % 50
    h = N // 10
    N = N % 10
    print(f'#{tc}')
    print(a, b, c, d, e, f, g, h)