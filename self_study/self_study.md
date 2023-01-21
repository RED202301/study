# 자율학습 1일차

### "Hello World!" 만들기

```python
print("Hello World!")
```

### 간단한 python 문법정리

> 코딩도장

## git 사용 방법

1-1 git repository 설정

- git init

1-2 README.md 작성

1-3 .gitignore 작성

1-4 git commit

1-5 git remote 설정하기

1-6 git 시나리오 연습하기

git rm --chached

git restore 

# 16진수 사용하기

```python
a = int(input())
print('%x'%a)
# x소문자, 대문자 출력이 다름 
```

```python
a = input()
n = int(a, 16)
print('%o' %n) #16진수를 8진수로 출
```

## 10진수 유니코드 출력

```python
n = ord(input()) # 문자의 순서위치
print(n)
```

> ord(): 문자의 순서위치(A:65, B: 66, C:67...)
> 
> ord(c): 문자 C를 10진수로 변환한 값

## 유니코드 문자를 10진 정수 1개

```python
c = int(input())
print(chr(c))
```

> chr() => 정수값 -> 문자, ord() => 문자->정수값

## format함수의 사용

> format(수, ".2f")를 사용하면 원하는 자리까지의 정확도로 반올림 된 실수 값을 만들어 준다. 2f => 소수점 아래 3번째 자리

```python
a = input()
a = float(a)
print(format(a, "2f"))
```

```python
a, b = map(float, input().split())
c = a/b

print("%0.3f" % c)
```

> print 할때 콤마 안넣고 %넣어서 계산한다.



## 리스트를 변수값으로 지정 받는 경우



```python
iduser_data : list
user_data['변수값']
id[-1: len(list['변수값'])]
```

> 예외처리

```python
try: if문과 동일
except: # ValueError, TypeError, 등이 있음 예외문 처리 할때 사용
```
