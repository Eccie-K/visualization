import pandas
import matplotlib.pyplot as plt
import pymysql  # connects to the database

connection = pymysql.connect("localhost", "root", "", "modcom_db")
df = pandas.read_sql("SELECT * FROM `TABLE 5`", connection)
print(df)
