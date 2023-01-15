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

응답(HTML) <=

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
