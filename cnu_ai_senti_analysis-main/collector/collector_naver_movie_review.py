import math

import requests
from bs4 import BeautifulSoup
import re

###################
# 1. 영화 제목 수집 #
###################

# movie_code :네이버 영화 코드(6자리 숫자)

# 제목 수집
# 함수
# - 1.생성 2. 호출
# - 함수는 생성하면 아무 동작 X
# - 반드시 생성 후 호출을 통해서 사용!

def movie_title_crawler(movie_code):
    url = f'https://movie.naver.com/movie/bi/mi/point.naver?code={movie_code}'
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')
    title = doc.select('h3.h_movie > a')[0].get_text()
    return title



# 리뷰 수집(리뷰, 평점, 작성자, 작성 일자 ) + 제목

def movie_review_crawler(movie_code):
    title = movie_title_crawler(movie_code)  # 제목 수집
    # 리뷰를 수집하는 코드 작성

    print(f'>> Start collecting movies for {title}')
    url = f'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code={movie_code}&type=after&onlyActualPointYn=N&onlySpoilerPointYn=N&order=sympathyScore&page=1'
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')
    all_count = doc.select('strong.total >em ')[0].get_text()  # 리뷰 전체 수

    # "2,480" : str type(문자열)
    #         : int type(정수형 숫자)
    # ex ) 문자 /10 나눗셈? --> X
    # print(type(all_count))
    # "2480" -> 2480 (O)
    # "2,480" -> 문자 포함 변환 (X)
    # 1. 숫자만 추출: 정규식 이용
    numbers = re.sub(r'[^0-9]', '', all_count)
    pages =math.ceil(int(numbers)/10)  # 만약 2485 건 -> 10으로 나누면 나며지 5 => 올림 해줌
    print(f'The total number of pages to collect is {pages}')  # 마지막 페이지 번호

    # 해당 페이지 리뷰 수집
    count = 0  # 전체 리뷰 수를 count

    for page in range(1, pages+1):
        url = f'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code={movie_code}&type=after&onlyActualPointYn=N&onlySpoilerPointYn=N&order=sympathyScore&page={page}'
        result = requests.get(url)
        doc = BeautifulSoup(result.text,'html.parser')
        review_list = doc.select('div.score_result >ul>li')  # 1page의 리뷰 10건
        for i,one in enumerate(review_list): # 리뷰 1건씩 수집
            # 리뷰, 평점, 작성자, 작성일자

            review = one.select('div.score_reple> p > span')[-1].get_text().strip()
            score = one.select('div.star_score > em')[0].get_text()  #평점, -1 은 맨 마지막
            print(f'# Review: {review}')
            print(f'# Score: {score}')
        break




    # set {제목, 리뷰, 평점, 작성자, 작성 일자}

