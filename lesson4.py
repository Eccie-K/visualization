import pandas
df = pandas.read_csv('power.csv',  parse_dates =['Date'])
df = df.set_index('Date')
print(df)
print(df.isnull().sum())

#dates have different formats
#2010-02-06, 1/02/19, 1-jun-2015, 2nd january 2000, Feb,12 ,09

newdates = pandas.to_datetime(['2010-02-06', '1/02/19', '1-Jun-2015', '2nd january 2000', 'Feb,12 ,2019',  'Nov 05 23 05:33:26'])

print(newdates)


# lets find outPower consumption from 2006 to 2017
import matplotlib.pyplot as plt

df.loc['2010', 'Consumption'].plot()
plt.title('Power usage in 2010')
plt.xlabel('Year 2010')
plt.ylabel('Power consumption')
plt.show()


df.loc['2007 - 2', 'Consumption'].plot()
plt.title('Power usage in February 2007')
plt.xlabel('Year 2010')
plt.ylabel('Power consumption')
plt.show()


df.loc['2010-01-01':'2012-08-01', 'Consumption'].plot()
plt.title('Power usage in 2010 and 2012')
plt.xlabel('Year 2010')
plt.ylabel('Power consumption')
plt.show()

df.loc['2012-01-01':'2014-01-01', ['Consumption', 'Wind', 'Solar']].plot()
plt.title('Power usage in 2008 and 2010')
plt.xlabel('2012-2014')
plt.ylabel('Power consumption')
plt.show()

