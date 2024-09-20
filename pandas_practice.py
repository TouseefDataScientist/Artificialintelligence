import  pandas as pd
file = pd.read_excel("practice_dataset.xlsx")
print(file)

# File head
print(file.head(10))


# Generating File_info

print(file.info())

# Generating file columns

print(file.columns)

# Generate Tails
print(file.tail(10))

# describe the dataset
print(file.describe())

# slicing the dataset



# Slice rows based on a condition in a column
#  slicing with a condition
sliced_data_condition = file[file['Salary'] > 50000]  
print(sliced_data_condition)


# Select rows where the value in 'Age' column matches the first value in 'Age' column
sliced_data = file.loc[file['Age'] == 43]
print(sliced_data)

