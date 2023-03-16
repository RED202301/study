import sys
sys.stdin = open("input.txt")

N = int(input())
stack = [0 for _ in range(N+1)]
arr = []
M = int(input())
k = []
for _ in range(1, M+1):
    cnt = 0
    p1, p2 = map(int, input().split())
    arr = []
    if stack != 0:
        for i in range(p1, p2+1):
            if stack[i] != 0:
                continue
            stack[i] = _
    for i in range(p1, p2 + 1):
        arr.append(i)
    k.append(arr)

u = []
p = []

for i in range(len(k)):

    u.append(len(k[i]))
    u = sorted(u)


t = 0
for i in range(len(k)):
    if len(k[i]) == u[-1]:
        p.append(i+1)
        t = p[0]

result = 0
o = ''
for _ in range(1, M + 1):
    cnt = 0
    for i in range(1, N+1):
        if stack[i] == _:
            cnt += 1
        if result < cnt:
            result = cnt
            o = _
print(t)
print(o)






#     print(i)
# print(stack)


        # if _ == stack[i]:
        #     cnt += 1


# print(stack)

# for i in range(N+1):
#     stack[i]