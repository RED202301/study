import sys
sys.stdin = open("input.txt")
sum = 0
max_ = 0
min_ = 0
result = 0
for i in range(10):
    N = int(input())
    sum += N
    if sum >= 100:
        max_ = sum
        min_ = sum - N
        break

a = max_ - 100
b = 100 - min_
if a <= b:
    result = max_
if a > b:
    result = min_


print(result)


#     if sum < N:
#         sum += N
#         if sum > N:
#             sum = sum - N
# print(sum)