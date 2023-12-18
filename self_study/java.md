JAVA 프로그램의 기본 구조

```java
public class Hello {
    public static int sum(int n, int m) {
    return n + m;
}
public static void main(String[] args) {
    int i = 20;
    int s;
    char a;

    s = sum(i, 10);    
    a = '?'
    System.out.println(a);
    System.out.println("Hello");
    System.out.println(s);
}
}
```

ans) ?

Hello

30

## Java 프로그램의 구조

- 클래스만들기 

```java
public class Hello {

}
```

- 자바 프로그램은 main() 메소드에서부터 실행을 시작한다.

```java
public static void main(String[] args) {

}
```

> 한 클래스에 두 개 이상의 main()을 가질 수 없다.
> 
> **실행**을 시작할 클래스만 main()을 가짐

- 메소드란?
1. C/C++ 함수를 자바에서는 method라고 부른다.

2. 반드시 클래스 내에 작성되어야 한다.

ex)

```java
public static int sum(int n, int m) {
    return n + m;
}
```

- 메소드 호출

```java
s = sum(i, 10); 
```

- 변수 선언

```java
int i = 20;
s = sum(i, 10);
```

- 문장
  
  자버에서 모든 문장은 ;(세미 콜론)으로 끝나야 한다.

- 화면 출력
  
  정수, 문자, 문자열 등 데이터를 화면에 출력하기 위해 System.out.println()을  이용하며, 사용 예는 다음과 같다. System.out.println() 은 출력 후 다음 행으로 이동하지 



식별자 



식별자란 클래스, 변수, 상수, 메소드에 붙이는 이름을 말한다.

규칙

특수문자, 공백, 식별자로 사용할 수 없으나 '_', '$'는 예외

if, while, class 등 자바ㅏ 언어의 키워드는 식별자로 사용할 수 없다.

식별자의 첫 번째 문자로 숫자는 사용할 수 없다.

true, false, null은 식별자로 사용 불가

대소문자 구별

길이 제한 X
