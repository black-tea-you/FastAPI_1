from fastapi import FastAPI
from pydantic import BaseModel        # 요청 데이터의 유효성 검사를 위한 모델 클래스
from typing import List               # 리스트 타입 명시를 위한 typing 모듈
from konlpy.tag import Okt            # 한국어 형태소 분석기 중 하나인 Okt (Twitter 형태소 분석기) JAVA 기반 JDK 필요
from collections import Counter       # 단어 등장 횟수를 세기 위한 Counter
import re                             # 정규표현식 처리를 위한 모듈
app=FastAPI()

# 형태소 분석기 인스턴스 생성
okt = Okt()

# 뉴스에서 자주 등장하지만 의미 없는 불용어(stopwords) 리스트
stopwords = set([
    '은', '는', '이', '가', '을', '를', '에', '의', '도', '으로', '에서', '와', '과',
    '한', '하다', '했다', '하기', '한다', '등', '때', '또', '또한', '기자', '뉴스',
    '기술', '제품', '서비스', '출시', '강화', '제공', '내용', '관련', '가능'
])