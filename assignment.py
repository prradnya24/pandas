# Problem statement
#sample data
import pandas as pd
sample_data=[120,150,130,170,160,180,140]
days_of_week=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
# Q1.create a panads series for sales data.
#1.use list of daily sales figures to create a pandas seroies
sales_series=pd.Series(sample_data,index=days_of_week)
print("Sales Series:\n",sales_series)

#2.Access days of the week as the index
print("Days of the week:\n",sales_series.index)

#Q2.Access and manipulate sales data.
#1.Access sales data for specific days using index labels
print("Sales on Wed:",sales_series['Wed'])
print("Sales on Fri:",sales_series['Fri'])

#2.calculate total sales for the week
total_sales=sales_series.sum()
print("Total sales for the week:",total_sales)

#Q.3Basic analysis of sales data
#1.Calculate average sales for the week.
average_sales=sales_series.mean()
print("Average sales for the week:",average_sales)

#2.Determine the days with sales figures significantly different from average
significant_days=sales_series[(sales_series>average_sales*1.1) | (sales_series<average_sales*0.9)]
print("Days with significant sales difference:\n",significant_days)

