# 패키지 import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 경로
csv_path = '../example/archive/google-stock-dataset-Monthly.csv'

# CSV 파일 읽어오기 (첫 번째, 마지막 열 제외)
new_df = pd.read_csv(csv_path, usecols=range(1, 7))

# 2022년 이후 데이터 필터링
df_after_2022 = new_df[new_df['Date'] >= '2022-01-01']

# 그래프 그리기
plt.plot(df_after_2022['Date'], df_after_2022['Low'], label='Low')
plt.plot(df_after_2022['Date'], df_after_2022['High'], label='High')

# 그래프 제목 설정
plt.title('High, Low Prices After 2022')

# x축 레이블 설정
plt.xlabel('Month')

# y축 레이블 설정
plt.ylabel('Price')

# 범례 표시
plt.legend()

# 그래프 표시
plt.show()
