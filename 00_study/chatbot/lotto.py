import random

numbers = list(range(1, 46))

# i = 0
# while i < 6:
#     print(random.choice(numbers))
#     i += 1
# i = 0
# while i < 5:
#     print(random.sample(numbers, k = 6))
#     i += 1

for i in range(5):
    print(random.sample(numbers, k = 6))


def sum(a, b):
    return a + b

num = sum(1, 3)
print(num)