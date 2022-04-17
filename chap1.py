import pandas as pd
exam_data={'이름':['철수', '민지', '영미', '한솔'],
        '나이':[12, 21, 18, 26],
        '직업':['중학생', '대학생', '고등학생', '회사원']}

# DataFrame 변환
df=pd.DataFrame(exam_data)
print(df)

# 열이름 변경 - rename, {}안에 바꾸고자 하는 열이름 :  바꿀 열 이름
df.rename(columns={'나이':'연령'}, inplace=True)
print(df)

# 열삭제 - drop, 삭제하고자 하는 열 혹은 행을 List로 입력, axis=0 행, axis=1 열
df.drop(['직업'], axis=1, inplace=True)
print(df)

# DataFrame 특정 데이터 조회 - iloc
df.iloc[1,1]
print(df.iloc[1,1])

# 열선택 -  DataFrame.열이름 혹은 .없이 Dataframe[열이름]
df.이름
print(df.이름)

df['이름']
print(df['이름'])

# 값의 크기로 정렬 - sort_values() 사용, assending=True/False
df.sort_values(by='연령', ascending=False)
print(df.sort_values(by='연령', ascending=False))