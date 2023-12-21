import sys
sys.stdin = open("input.txt")

N = input()
C = int(input())
BP = list(map(int, input().split()))

print(N[0])

for i in N:
    
    if i != 