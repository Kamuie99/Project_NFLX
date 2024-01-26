# 패키지 import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 경로
csv_path = '../example/archive/google-stock-dataset-Monthly.csv'

# CSV 파일 읽어오기 (첫 번째, 마지막 열 제외)
df = pd.read_csv(csv_path, usecols=range(1, 7))

# CSV 파일 읽어오기 (첫 번째, 마지막 열 제외)
new_df = pd.read_csv(csv_path, usecols=range(1, 7))

# 2022년 이후 데이터 필터링
df_after_2022 = new_df[new_df["Date"] >= "2022-01-01"]


# 원화 환율 (예시로 1달러당 1300원 가정)
exchange_rate = 1300

# 각 컬럼을 원화로 계산하여 추가
df['High(won)'] = df['High'] * exchange_rate
df['Low(won)'] = df['Low'] * exchange_rate
df['Close(won)'] = df['Close'] * exchange_rate

# 2022년 이후 데이터 필터링
df = df[new_df['Date'] >= '2022-01-01']

# 수정된 데이터프레임 출력
print(df)