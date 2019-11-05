import pandas
import matplotlib.pyplot as plt
import pymysql  # connects to the database

connection = pymysql.connect("localhost", "root", "", "modcom_db")
df = pandas.read_sql("SELECT * FROM `TABLE 5`", connection)
print(df)
print(df['Property_Area'])

# generating a pie chart

df['Self_Employed'].fillna('Not Known', inplace=True)
df.groupby('Self_Employed').size().plot(kind = 'pie', autopct = '%1.1f%%',
                                            explode=(0, 0.2, 0))

plt.title("Self employed distribution")
plt.xlabel("")
plt.ylabel("")
plt.show()



# histogram
figure, ax = plt.subplots()
ax.hist(df['ApplicantIncome'], color = 'green', label = 'App.Income', alpha = 0.75)
ax.hist(df['CoapplicantIncome'], color = 'red', label = 'C. inc', alpha = 0.75)

ax.legend(loc = 'best')
ax.set_title('Distribution of Applicant Income')
ax.set_xlabel('Income')
ax.set_ylabel('Freq')
plt.show()


#stacked bar chart


