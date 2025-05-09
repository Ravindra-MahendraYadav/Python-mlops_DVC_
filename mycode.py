import pandas as pd

# Step 1: Create a dictionary with data
data = {
    'ID': [101, 102, 103],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Salary': [70000, 85000, 90000]
}

# Step 2: Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Step 3: Save the DataFrame to a CSV file in the same directory
df.to_csv('employee_data.csv', index=False)

print("CSV file 'employee_data.csv' has been created successfully.")
