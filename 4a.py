import pandas as pd 

# Creating a Pandas Series from a Python list
data = [10, 20, 30, 40, 50] 
series = pd.Series(data) 

print("Pandas Series:")
print(series)

# Convert Series to Python list 
list_data = series.tolist() 
print("Series as Python List:", list_data) 
print("Type of list_data:", type(list_data)) 
