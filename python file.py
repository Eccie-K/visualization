import pandas
#modcom.co.ke

data_frame = pandas.read_csv('school.csv')
print(data_frame)

empties = data_frame.isnull().sum()
print(empties)
# empties can be ignored or filled using a program

#Reasons for creating plots (visualiation)
# 1.Correlation
# Check rrelationship between two or more variables .. numeric variables
# Find out the relationship between weight and height
# positive corelation: must be > 0 to 1 ,,,,,above 0.5 considered to be strong positive corelation.
# negative corelation: less than 0 to -1,,,,,,above -0.5 is a strong negative corelation
# No corelation is 0(zero)

#Scatter, heatmaps
#fill the missing numeric variables (using the median)

medianH = data_frame['Height'].median()
medianW = data_frame['Weight'].median()

data_frame['Height'].fillna(medianH, inplace=True)
data_frame['Weight'].fillna(medianW, inplace=True)

empties = data_frame.isnull().sum()
print(empties)

import matplotlib.pyplot as plt
figure, ax = plt.subplots()
ax.scatter(data_frame['Height'], data_frame['Weight'], color = 'orange', s=30)
ax.set_title("Relations of Height vs Weight")
ax.set_xlabel("Height")
ax.set_ylabel("Weight")
plt.show()



# Draw a scatter for Math vs Writing


figure, ax = plt.subplots()
ax.scatter(data_frame['Math'], data_frame['Reading'], color = 'blue', s=30)

ax.plot([data_frame['Math'].min(), data_frame['Math'].max()],
        [data_frame['Reading'].min(), data_frame['Reading'].max()], color = 'green')

ax.set_title("Relations of Math vs Reading")
ax.set_xlabel("Math")
ax.set_ylabel("Reading")
plt.show()


#heat maps
# to use heat maps you must install seaborn, to make matplotlibs look better

import seaborn

df = data_frame[['Reading', 'Writing', 'Math', 'English', 'Weight', 'Height', 'SleepTime', 'StudyTime']]
figure, ax = plt.subplots()
seaborn.heatmap(df.corr(), cmap = 'Greens', annot = True)
plt.show()

#Normality - Normal distribution
#Checking distribution of numric variables
# Check if normally distibuted or not

figure, ax = plt.subplots()
ax.hist(df['Math'], color = 'green', label = 'Math', alpha = 0.75)
ax.hist(df['English'], color = 'red', label = 'English', alpha = 0.75)
ax.hist(df['Reading'], color = 'yellow', label = 'Reading', alpha = 0.75)
ax.hist(df['Writing'], color = 'blue', label = 'Writing', alpha = 0.75)
ax.legend(loc = 'best')
ax.set_title('Distribution of Maths')
ax.set_xlabel('subjects')
ax.set_ylabel('Freq')
plt.show()

# pie charts