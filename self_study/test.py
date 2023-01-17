# i = 1
result = 0
for i in range(1,1000):
    # a = 2 * i
    # b = 7 * i
    # if a < 1000 and a != b:
    #     print(a)
    #     result += a
    # if b < 1000:
    #     print(b)
    #     result += b
    if i%2 == 0 or i%7 == 0:
        result += i
print(result)

