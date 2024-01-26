# 패키지 import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# CSV 파일 경로
csv_path = '../archive/NFLX.csv'

# csv 파일 읽어오기 (이때, 'Date', 'Open', 'High', 'Low', 'Close' 필드만 읽어오도록 구성)
df = pd.read_csv(csv_path, usecols=range(0, 5))

# 'Date' 열을 날짜 형식으로 변환
df['Date'] = pd.to_datetime(df['Date'])

# 2021년 이후 데이터 필터링
df_after_2021 = df[df['Date'].dt.year >= 2021]

# 그래프 그리기
plt.plot(df_after_2021['Date'], df_after_2021['Close'], label='Close')

# 그래프 제목 설정
plt.title('NFLX Close Price')

# x축 레이블 설정
plt.xlabel('Date')

# y축 레이블 설정
plt.ylabel('Close Price')

# x축에 월별로 눈금 표시
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=2))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# 그래프 시작 월을 2021년 1월로 설정
plt.gca().set_xlim([pd.Timestamp('2021-01-01'), df_after_2021['Date'].max()])

# 범례 표시
plt.legend()

# 레이아웃 자동 조절
plt.tight_layout()

# 그래프 표시
plt.show()