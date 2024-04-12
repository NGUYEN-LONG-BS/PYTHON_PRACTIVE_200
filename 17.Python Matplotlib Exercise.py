# Page 121
# Exercise 1: Read Total profit of all months and show it using a line plot
# Total profit data provided for each month. Generated line plot must include the following properties: –
# X label name = Month Number
# Y label name = Total profit

import pandas as pd
import matplotlib.pyplot as plt
sales_data=pd.read_csv("company_sales_data.csv")
sales_data.head()