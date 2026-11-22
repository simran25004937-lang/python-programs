import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
data = {
    'Name': ['Simran', 'Rahul', 'Priya', 'Aman', 'Riya'],
    'Age': [19, 20, None, 21, 22],
    'Salary': [25000, 30000, 28000, None, 35000]
}

df = pd.DataFrame(data)

# 1. Load and display data
print("Original Data:")
print(df)

# 2. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 3. Clean the data
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

print("\nCleaned Data:")
print(df)

# 4. Explore the data
print("\nData Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

# 5. Data Visualization

# Bar Chart
plt.bar(df['Name'], df['Salary'])
plt.title("Employee Salary - Bar Chart")
plt.xlabel("Employees")
plt.ylabel("Salary")
plt.show()

# Line Chart
plt.plot(df['Name'], df['Salary'], marker='o')
plt.title("Employee Salary - Line Chart")
plt.xlabel("Employees")
plt.ylabel("Salary")
plt.show()

# Pie Chart
plt.pie(df['Salary'], labels=df['Name'], autopct='%1.1f%%')
plt.title("Employee Salary - Pie Chart")
plt.show()

# Histogram
plt.hist(df['Salary'], bins=5)
plt.title("Salary Distribution - Histogram")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot
plt.scatter(df['Age'], df['Salary'])
plt.title("Age vs Salary - Scatter Plot")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()