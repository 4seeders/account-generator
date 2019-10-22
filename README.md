# python을 이용한 svn, redmine, mssql 계정생성
### 개요
---
- 프로젝트의 개발환경은 svn, redmine, mssql로 구성되어 있다.
- 개발자가 투입될때마다 svn, redmine, mssql 계정을 생성해야 하고, svn 경로등을 메일로 전송해야 한다.
- 개발자가 적으면 괜찮지만 수시로 늘어나거나 줄어들 수 있다고 가정하여, 자동화 하기로 한다.

### 사용기술 및 개발환경
---
- Language : python
- Tools : visual studio code

### 목표
---
1. SVN, redmine, MSSQL 계정을 생성하는 스크립트를 작성한다. (적당히 기능별로 나눠서 작성한다.)
2. 생성한 계정정보를 메일로 전송하는 스크립트를 작성한다.

### 분석
---
- SVN 계정생성
    1. SVN Edge에 접속하여 관리자로 로그인한다.
    2. Users 메뉴로 이동하여, 생성버튼을 클릭한다.
    3. 로그인계정 정보등을 입력후 생성버튼을 클릭한다.

- redmine 계정생성
    1. redmine에 접속하여 관리자로 로그인한다.
    2. 관리페이지 메뉴아래에 있는 사용자 페이지로 이동하여, 새 사용자 버튼을 클릭한다.
    3. 로그인계정 정보등을 입력후 만들기 버튼을 클릭한다.
    4. 프로젝트 페이지로 이동하여, 구성원을 추가한다. (역할에 맞게)

- MSSQL 계정생성
    1. 관리자 계정으로 db에 접속한다.
    2. 쿼리로 사용자를 생성과 권한을 할당한다.

- 메일전송
    1. SMTP를 이용하여 TEMPLATE를 전송한다.

### 기능정리
---
1. 세션유지 (관리자 계정 로그인)
2. HTTP를 이용한 요청 전송 (로그인 사용자 정보 전송)
3. DB접속 및 쿼리 수행 (MSSQL 계정)
4. 메일전송 (GMAIL 활용)

### 개발제약사항
---
1. 각 기능별 스크립트를 작성한다.
2. 각 기능별 스크립트를 호출하는 main 스크립트를 작성한다. (endpoint, 파라미터를 보내면 되는것)
3. 매개변수 : ID, PW, 이름(성, 이름 분리필요.), 이메일 
    - 일반적으로 회사들은 그룹웨어 ID가 이메일 역할을 하므로, ID로 이메일을 만든다.
    - 호출 예 ) python 계정생성.py hong2019, "홍길동"
    - 성, 이름 분리. 성 = '홍길동'[:1], 이름 = '홍길동'[1:]

### run
---
python developer_account.py -i 'dev2014' -n '홍길동'


### 참고자료
---
1. HTTP요청, 로그인 세션 유지
    [나만의 웹 크롤러 만들기(2): Login with Session | Beomi's Tech Blog](https://beomi.github.io/2017/01/20/HowToMakeWebCrawler-With-Login/)
2. MSSQL 접속 및 쿼리 수행
    [예제로 배우는 파이썬 프로그래밍 - MSSQL 사용](http://pythonstudy.xyz/python/article/208-MSSQL-%EC%82%AC%EC%9A%A9)
3. 메일전송
    [파이썬으로 이메일 보내기(SMTP)](https://yeolco.tistory.com/93)
