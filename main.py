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
print(df)
df.to_csv( "file.csv",index=False )