# 넷플릭스 주가 데이터 분석

## 공통 요구 사항

- 캐글을 활용하여 데이터를 다운로드 받아 활용
- 데이터셋: ‘Netflix Stock Price Prediction(넷플릭스 주식 가격 데이터)’
- 데이터셋 요약: 2018-02-05 ~ 2022-02-04 까지의 일별 데이터
 

[Netflix Stock Price Prediction](https://www.kaggle.com/datasets/jainilcoder/netflix-stock-price-prediction)

## 세부 요구 사항

1. 데이터 전처리 – 데이터 읽어오기
2. 데이터 전처리 – 2021년 이후의 종가 데이터 출력하기
3. 데이터 분석 - 2021년 이후 최고, 최저가 출력하기
4. 데이터 분석 – 2021년 이후 월 별 평균 종가 출력하기
5. 데이터 시각화 – 2022년 1월 이후 월 별 최고, 최저, 종가 시각화

## 프로젝트 소감

1. 파일 경로에서 .을 잘 찍고 ctrl 눌러서 꼭 경로 확인 해보고 쓰자.
2. 파일 읽어오기 `.read_csv` 에서 example 예시가 왜 range(1, 7)인지 어려웠는데 해결
3. `.to_datetime` 메서드를 통해 해당 열 전체를 날짜 형식으로 변환할 수 있는 장점 터득
4. 표 출력 할 때 x 축 눈금과 x축 시작값이 다르다는 것이 어려웠음
5. 해당 x축에 원하는 값을 띄우는 과정에서 구글링을 많이 많이 해봄…
6. `데이터 전처리` 라는 분야에 대해 처음이었는데, Pandas를 사용하여 csv 파일을 활용한 데이터 처리가 상당히 빠르고 편리한 점이 인상깊었음