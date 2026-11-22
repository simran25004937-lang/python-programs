Aim:Implementation of NumPy, Pandas and Matplotlib in Python

Code:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. NumPy Operations
arr = np.array([10, 20, 30, 40, 50])

print("NumPy Array:")
print(arr)

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# 2. Pandas Operations
data = {
    'Name': ['Simran', 'Rahul', 'Priya', 'Aman', 'Riya'],
    'Age': [19, 20, 21, 22, 23],
    'Salary': [25000, 30000, 28000, 35000, 40000]
}

df = pd.DataFrame(data)

print("\nPandas DataFrame:")
print(df)

print("\nFirst 3 Records:")
print(df.head(3))

print("\nStatistical Summary:")
print(df.describe())

print("\nAverage Salary:")
print(df['Salary'].mean())

# 3. Matplotlib Visualization

# Bar Chart
plt.bar(df['Name'], df['Salary'])
plt.title("Employee Salary - Bar Chart")
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.show()

# Line Chart
plt.plot(df['Name'], df['Salary'], marker='o')
plt.title("Employee Salary - Line Chart")
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.show()

# Pie Chart
plt.pie(df['Salary'], labels=df['Name'], autopct='%1.1f%%')
plt.title("Employee Salary - Pie Chart")
plt.show()

Output:
NumPy Array:
[10 20 30 40 50]

Sum: 150
Mean: 30.0
Maximum: 50
Minimum: 10

Pandas DataFrame:
     Name  Age  Salary
0  Simran   19   25000
1   Rahul   20   30000
2   Priya   21   28000
3    Aman   22   35000
4    Riya   23   40000

First 3 Records:
     Name  Age  Salary
0  Simran   19   25000
1   Rahul   20   30000
2   Priya   21   28000

Average Salary: 31600.0

Result:Thus, NumPy, Pandas and Matplotlib libraries were successfully implemented in a single Python program.
