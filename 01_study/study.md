- # vs 코드

- json =>  java script object notation
  
  API 요청(python) 응답(서버)

> JS란?

DoM 웹페이지 조작가능한 유일한 언어

code --version  : 버전 확인

json 은 파이썬 딕셔너리 처럼 표현  

> 쉼표 까먹지 말자 들여쓰기는 상관 없음

# 파이썬 기초

> 함수

```
반복 하고 싶은 코드 덩어리를 모아 놓은 것
```

- INPUT X => FUNCTION f: => OUTPUT f(x)

- Excel에서의 하수(function)

sum(), average(), count()

## 파이썬 함수

Built in functions (내장함수)

Non - built- in functions

python - 내장함수 : 구글에 python Built-in-functions 검색하면 다 나옴

abs() - 절댓값

len() -길이

- len : 길이, 개수(List,Dictionary)

> 모듈

: 함수나 변수 등을 모아 놓은 파이썬 파일

모듈사용(random 모듈사용 (실습함))

1. 함수가 포함된 파일을 불러온다.(import)

2. 함수를 사용한다

커서 두고 알트 쉬프트 방향키 하면 복사

알트 방향키는 줄바꿈

요청과 응답

클라이언트(정보를 원하는) <=> 서버(정보를 주는)

요청 - 주소(URL) =>

응답(HTML) <= json을 받아옴

data[result][:0]

---

> JSON

- 데이터만을 주고받기위한표기법

- 파이썬의 `Dictionaray`와  `List`구조로 쉽게 변환하여 활용가능

- `API`의 응답으로 많이 이용

> `API`

소프트웨어가 서로 통신할 수 있도록 연결해주는 인터페이스

`Application Programing Interface`

주소 뒤에 ? k(키값과)=밸류(V)

key => api 서버개발자 => client

ex)

name : ??

파이썬 <-> agify.io 

`requests library`(패키지를 다르게 부르는 용도)(내장함수가 아님 => 외부 라이브러리(3rd party library) : import 써야함

파이썬에서 요청을 쉽게 보낼 수 있게 도와주는 모듈(파일)

python requests install 다운로드 하는 법 (공식문서(python을 봐야함)

pip install requests

- 설치 확인법

pip list

- requests library
  
  파이썬에서 요청을 쉽게 보낼 수 있게 도와주는 모듈
  
  import requests

- r = requeste.get~~~
  
  print(r)
  
   실행방법
  
  python random_age.py
  
  200 은 성공

- 404 - page not fine
  
  200 - ok
  
  500 - server 터짐
  
  2 : 성공(정상적 작동)
  
  4 : 니가 잘못함(유저(요청자(클라이언트))가 잘못함) : 없는데 니가 잘못보낸 거 아니야?
  
  5 : 서버가 잘못함(서버에 무슨일이 벌어짐)=> 서버에서 작성된 코드가 잘못된 것 등

> 400번대 중요 why? : 항상 요청자가 잘못함 / 401 : 인증이 안됨/ 403 : 권한이 없음

- API

- Web

json 함수 json을 파이썬에서 볼 수 있게 하는 함수

API - 실습 LOTTO

주어진 url을 이요해 로또 1021회차 당첨 번호 수집 - ?method (key값)  => &method = edit/ value(getLottoNumber) /  name => 무엇이든 반환 , method => edit(기존 요청 수정)/ create => 생성하는 것

https:// => 하이퍼 프로토콜 전송 규약

notion => 인터넷 https://

                   휴대폰 notion://

파이썬으로 웹 요청 보내기

api 파이썬 창에서 보는 방법

for key, value in r.item():

print(key, value, sep = " ")

sep => ""칸만큼 띄운다

---

input("회차를 입력해주세요 : ")

---

동행복권 로또 당첨번호 api 사용 ; (회차 직접 입력 ) -> 숫자 문자 상관없음

api 보고 입력 6개 번호면 일일이 다 입력 r[''] 구조 

---

함수 선언 한 것은 괄호로 묶어줄 필요가 없음

---

교수님 답변

num = input()

url = 'https://www~'

response = requests.get(url)    .json(을 붙이면 값이 나옴)

print(response)

hook : 특정유저에게 보내는 기록을 가져옴

> 변수의 조건 4가지

- 식별자의 이름은 영문 알파벳, 언더스코어(__), 숫자로 구성

- 첫글자에 숫자가 올수 없음

- 길이 제한이 없고, 대소문자를 구별

- 다음의 키워드는 선언 못함

 안녕하세요
