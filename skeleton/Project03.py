# 패키지 import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 경로
csv_path = '../archive/NFLX.csv'

# csv 파일 읽어오기 (이때, 'Date', 'Open', 'High', 'Low', 'Close' 필드만 읽어오도록 구성)
df = pd.read_csv(csv_path, usecols=range(0, 5))

# 2021년 이후 데이터 필터링
df_after_2021 = df[df['Date'] >= '2021-01-01']

# 2021년 이후 데이터에서 가장 높은 종가 변수에 저장
max_price = df_after_2021['Close'].max()

# 2021년 이후 데이터에서 가장 낮은 종가 변수에 저장
min_price = df_after_2021['Close'].min()


print('최고 종가:', max_price)
print('최저 종가:', min_price)

