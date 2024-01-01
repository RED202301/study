import sys
sys.stdin = open("input.txt")

# N은 Number이다.
N = int(input())

# 숫자를 세기위한 count를 0으로 맞춘다.
cnt = 0
while N == 1:
    if N % 2 == 0:
        N = N%2
        cnt += 1
        print(N)
    elif N % 3 == 0:
        N = N%3
        cnt += 1
        print(N)
    else:
        N -= 1
        cnt += 1
        print(N)
    print(cnt)

# BFS로 푸는 방법으로 다시 풀어보자

    