# 패키지 import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 경로
csv_path = '../archive/NFLX.csv'

# csv 파일 읽어오기 (이때, 'Date', 'Open', 'High', 'Low', 'Close' 필드만 읽어오도록 구성)
new_df = pd.read_csv(csv_path, usecols=range(0, 5))

# 2021년 이후 데이터 필터링
df_after_2021 = new_df[new_df['Date'] >= '2021-01-01']

# 'Date' 열을 날짜 형식으로 변환 (데이터프레임 복사)
df_after_2021 = df_after_2021.copy()
df_after_2021['Date'] = pd.to_datetime(df_after_2021['Date'], errors='coerce')

# 월 별로 그룹화하고 평균 Close 값을 계산
df_monthly_avg_close = df_after_2021.groupby(df_after_2021['Date'].dt.to_period("M")).mean()

# 그래프 시각화
plt.plot(df_monthly_avg_close.index.astype(str), df_monthly_avg_close['Close'], label='Close')

# x 축 눈금을 두 달 단위로 표시, x축 45도 회전
plt.xticks(df_monthly_avg_close.index.astype(str)[::2], rotation=45)


# 그래프 제목 설정
plt.title('Monthly Average Close Price')

# x축 레이블 설정
plt.xlabel('Date')

# y축 레이블 설정
plt.ylabel('Average Close Price')

# 레이아웃 자동 조절
plt.tight_layout()

# 보여줘
plt.show()