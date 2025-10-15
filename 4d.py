import pandas as pd
import numpy as np

# Sample dictionary data and labels
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
             'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create the DataFrame
df = pd.DataFrame(exam_data, index=labels)

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Insert a new column 'age' into the DataFrame
df['age'] = [14, 15, 16, 14, 15, 16, 17, 15, 14, 16]

# Display updated DataFrame
print("\nDataFrame after adding new column 'age':")
print(df)
