import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import os

#todo later dynamically let user select csv files

file_path = os.path.join(os.path.dirname(__file__), "data", "sales_data_201904.csv")
dataframe = pd.read_csv(file_path)

total_sales = dataframe['sales price'].sum()

pvt_df = dataframe.pivot_table(index= ['date'], values= ['sales price'],  aggfunc= np.sum)

plt.plot(pvt_df)
plt.show(block=False)
input('press <ENTER> to continue')

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")