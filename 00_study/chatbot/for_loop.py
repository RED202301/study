numbers = [1, 2, 3, 4]

# numbers 리스트가 가진 모든 요소들을 순회할 때 까지
# numbers가 가진 각 요소를 출력
for num in numbers:
    if num % 2 == 1:
        print(num)
    elif num == 2:
        print("이")
print("남은 숫자는 :", num)

# for num in {'a': 1, 'b': 2}:
#     print(num)