import sys
sys.stdin = open("input.txt")

E, S, M = map(int, input().split())

i = 1
while True:
    if ((i-E) % 15 == 0) and ((i-S) % 28 == 0) and ((i-M) % 19 == 0):
        break 
    i += 1


print(i)