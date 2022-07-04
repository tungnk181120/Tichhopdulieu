import pandas as pd

# df1 = pd.read_csv("data_booking_com_1.csv", sep=",", header=0, index_col=None)
# df2 = pd.read_csv("data_booking_com_2.csv", sep=",", header=0, index_col=None)
# df3 = pd.read_csv("data_booking_com_3.csv", sep=",", header=0, index_col=None)
# frames = [df1, df2, df3]

# result = pd.concat(frames)

# result.to_csv('craw_booking_com_full.csv', index=False, encoding='utf8')

df1 = pd.read_csv("craw_booking_com_full.csv",
                  sep=",", header=0, index_col=None)
print(df1.info())
