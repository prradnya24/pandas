import numpy as np


marks = np.array([[85, 90, 78],
[88, 92, 80],
[75, 85, 82],
[90, 87, 88]])


print("Marks array:")
print(marks)
# Average marks per student (row-wise)
avg_per_student = np.mean(marks, axis=1)

# # Average marks per subject (column-wise)
avg_per_subject = np.mean(marks, axis=0)
print("Average marks per student:")
print(avg_per_student)
print("Average marks per subject:")
print(avg_per_subject)

import numpy as np
# Celsius temperatures
temp = np.array([25, 30, 35, 40])
# Convert to Fahrenheit
print('temp in celsius:',temp)
fahrenheit = temp * 9/5 + 32
print('temp in fahrenheit:',fahrenheit)



import numpy as np
# Monthly sales data
sales = np.array([1000, 1200, 1500, 1800])
print('sales data:',sales)
# (current - previous) / previous * 100
growth = (sales[1:] - sales[:-1]) / sales[:-1] * 100
print('percentage growth:',growth)



import numpy as np
# Raw sensor data
data = np.array([100, 300, 500, 700, 900])
print('raw data:',data)
# Normalize data using universal functions
normalized = (data - np.min(data)) / (np.max(data) - np.min(data))
print('Normalized data',normalized)

import numpy as np

# Example EEG signal data
eeg = np.array([0.1, 0.25, 0.05, 0.8, 0.3, 0.18, 0.5])

# Apply threshold filter: set values below 0.2 to 0
eeg[eeg < 0.2] = 0

print("Filtered EEG signal (Boolean Indexing):")
print(eeg)

import numpy as np

eeg = np.array([0.1, 0.25, 0.05, 0.8, 0.3, 0.18, 0.5])
filtered = np.where(eeg < 0.2, 0, eeg)
print("Filtered EEG signal (np.where):")
print(filtered)


