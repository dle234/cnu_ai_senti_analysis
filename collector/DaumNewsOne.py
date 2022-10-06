# 주석
# ->개발자의 메모장. 파이썬이 실행 안함
#파이썬의 경로
#1. 프로젝트(cnu_ai_senti_analysis-main)
# ㄴ2. python package(collector)
#    ㄴ3.Python file(test.py, DaumNewsOne.py)
# python package: puthon file들을 모아두는 폴더
#                          폴더아이콘 안에 구멍 뚫려있음


#import와 Library(module)
# 파이썬 코들르 직접 작성해서 개발도 가능하지만 다른 개발자가
#이미 만들어놓은 코드를 사용하면 편리
# 이미 개발되어있는 코드들의 묶음=라이브러리(모듈)
# 1. built in library: Python 설치하면 자동으로 제공
#                                   예: math, sys, os 등
# 2. 위부 library : 여러분이 직접 추가해서 사용!
#                                   예: requests, beautifulsoup4 등
# 파이참 테마변경 으로 변경하기 폰트크기 바꾸기
# library 사용하기 위해서는 improt 작업 진행
#  - import 는 도서관에서 필요한 책을 빌려오는 개념


import requests
#책 전체를 빌려옴
from bs4 import BeautifulSoup
# bs4라는 책에서 Beutiful soup 1개 파트만 빌려옴

#목표 : Daum 뉴스 웹페이지 제목과 본문 데이터를 수집
# 1. url :https://v.daum.net/v/20221006105621984
url = 'https://v.daum.net/v/20221006105621984'
# 2. requests(request 도와줌)로 해당 url의 html 전체 코드를 수집

result = requests.get(url)
# print(result.text)
# response 200 : 성공, alt+shift -> 코드 위 아래로 이동가능
# 3. beautiulsoup 을 통해서'제복과 본문' 만 추출
doc = BeautifulSoup(result.text, 'html.parser')
#python 은 []: list type
#index   0 1 2 3 4 5
#      -[5,6,9,10,15]: list 내에는 다양한 데이터 저장가능
# [5] : 대괄호 벗겨줌, get_text() : 텍스트 값만 뽑아줌
title = doc.select('h3.tit_view')[0].get_text()
print(f'뉴스 제목: {title}')