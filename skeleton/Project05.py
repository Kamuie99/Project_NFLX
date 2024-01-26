# 패키지 import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# CSV 파일 경로
csv_path = '../archive/NFLX.csv'

# csv 파일 읽어오기 (이때, 'Date', 'Open', 'High', 'Low', 'Close' 필드만 읽어오도록 구성)
df = pd.read_csv(csv_path, usecols=range(0, 5))

# 2022년 이후 데이터 필터링
df_after_2022 = df[df['Date'] >= '2022-01-01']

# 그래프 그리기
plt.plot(df_after_2022['Date'], df_after_2022['High'], label = 'High')
plt.plot(df_after_2022['Date'], df_after_2022['Low'], label = 'Low')
plt.plot(df_after_2022['Date'], df_after_2022['Close'], label = 'Close')

# x 축 눈금을 4일 단위로 표시, x축 45도 회전
plt.xticks(df_after_2022['Date'][::4].tolist(), rotation=45)

# 그래프 제목 설정
plt.title('High, Low and Close Prices since January 2022')

# x축 레이블 설정
plt.xlabel('Date')

# y축 레이블 설정
plt.ylabel('Price')

# 범례 표시
plt.legend()

# 레이아웃 자동 조절
plt.tight_layout()

# 그래프 표시
plt.show()
