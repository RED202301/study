# # student = {'홍진환': 50, '김성현': 50, '홍진환': 30}
# student = {'강남구':'비싸다', 
# '종로구':[1, 2, 3], 
# '서대문구': {
#     '김구현':13,
#     'viktor':['여기도', 'dict의', 'value이다.']
#     }
# }

# menu = [['아침', '점심', '저녁'], {'강남구':50, '서대문구':47}]

# print(student)
# print(menu)
# print(menu[0][1])
# print(menu[1]['서대문구'])
# print(student['서대문구']['viktor'][1])

year = int(input())
if year % 4 == 0 and year % 100 != 0:
    print('윤년')
elif year % 400 == 0:
    print('윤년')
else:
    print(year)