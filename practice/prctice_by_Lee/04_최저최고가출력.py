# 패키지 import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 경로
csv_path = '../example/archive/google-stock-dataset-Monthly.csv'

# CSV 파일 읽어오기 (첫 번째, 마지막 열 제외)
df = pd.read_csv(csv_path, usecols=range(1, 7))

# 그래프 그리기
plt.plot(df['Date'], df['Close'], label = 'Close')
plt.plot(df['Date'], df['Low'], label = 'Low')
plt.plot(df['Date'], df['High'], label = 'High')

# 그래프 제목 설정
plt.title('High, Low Prices over Time')

# x축 레이블 설정
plt.xlabel('Date')

# y축 레이블 설정
plt.ylabel('Price')

# 범례 표시
plt.legend

# 그래프 표시
plt.show()
