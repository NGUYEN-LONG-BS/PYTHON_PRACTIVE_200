# Page 121
# Exercise 1: Read Total profit of all months and show it using a line plot
# Total profit data provided for each month. Generated line plot must include the following properties: –
# X label name = Month Number
# Y label name = Total profit

import pandas as pd
import matplotlib.pyplot as plt
# sales_data=pd.read_csv("company_sales_data.csv")
sales_data=pd.read_csv(r"C:\Users\ADMIN\Desktop\GITHUB\PYTHON_PRACTIVE_200\17.Python Matplotlib Exercise\company_sales_data.csv")
sales_data.head()
# print(sales_data.head())

import numpy as np
monthList=sales_data["month_number"].tolist()
# print(monthList)
profitList=np.arange(17000,25000,1000).tolist()
# print(profitList)
data_List=sales_data["total profit"].tolist()
# print(data_List)

plt.plot(monthList, data_List, linestyle='-')
plt.xlabel("Month Number")
plt.xticks(monthList)
plt.yticks(profitList)
plt.ylabel("Total profit")
plt.title("COMPANY PROFIT PER MONTH")
plt.show()
