import pandas

data_frame = pandas.read_csv('school.csv')

print(data_frame)
# pie, bar,stacked/unstacked, line charts

empties = data_frame.isnull().sum()
print(empties)


# numeric/quantitative e.g weight, height, math, age
#categorical e.g countries, counties, towns, product, names, course
#ordinal (follows a specific pattern), good,bad,excellent,average,gender, low,high,medium
#Objective: find the proportion of gender
# 0 - male, 1-female, 2-unknown

data_frame['Gender'].fillna(2, inplace=True)
data_frame['Gender'].replace({0:'Male', 1:'Female', 2:'Unknown'}, inplace = True)

import matplotlib.pyplot as plt

x = data_frame.groupby('Gender').size()
print(x)

#Pie chart

x = data_frame.groupby('Gender').size().plot(kind = 'pie', autopct = '%1.1f%%',
                                            explode = (0,  0,0.2))

plt.title = ('Gender distribution')
plt.xlabel =('')
plt.ylabel = ('')
plt.show()

# pie chart for rank 1. Freshman, Sophomore, Junior, Senior



data_frame['Rank'].fillna(0, inplace=True)
data_frame['Rank'].replace({0:'Freshman', 1:'Sophomore', 2:'Junior', 3:'Senior', 4:'Unknown'}, inplace = True)

y = data_frame.groupby('Rank').size()
print(x)


data_frame.groupby('Rank').size().plot(kind = 'pie', autopct = '%1.1f%%',
                                            explode = (0,  0, 0.2, 0.2, 0.2))


plt.show()


#Bar Chart

# find out maths perfomance by gender
z = data_frame.groupby('Gender')['Weight'].mean()
print(z)

data_frame.groupby('Gender')['Weight'].mean().plot(kind = 'bar', color = 'green')
plt.title = ('Weight Mean by Gender')
plt.xlabel=('Gender')
plt.ylabel= ('Weight')
plt.show()


# stacked bar chart
k = data_frame.groupby(['Gender', 'Rank'])['Weight'].mean().unstack()
print(k)

data_frame.groupby(['Gender', 'Rank'])['Weight'].mean().unstack().plot(kind = 'bar',
                                                                       stacked = False)
plt.title = ("Stacked bar chart to show Gender vs Average Weight")
plt.xlabel = ("Gender")
plt.ylabel = ("Average weight")
plt.show()


#How commute 1.Walk, 2. Bike, 3.Car, 4. Public, 5.Other
#Smoking   0 Non Smoker, 2. Past Smoker, 3. Current Smoker
#Math

#Objective: to check math mean score by HowCommute and smoking
# need to fillna and replace as well




