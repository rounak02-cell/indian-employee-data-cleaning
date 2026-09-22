# importing necessary libraries 
import pandas as pd
import numpy as np

# loading the dataset
df = pd.read_csv('C:\\Users\\Rounak\\Downloads\\Indian_Employee_Data.csv')
print(df.head())

# checking the missing values
print('Missing value in each column')
print(df.isnull().sum())

# handle inf values before computing any mean/median, or the mean itself becomes inf
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# treat negative salaries as missing before averaging, so they don't skew the mean
df.loc[df['Salary'] < 0, 'Salary'] = np.nan

df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Performance_Rating'] = df['Performance_Rating'].fillna(df['Performance_Rating'].median())

df = df.fillna(df.mean(numeric_only=True))

cat_cols = df.select_dtypes(include='object').columns
df[cat_cols] = df[cat_cols].fillna('Unknown')

# remove duplicate records
df.drop_duplicates(inplace=True)

salary_mean = df['Salary'].mean()
salary_std = df['Salary'].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

# remove rows where salary is too high or too low
df = df[(df['Salary'] >= lower_bound) & (df['Salary'] <= upper_bound)]

df.to_csv('cleaned_indian_employee_Data.csv', index=False)

print('Data cleaning completed! Saved as "cleaned_indian_employee_Data.csv"')