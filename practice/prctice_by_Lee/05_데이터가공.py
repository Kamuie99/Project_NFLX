# 패키지 import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 경로
csv_path = '../example/archive/google-stock-dataset-Monthly.csv'

# CSV 파일 읽어오기 (첫 번째, 마지막 열 제외)
new_df = pd.read_csv(csv_path, usecols=range(1, 7))

# 2022년 이후 데이터 필터링
df_aftter_2022 = new_df[new_df['Date'] >= '2022-01-01']

# 출력하기
print(df_aftter_2022)