# Indian Employee Data Cleaning

A data cleaning and preprocessing project using Python, Pandas, and NumPy to prepare an Indian employee dataset for reliable data analysis.

## 📌 Project Overview

This project focuses on cleaning and preprocessing employee data by identifying missing values, handling invalid data, detecting salary outliers, and generating a cleaned dataset.

The goal is to transform raw employee data into a structured and analysis-ready dataset.

## 🎯 Objectives

- Load and inspect the employee dataset
- Identify missing values
- Handle missing numerical values
- Detect and handle invalid salary values
- Identify salary outliers using statistical methods
- Remove extreme salary records
- Export the cleaned dataset for further analysis

## 🗂️ Dataset

The dataset contains employee-related information such as:

- Gender
- Department
- Position
- Salary
- Experience Years
- City
- State
- Education
- Performance Rating
- Joining Date
- Projects Completed
- Overtime Hours

## 🛠️ Technologies Used

- **Python**
- **Pandas** – Data manipulation and preprocessing
- **NumPy** – Numerical operations
- **Git & GitHub** – Version control and project management

## 🔍 Data Cleaning Process

### 1. Dataset Loading

The dataset is loaded into a Pandas DataFrame using `read_csv()`.

### 2. Missing Value Detection

Missing values are identified using:

```python
df.isnull().sum()
