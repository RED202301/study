# ✔ Why Git & Github

**Git이란**

: 분산 버전 관리 시스템

1. 분산 버전 관리 프로그램
   
   - 코드의 히스토리(버전)을 관리하는 도구
   
   - 개발되어온 과정 파악 가능
   
   - 이전 버전과의 변경 사항 비교 및 분석

> 버전 : 컴퓨터 소프트웨어의 특정 상태

> 관리 : 어떤 일의 사무, 시설이나 물건의 유지,개량

> 프로그램 : 컴퓨터에서 실행될 때 특정 작업을 수행하는 일련의 명령어들의 모음

버전 관리 : ex)  1. 파일에 날짜와 시간을 기입 2. <mark>변경사항</mark>을 기록하는 파일 3. 맨 나중 파일과, 이전 변경사항만 남겨

> 각 부품들을 따로 조립 기록 후 마지막 버전에서 합치기만 하면 됨 => 이를 자동으로 해주는 것이 깃(`GIT`)

**Git** 과 GitHub는 다르다

: 집과 강의장에서 공부한 것을 하나로 합치거나, 함께 관리 하고 싶으면 사용하면 좋음

: Git 기반의 저장소 서비스를 제공하는 서비스

GitHub => 공개적임 : 공부, gitlab 제외한 대부분, 교재, pdf,  ppt 등을 제외하고 올려도 됨

GitLab : 원격저장소 / 프라이빗한 공간 ex) ssafy사람들만 볼 수 있는 ssafy 전용 pjt, hw

Bitbucket

# ✔ CLI & Markdown

# ✔ Git 기본기

README.md

repository

:특정 디렉토리를 버전 관리하는 저장소 

- 한 폴더안에 있는 여러 파일들을 함께 관리할 수 있는 수정사항들을 기록할 수,모을 수 있는 repository(저장소)

<mark>git.init</mark> 명령어로 로컬 저장소를 생성(git 초기화 git 폴더 생성)

.git 디렉토리에 버전 관리에 필요한 모든 것이 들어있음

master => branch(누가 관리하는가?)

README.md 생성하기

- 새폴더를 만들고 README.md 파일을 생성해 주세요.

- 이 파일을 버전 관리하며 Git을 사용해 봅시다.

- -> 특정 버전으로 남긴다. => "커밋(commit)"한다. : 3가지 영역을 바탕으로 동작~!
  
  지금까지의 내용을 버전으로 남긴다.

- working Directory : 내가 작업하고 있는 실제 디렉토리 : 실제로 작업한 파일 => 깃으로 관리한 것 아님

- Staging Area : 커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳 : 깃에서 관리하는 것

- Repository : 커밋들이 저장되는 곳

> untracked(파일) -> git add => staged(tracked) -> git commit => committed(tracked)

✔ 깃 commit 추가 방법

git add XXX.md(확장자)

git status (확인)

git config -m "아무이름/ 파일명""

git config  --global --list

git commit -m "아무이름/ 파일명"

git log

---

git 막힐때 q(quit)

---

ctrl + L => 현재 작성 중인 코드 제일 상단으로 옮겨줌

---

git log 간단하게 보고 싶을 때 

git log --oneline

git log  직관적으로 보고싶을때

git log --oneline --graph

---

# Git Hub

git commit 만 눌러서 문제가 생길 경우 insert나 i를 누르면 됩니다.

second commit 후 ESG 후 insert모드 자리에 :붙이고 wq(writequit)[대문자안됨]

vim ~/.gitconfig

code ~/.gitconfigg

<mark>git remote add origin http://git~~~<m</mark>ark>~~</mark>

저 주소를 origin이라는 별명에 추가해 원격으로 관리하겠다.

git remote -v 로그 보여줘

<mark>git push</mark> : 원격저장소에 저장한 파일을 올려줘 git아

=> 어디에 올릴지 물어봄 : git push origin master /;; ex) git push git 별명이름 master(권한, main이면 main)

git remote remove origin : 원격저장소 잘못 넣었을 때 지우는 방법

Gcl 이 연결되었다는 것을 확인하는 방법

:검색 자격증명관리자

windows 자격증명

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

---

git clone url 주소 : git에서 파일 가져오기

clone : 최초로 관리파일(git)을 가져올 때만 사용(원격저장소와 연결할 때만 사용)

git pull : 자료 가져옴

add commit push

---

git pull

mv test.md study.md : 이름 바꾸기

git commit -m "edit file name"

push

---

git add . : 모든 파일 가져옴ㅎ

git config --global user.name  이메일 입력~

cmd 에서 강제종료

cmd : microsoft Corporation 

tasklist

taskkill /pid 8040

taskkill/F /pid 8040

code ~./bashrc => vs코드 설정

alias jp="jupyter notebook" `공백 X`

source ~/.bashrc로 확인

b -> 아래 한줄 추가

a => 위로 한줄 추가

dd =>  그줄 삭제

실수로 코드입력했을 시 위에 종료 or 커널에 restart clear

jp 나올때 컨트롤 c 2번 3번 정도하고 bash나와지면 jp끄기log
