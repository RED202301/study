import sys
sys.stdin = open("input.txt")

N = int(input())


answer = 0
for i in range(1, N+1):
    answer += len(str(i))

print(answer)
    





