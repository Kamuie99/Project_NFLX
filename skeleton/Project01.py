# 패키지 import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 경로
csv_path = '../archive/NFLX.csv'

# csv 파일 읽어오기 (이때, 'Date', 'Open', 'High', 'Low', 'Close' 필드만 읽어오도록 구성)
df = pd.read_csv(csv_path, usecols=range(0, 5))

# DataFrame 출력
print(df)