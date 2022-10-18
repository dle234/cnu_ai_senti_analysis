import pprint
import requests
from bs4 import BeautifulSoup
from collector.CollectorSn import get_daum_news

url = 'https://news.daum.net/breakingnews/digital'
result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')  # 텍스트 파일을 html 파일로 읽기
title_list = doc.select('ul.list_news2 a.link_txt')
# <a href='url'>:a 태그는 클릭 했을 때 해당 url 로 이동
# len(): list[]의 갯수를 알려 주는 함수
# pretty print : pprint
# pprint.pprint(title_list)
# print(len(title_list))
# enumerate(): 반복 하면서 index 번호와 item 을 모두 가져옴
# list[]의 index 는 0번 부터 시작
# len(list)= 15, index = 0~14
for i, title in enumerate(title_list):
    print(f'인덱스: {i+1}, url: {title["href"]}')  # []안에 속성값 써주면 그 속성을 가진 요소 가져옴
    get_daum_news(title["href"])       # 뉴스 제목, 본문 수집 함수



