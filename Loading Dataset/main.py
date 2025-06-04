import pandas as pd

# the pd.read_csv() syntax is how you load the dataset into a DataFrame, so you can work with it.
data_file = pd.read_csv("C:/Users/jusbe/Desktop/pythonProject/first_project/archive/StudentsPerformance.csv")


# the df.head() function shows the first 5 rows in your dataset.
# This will help you understand what is inside your dataset, like column names, values, formats.
print(data_file.head())

# the df.shape function gives the number of rows and columns. This is useful to know how big your dataset is.
print("\nShape:", data_file.shape)

# df.info() functions shows information like the column names, cata types, and missing values in the dataset
# This tells us what we will need to clean or convert before doing machine learning
print("\nInfo:")
print(data_file.info())

# ok this is Here are some more functions (please refer to the pandas docs to learn more)

# See basic statistics for numeric columns (mean, std, min, max, etc.)
print("\nSummary statistics:")
print(data_file.describe())

# Check for missing values in each column
print("\nMissing values per column:")
print(data_file.isnull().sum())

# Show unique values in a categorical column (e.g. gender)
print("\nUnique values in 'gender':")
print(data_file['gender'].value_counts())
