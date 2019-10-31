
#How commute 1.Walk, 2. Bike, 3.Car, 4. Public, 5.Other
#Smoking   0 Non Smoker, 2. Past Smoker, 3. Current Smoker
#Math

#Objective: to check math mean score by HowCommute and smoking
# need to fillna and replace as well


import pandas

#task1

df = pandas.read_csv('school.csv')

print(df)

empties = df.isnull().sum()
print(empties)

df['Smoking'].fillna(3, inplace = True)
df['Smoking'].replace({0:'Non smoker', 1:'Past smoker', 2:'Current smoker', 3:'Unknown'}, inplace = True)


df['HowCommute'].fillna(0, inplace=True)
df['HowCommute'].replace({0:'Unknown', 1:'Walk', 2:'Bike', 3:'Public', 4:'Car', 5:'Others'}, inplace = True)

import matplotlib.pyplot as plt

x = df.groupby(['HowCommute', 'Smoking', ])['Math'].mean()

print(x)

df.groupby(['HowCommute', 'Smoking', ])['Math'].mean().unstack().plot(kind = 'bar', stacked = False)

plt.xlabel = ('HowCommute')
plt.ylabel = ('Average math score')
plt.show()
