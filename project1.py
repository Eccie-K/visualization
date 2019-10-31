# pandas help in acquiring data from a given source
# pandas are used for data cleaning, data preparation
# modcom.co.ke/datascience

import pandas

data = pandas.read_csv('school.csv')
print(data) #shows everything
print(data['Gender'])#shows one column
print(data['State'], ['Math'])
data_x = data[["Rank", "Gender", "Sprint"]]# narrow down your data
print(data_x)

data_y = data[["Height", "Weight", "Smoking"]]
print(data_y)

#checking for empties, none,null
# if missing rows are <5% of the sample size, ignore otherwise proceed

empties = data.isnull().sum()
print(empties)

# imputation: a process of fixing missing values
# replace,,,fillnan,,,,dropnan(methods of fixing missing values)

#dropping empties
#data.dropna(inplace=True) #inplace = True updates data after removing
#print(data)


#plotiing, graphs

import matplotlib.pyplot as plt  #matplotlib is for graphs and must be installed

#objective: to see the perfomance in maths vs english
# bar(horizontal and vertical), pie, histograms,gantt, scatter, stacked/unstacked
# bo plots, density, line-graph


figure, ax = plt.subplots()
ax.scatter(data['Reading'], data['Math'], color = 'orange', s = 30)

ax.set_title('Reading vs Math')
ax.set_xlabel('Reading Score')
ax.set_ylabel('Math Score')
plt.show()







