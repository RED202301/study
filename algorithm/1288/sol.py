import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    i = 1
    arr = [0 for _ in range(10)]
    while i != 100:
        N = N * i
        if N % 10


