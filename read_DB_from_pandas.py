import sqlite3
import pandas as pd
import sqlalchemy
from matplotlib import pyplot as plt

engine = sqlalchemy.create_engine("sqlite:///db.sqlite3")
temp_data = pd.read_sql('SELECT * FROM tempreture_temp WHERE created_date < datetime("now","localtime") AND created_date > datetime("now","localtime", "-30 days")',engine)
print(temp_data)
x=temp_data["created_date"]
y=temp_data["temperture"]
plt.plot(x,y,marker="o")
plt.xticks(rotation=90)
plt.xlabel('x-axis label') # x軸のラベル
plt.subplots_adjust(left=0.1, right=0.95, bottom=0.5, top=0.95)
plt.show()
