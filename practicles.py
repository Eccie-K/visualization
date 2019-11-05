import pandas

df = pandas.read_csv('sales.csv', parse_dates=['Date'])
df = df.set_index('Date')
print(df)
print(df).isnull().sum()

newdates = pandas.to_datetime(['2010-02-06', '1/02/19', '1-Jun-2015', '2nd january 2000', 'Feb,12 ,2019',  'Nov 05 23 05:33:26'])

print(newdates)

import matplotlib.pyplot as plt

