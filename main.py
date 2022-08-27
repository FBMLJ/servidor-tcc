from unicodedata import name
import pandas as pd
df = pd.read_csv("AEP_hourly.csv", parse_dates=[0])
df.head()

df['hour'] = df['Datetime'].dt.hour
df['day'] = df['Datetime'].dt.day
df['month'] = df['Datetime'].dt.month
df['weekday'] = df['Datetime'].dt.weekday
df['year'] = df['Datetime'].dt.year
df = df.query("year != 2018 and year!=2004")
df['year'].value_counts()


delta =df['AEP_MW'].max()- df['AEP_MW'].min()
df["grupo"] = -10000
for i in range(3):
   df["grupo"] = (df['AEP_MW'] - df['AEP_MW'].min())/(delta/3)

df["grupo"] = df["grupo"].astype(int)


print(df.at["AEP_MW"])
# for i in enumerate(df.iterrows()):
   # print(i)
# print(df.grupo.unique())
# print(df.grupo.min())
# df[['hour','day','month','weekday','year','grupo']].to_csv( "file.csv",index=False )