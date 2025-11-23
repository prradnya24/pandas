import pandas as pd

# Create Series from a list
data = [1, 2, 3, 4]
s= pd.Series(data)

# Create Series with custom index
index = ['a', 'b', 'c', 'd']
series_with_index = pd.Series(data, index=index)

# Create Series from a dictionary
data_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
series_from_dict = pd.Series(data_dict)

# Accessing elements
print(s[2])  # Access third element (0-based indexing)
print(series_with_index[2])  # Access by integer position

# Display first and last rows
first_n_rows = s.head(2)
print(first_n_rows)

last_n_rows = s.tail(2)
print(last_n_rows)

# Display dimension (shape)
dimension = s.shape
print(dimension)

# Display statistical summary
stats = s.describe()
print(stats)

# Display unique values
unique_values = s.unique()
print(unique_values)

data=[1,2,3,4,5]
series=pd.Series(data)
print(series)


result_series= series + series_with_index
print(result_series)

sqaured_series=series.apply(lambda x: x**2)
print(sqaured_series)

mapped_series=series.map({1:'one',2:'two',3:'three',4:'four'})
print(mapped_series)

sorted_series=series.sort_values()
print(sorted_series)

missing_values=series.isnull()
print(missing_values)

filled_series=series.fillna(0)
print(filled_series)


data={'a':10,'b':20,'c':30,'d':40}
series=pd.Series(data)
selected_greater_than_30=series[series> 30]
print(selected_greater_than_30)

#select the elements equal to 20
selected_equal_to_20=series[series == 20]
print(selected_equal_to_20)

select_multiple_condtions=series[(series > 10) & (series < 40 )]
print(select_multiple_condtions)

selected_by_list=series[series.isin([10,30])]
print(selected_by_list)

string_series=pd.Series(['apple','banana','cherry','date'])
selected_by_string=string_series[string_series.str.startswith('b')]
print(selected_by_string)


selected_by_index_labels=series.loc[['a','c']]
print(selected_by_index_labels)


selected_by_numeric_positions=series.iloc[1:4]
print(selected_by_numeric_positions)


# sales_data=[120,150,130,170,180,140]


