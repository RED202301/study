import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
T = int(input())
arr = [[0 for _ in range(N+1)] for _ in range(M+1)]
arx = []
ary = []
xs = 0
xh = 0
xl = 0
yh = 0
yl = 0
ys = 0
shlx = []
shly = []
for _ in range(T):
    x, y = map(int, input().split())
    if x == 0:
        arx.append(y)
        arx = sorted(arx)
    if x == 1:
        ary.append(y)
        ary = sorted(ary)
if len(arx) != 1:
    for i in range(len(arx)-1):
        xs = arx[i+1] - arx[i]
        xh = M - arx[-1]
        xl = arx[0] - 0
        shlx.append(xs)
        shlx.append(xh)
        shlx.append(xl)
    print(shlx)
else:
    if M - arx[0] >= arx[0] - 0:
        xs = M - arx[0]
    else:
        xs = arx[0] - 0


if len(ary) != 1:
    for j in range(len(ary)-1):
        ys = ary[j+1] - ary[j]
        yh = M - ary[-1]
        yl = ary[0] - 0
        shly.append(ys)
        shly.append(yh)
        shly.append(yl)
    print(shly)

else:
    if N - ary[0] >= ary[0] - 0:
        ys = N - ary[0]
    else:
        ys = ary[0] - 0
# print(xs * ys)

# if len(arx) == 1:
#     if M - arx[0] > arx[0] - 0:
#         result = M - arx[0]
#     else:
#         result = arx[0] - 0
# else:
#     for i in range(len(arx)-1):
#         for j in range(i+1, len(arx)):
#             if arx[i] > arx[j]:
#                 k = arx[i] - arx[j]
#                 k1 = M - arx[i]
#                 k2 = arx[j] - 0
#             else:
#                 arx[i], arx[j] = arx[j], arx[i]
#             resu.append(k)
#             resu.append(k1)
#             resu.append(k2)
#     result = max(resu)
# if len(ary) == 1:
#     if N - ary[0] > ary[0] - 0:
#         res = N - ary[0]
#     else:
#         res = ary[0] - 0
# else:
#     for i in range(len(ary) - 1):
#         for j in range(i + 1, len(ary)):
#             if ary[i] > ary[j]:
#                 u = ary[i] - ary[j]
#                 u1 = N - ary[i]
#                 u2 = ary[j] - 0
#             else:
#                 ary[i], ary[j] = ary[j], ary[i]
#         resw.append(u)
#         resw.append(u1)
#         resw.append(u2)
#     res = max(resw)
#
# print(result * res)
#













# result = []
# res = []
# arx = []
# ary = []
# k = 0
# k1 = 0
# k2 = 0
# u2 = 0
# u = 0
# u1 = 0
#     if x == 0:
#         arx.append(y)
#     else:
#         ary.append(y)
#
# for i in range(len(arx)-1):
#     for j in range(i+1, len(arx)):
#         if arx[i] > arx[j]:
#             k = arx[i] - arx[j]
#             k1 = M - arx[i]
#             k2 = arx[j] - 0
#         else:
#             arx[i], arx[j] = arx[j], arx[i]
#     result.append(k)
#     result.append(k1)
#     result.append(k2)
# if len(result) == 0:
#     if len(arx) == 1:
#         k = M - arx[0]
#         k1 = arx[0] - 0
#         if k < k1:
#             k = k1
# else:
#     k = max(result)
#
# k = max(result)
# for i in range(len(ary) - 1):
#     for j in range(i + 1, len(ary)):
#         if ary[i] > ary[j]:
#             u = ary[i] - ary[j]
#             u1 = N - ary[i]
#             u2 = ary[j] - 0
#         else:
#             ary[i], ary[j] = ary[j], ary[i]
#     res.append(u)
#     res.append(u1)
#     res.append(u2)
# if len(res) == 0:
#     if len(ary) == 1:
#         u = N - ary[0]
#         u1 = ary[0] - 0
#         if u < u1:
#             u = u1
# else:
#     u = max(res)


# print(u * k)


    # print(max(result) * max(res))
    # k = 0
    # o = 0
    # if x == 1:
    #     k = N - y
    #
    # if x == 0:
    #     o = M - y
    #
    # print(o)
    # if result < k:
    #     result = k
    # if res < o:
    #     res = o

# print(result * res)


