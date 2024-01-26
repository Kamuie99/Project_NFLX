# 패키지 import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 경로
csv_path = '../example/archive/google-stock-dataset-Monthly.csv'

# CSV 파일 읽어오기 (첫 번째, 마지막 열 제외)
df = pd.read_csv(csv_path, usecols=range(1, 7))

# 가장 최근을 제외한 마지막 1년 추출
df = df.tail(13)

# 마지막 개월의 Close 가격
last_month_close = df['Close'].iloc[-1]

# 마지막 개월을 제외한 1년의 데이터와 마지막 개월의 증가 간의 상관 관계
High_Close_corr = df['High'].iloc[:-1].corr(df['Close'])
Low_Close_corr = df['Low'].iloc[:-1].corr(df['Close'])
Volume_Close_corr = df['Volume'].iloc[:-1].corr(df['Close'])

# 그래프 그리기
plt.plot(df['Date'], df['Close'], label='Close')
plt.plot(df['Date'], df['Low'], label='Low')
plt.plot(df['Date'], df['High'], label='High')

# 그래프 제목 설정
plt.title('High, Low Prices over Time')

# x축 레이블 설정
plt.xlabel('Date')

# y축 레이블 설정
plt.ylabel('Price')

# x축 설정(회전시키기)
plt.xticks(rotation=45)

# 범례 표시
plt.legend()

# 그래프 표시
plt.show()
