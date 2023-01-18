##### 잘못된 스타일 가이드 예시

ex)

1. ''와 ''''번갈아가면서 쓰지 않기

2. 들여쓰기는 4칸 or tab 그리고 같은 칸을 들여쓰기해야함

3. 변수선언 및 할당 쓸때는 붙여쓰면 안됨

4. 한 코드 내에는 반드시 한 종류의 들여쓰기만 가능

True == 1

Falsy == 0

> 미세먼지 외출정도 출력하기

```python
dust = int(input())
if dust > 150:
    print("매우 나쁨")
    if dust > 300:
        print("실외 활동을 자제해 주십시오.")
elif dust > 80:
    print("나쁨")
elif dust > 30:
    print("보통")
elif >= 0:
    print("좋음")
else:
    print("값이 잘못되었습니다.")
print("미세먼지 확인완료")
```

##### 조건표현식

```python
num = 10
value = num if num >= 0 else -num
```

> 4줄 분량의 조건식을 축야할 때 사용가능

##### 반복문의 제어

1. break : 조건이 되었을 때 반복문을 종료(빠져나옴)

2. continue : 조건이 되었을 때 이를 넘기고 다시 조건을 시작

3. for-else
   
   - 끝까지 반복문을 실행한 이후에 else 문 실행
     
     - break를 통해 중간에 종료되는 경우 else 문을 실행되지 않음

4. pass : 아무의미 없음 (문법상 필요할 때)

##### List Comprehension : 표현식으로 간결하게 리스트를 표현

```python
[code for 변수 in iterable]

[code for 변수 in iterable if 조건식]
```

enumerate 순회

- enumerate()
  
  - 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환
    
    - (index,value) 형태의 tuple로 구성된 열거 객체를 반환

```python
members = ['민수', '영희', '철수']

for idx, number in enumerate(members):

    print(idx, number)

...

0 민수

1 영희

2 철수

...
```

> 번호와 value를 보여줌 여기서 추가하고 싶다면 
> 
> for 문에(enumerate(members, <mark>start = 1</mark>):
> 
> start = 1을 붙이면 됨

- 추가 메서드를 활용하여 순회할 수 있음
  
  - keys() : key로 구성된 결과
  
  - values() : value로 구성된 결과
  
  - items() : (key,value)의 튜플로 구성된 결과

```python
grades = {'john': 80, 'eric': 90}
print(grades.keys())
print(grades.values())
print(grades.items())
...
dict_keys {['john', 'eric']}
dict_values {[80, 90]}
dict_items {[('john', 80), ('eric', 90)]}
```

```python
grades = {'john': 80, 'eric' : 90}
for student, grade in grades.items():
    print(student, grade)
...
```

---

함수의 결괏값(output) : return도 있어도 되고 없어도 됨 없어도 None 이 나옴

함수의 입력(input) : parameter는 있어도 되고 없어도 됨

함수의 범위(Scope) : 변수의 제한 범위 (내가 찾고자하는 변수가 존재하는 프로그램 상의 범위) 찾는 순서 => LEGB

- print 함수와 return의 차이점
  
  - print를 사용하면 호출될 때마다 값이 출력됨(주로 테스트를 위해 사용)
  
  - 데이터 처리를 위해서는 return 사용

> print는 단지 확인을 위해서 출력이 끝 return은 밖으로 빼냄

---

> ### 함수

len 함수 X

sum 함수 X

- return은 두 개이상이 안되기에 ,를 찍고 이어서 써줌 ex) x - y, x * y[이거는 튜플형식을 묶어줌]
1.  dict로 묶어주지 않는 이유 k : v형태이기에 구조상 안됨

2.  set로 묶지 않는 이유 : 중복값이 있을 수 없다는 특징 때문에 set는 할 수 없음

3.  list로 묶지 않는 이유 :  변동 값이기에 list는 할 수 없음 

4. Tuple로 묶는 이유 : immutalbe이기에 가능\
   
   > 구조, 중복, 변동의 이유가 있기에 tuple `but` 내가 변동값을 쓰고 싶으면 list로 묶어도 된다.

```python
if x < y:
    return x * y
else:
    return x - y
```

> 함수 종료 시점은 return하는 순간 끝이남



##### positinal argument의 형식 : 순서대로

```python
def add(x, y):
    return x + y
add(1) / add(2, 3, 4) #처럼하면 오류날 수 있음
```



##### keyword argument의 형식 : 직접 키워드 지정

keyword 함수가 먼저 나올 수 없는 이유



```python
def add(x, y):
    return x + y
add(x = 3, 2) # 함수는 앞에부터 채우기 x = 3을 먼저넣어버리면
# 3과 2가 둘다 x로 가기에 충돌이일어남
```

> (y = 2, x = 3) 의 형태는 가능



##### Default argument values

```python
def add(x, y=0):

    return x + y

add(2, 3)
```

range(5)

range(1, 5)가 가능한 이유는 range의 시작점이 0부터 default값이 설정되어있는 것



##### python의 범위

각 범위들은 본인 기준이기에 local에서 enclose였던 부분도 enclose에선 local임

위치 보는 함수 print(locals())

  print(globals())
