import random # 모듈 -> 파이썬 파일 : ctrl 클릭하면 모듈 열어줌 or print(dir(모듈명(random))): 소문자만 봐도 충분 bec) 소문자가 함수 종류이기때문
# import를 기존 menu를 밑으로 보내고 위에 적은 이유 : 모듈, 패키지 등은 제일 위에 적음 import 여러개도 순서대로 위에서 
menu = ['닭고기온메밀국수', '토마토 리조또', '무파마', '김치찜']
print(menu)
print(menu[0])

# print(dir(random))

print(random.choice(menu))