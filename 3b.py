import numpy as np 

# 1D array
arr = np.array([1, 3, 2, 3, 4, 2, 1, 5]) 

print("Max:", np.max(arr))             # Maximum value
print("Min:", np.min(arr))             # Minimum value
print("Argmax:", np.argmax(arr))       # Index of max value
print("Argmin:", np.argmin(arr))       # Index of min value
print("Repr:", repr(arr))              # Official string representation
print("Unique:", np.unique(arr))       # Unique elements
print("Bincount:", np.bincount(arr))   # Counts of each integer value

# Count occurrences of a specific value
count_3 = np.count_nonzero(arr == 3)  
print("Count of 3:", count_3)         

# Filter numbers based on a condition
specified_num = 3
less_than = arr[arr < specified_num]
greater_than = arr[arr > specified_num]
print(f"Numbers less than {specified_num}:", less_than)
print(f"Numbers greater than {specified_num}:", greater_than
