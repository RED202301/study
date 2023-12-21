import sys
sys.stdin = open("input.txt")

T = int(input())
arr = list(map(int, input().split()) for _ in range(T))

print(arr)