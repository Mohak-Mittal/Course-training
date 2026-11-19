import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],
    "Name": [
        "Aarav Sharma", "Ananya Iyer", "Rohan Mehta", "Priya Nair", "Vikram Singh",
        "Sneha Patel", "Aditya Verma", "Neha Gupta", "Karan Malhotra", "Pooja Reddy",
        "Rahul Das", "Divya Joshi", "Manish Rao", "Ritu Kapoor", "Amit Choudhury"
    ],
    "Age": [25, 28, 35, 30, 42, 26, 31, 29, 38, 27, 45, 33, 24, 36, 40],
    "Department": [
        "IT", "HR", "Finance", "Marketing", "IT",
        "Finance", "IT", "HR", "Marketing", "Finance",
        "Management", "IT", "Marketing", "HR", "Finance"
    ],
    "Salary": [
        60000, 52000, 85000, 62000, 120000,
        58000, 75000, 54000, 92000, 61000,
        140000, 78000, 48000, 70000, 98000
    ],
    "Experience": [2, 4, 10, 6, 18, 3, 7, 5, 12, 3, 20, 8, 1, 9, 15],
    "Performance_Score": [88, 92, 85, 90, 95, 78, 89, 84, 91, 80, 96, 87, 75, 93, 89]
}

df = pd.DataFrame(data)

print (df)

print(df.head())

print(df.tail())

print(df.sample(5, random_state=42))

print(df.shape)

print(df.columns.tolist())

df.info()

print(df.describe())

total_rows = df.shape[0]
total_cols = df.shape[1]
numerical_cols = df.select_dtypes(include=["number"]).columns.tolist()
categorical_cols = df.select_dtypes(include=["object", "string"]).columns.tolist()
avg_salary = df["Salary"].mean()
max_salary = df["Salary"].max()
min_salary = df["Salary"].min()
avg_age = df["Age"].mean()
max_exp = df["Experience"].max()
highest_score = df["Performance_Score"].max()

print(f"Total rows?                 : {total_rows}")
print(f"Total columns?              : {total_cols}")
print(f"Numerical columns?          : {numerical_cols}")
print(f"Categorical columns?        : {categorical_cols}")
print(f"Average salary?             : {avg_salary:.2f}")
print(f"Maximum salary?             : {max_salary}")
print(f"Minimum salary?             : {min_salary}")
print(f"Average age?                : {avg_age:.2f} years")
print(f"Maximum experience?         : {max_exp} years")
print(f"Highest performance score?  : {highest_score}")