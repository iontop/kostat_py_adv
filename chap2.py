import pandas as pd

# 다양한 데이터 파일 가져오기 & 저장하기

# 과제 [2-1]
filepath="D:\\Python\\Samples\\kostat_py\\chap2\\"
df1=pd.read_csv(filepath+"df_test.csv")
df2=pd.read_excel(filepath+"df_test.xlsx")
df3=pd.read_json(filepath+"df_test.json")

# print("*** csv ***")
# print(df1)
# print("*** xlsx ***")
# print(df2)
# print("*** json ***")
# print(df3)

# 과제[2-2]
df3.to_csv(filepath+"df_conv.csv")

# 과제[2-3]
writer=pd.ExcelWriter(filepath+"df_excel.xlsx") # D:\Python\Samples\kostat_py\chap2\df_excel.xlsx

df1.to_excel(writer, sheet_name="df1")
df2.to_excel(writer, sheet_name="df2")
df3.to_excel(writer, sheet_name="df3")

writer.save() # write.save()가 없으면 0KB짜리 df_excel.xlsx가 만들어짐

