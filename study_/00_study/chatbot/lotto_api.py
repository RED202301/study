# # # 파이썬으로 웹 요청 보낼 수 있는 라이브러리 불러오기

# # # 동행복권 로또 당첨번호 api 사용하기
# # # (회차 직접 입력) -> 숫자 문자 상관없음
# # # 입력받은 회차에 해당하는 당첨번호 확인하기 -> 6개 (보너스번호 제외)

# # # (선택사항)  - 보너스 번호 확인하기

# # import requests

# # num = input('회차를 입력해주세요 : ')
import random
import requests
num = 1049
url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
r = requests.get(url).json()

# # # for key, value in r.items():
# # #     print(key,value,sep = "     ")

# # print(num, '회차의 로또번호는', r['drwtNo1'], r['drwtNo2'], r['drwtNo3'], r['drwtNo4'], r['drwtNo5'], r['drwtNo6'], '입니다', sep =" ")


# #4 이걸 1000번 반복한다.
# # 1. 로또 번호 6개를 추첨받는다.
# # 2. 내가 추첨 받은 6개 번호가 1049회차 당첨 번호와 일치 하는지 확인한다.
#     # 2-1. 확인하는 방법은 내 번호 6개를 순회하면서 1049회 당첨번호 목록에 해당 숫자가 있는지
#     # 있다면 적중 횟수 + 1
#     #numbers = [1, 2, 3, 4, 5,]
#     # if 3 in numbers:
#     # print(True)
# # 그래서 당첨 번호가 6개 면 1등
# # 5개면 3등
# # 4개면 4등
# # 3개면 5등
# # 2개이하면 꽝을 출력한다.
# import random
# import requests

# numbers = list(range(1, 46))

# num = 1049
# r = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}').json()

# lotto_ = [r['drwtNo1'], r['drwtNo2'], r['drwtNo3'], r['drwtNo4'], r['drwtNo5'], r['drwtNo6']]

# for t in range(100000):
#     lotto = random.sample(numbers, k = 6)

#     d=0
#     numbers_ = list(range(6))
#     for i in numbers_:
#         if lotto[i] in lotto_:
#             d = d + 1


#     if d == 6:
#         print("1등")
#     elif d == 5:
#         print("3등")
#     elif d == 4:
#         print("4등")
#     elif d == 3:
#         print("5등")
#     else:
#         print("꽝")

numbers = list(range(1, 7))
win_num = []
#coun_list["1등"] = count_list["1등"] + 1
for no in numbers:
    win_num.append(r[f'drwtNo{no}'])
print(win_num)

count_list = {
    "1등": 0,
    "2등": 0,
    "3등": 0,
    "4등": 0,
    "5등": 0,
    "꽝": 0,
}
for _ in range(100000):
    my_num = random.sample(range(1, 46), 6)
    count = 0
    for num in my_num:
        if num in win_num:
            count = count + 1

    if count == 6:
        count_list['1등'] = count_list['1등'] + 1
        #print("1등")
    elif count == 5 and r['bnusNo'] in my_num:
        count_list['2등'] = count_list['2등'] + 1
    elif count == 5:
        count_list['3등'] = count_list['3등'] + 1
        #print("3등")
    elif count == 4:
        count_list['4등'] = count_list['4등'] + 1
        #print("4등")
    elif count == 3:
        count_list['5등'] = count_list['5등'] + 1
        #print("5등")
    else:
        count_list['꽝'] = count_list['꽝'] + 1
        #print("꽝")

print(count_list)

  # count = len(set(my_num) & set(win_num))