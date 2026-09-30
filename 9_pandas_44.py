# 1. Create a dictionary containing information for 5 students, convert it into a Pandas DataFrame, calculate total and average marks, and display students who scored more than 75% average.
import pandas as pd

data = {
    "Student ID": [101, 102, 103, 104, 105],
    "Student Name": ["Amit", "Rahul", "Sneha", "Priya", "Rohit"],
    "Python Marks": [85, 72, 90, 65, 80],
    "DBMS Marks": [78, 68, 88, 70, 82],
    "Mathematics Marks": [92, 75, 85, 60, 78]
}

df = pd.DataFrame(data)

df["Total Marks"] = df["Python Marks"] + df["DBMS Marks"] + df["Mathematics Marks"]

df["Average Marks"] = df["Total Marks"] / 3

print("DataFrame:")
print(df)

print("\nStudents with more than 75% average:")
print(df[df["Average Marks"] > 75])

# 2. Create an employee dictionary, convert it into a Pandas DataFrame, and display employees with salary greater than 50000, average salary, highest salary, and employee with highest experience.
import pandas as pd

data = {
    "Employee ID": [101, 102, 103, 104, 105],
    "Employee Name": ["Amit", "Rahul", "Sneha", "Priya", "Rohit"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales"],
    "Salary": [55000, 48000, 65000, 72000, 45000],
    "Experience": [3, 5, 7, 4, 9]
}

df = pd.DataFrame(data)

print("Employee DataFrame:")
print(df)

print("\nEmployees with salary greater than ₹50,000:")
print(df[df["Salary"] > 50000])

print("\nAverage Salary:", df["Salary"].mean())

print("\nHighest Salary:", df["Salary"].max())

print("\nEmployee with Highest Experience:")
print(df.loc[df["Experience"].idxmax()])

# 3. Create a product dictionary, convert it into a Pandas DataFrame, calculate total amount using Price multiplied by Quantity, and find the product having the highest total sales.
import pandas as pd

data = {
    "Product ID": [101, 102, 103, 104, 105],
    "Product Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Electronics"],
    "Price": [50000, 800, 1500, 12000, 15000],
    "Quantity": [5, 20, 15, 8, 6]
}

df = pd.DataFrame(data)

df["Total Amount"] = df["Price"] * df["Quantity"]

print("Product DataFrame:")
print(df)

print("\nProduct with Highest Total Sales:")
print(df.loc[df["Total Amount"].idxmax()])

# 4. Create a patient dictionary, convert it into a Pandas DataFrame, and display patients above 60 years, average medical charge, maximum medical charge, and patients with charges greater than 50000.
import pandas as pd

data = {
    "Patient ID": [101, 102, 103, 104, 105],
    "Patient Name": ["Amit", "Rahul", "Sneha", "Priya", "Rohit"],
    "Age": [65, 45, 72, 58, 67],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Asthma", "Blood Pressure"],
    "Medical Charges": [55000, 25000, 85000, 40000, 65000]
}

df = pd.DataFrame(data)

print("Patient DataFrame:")
print(df)

print("\nPatients above 60 years:")
print(df[df["Age"] > 60])

print("\nAverage Medical Charge:", df["Medical Charges"].mean())

print("\nMaximum Medical Charge:", df["Medical Charges"].max())

print("\nPatients with Medical Charges greater than ₹50,000:")
print(df[df["Medical Charges"] > 50000])

# 5. Create an order dictionary, convert it into a Pandas DataFrame, calculate the final amount, and display all orders, orders above 5000, highest-value order, and average order value.
import pandas as pd

data = {
    "Order_ID": [101, 102, 103, 104, 105],
    "Customer": ["Amit", "Rahul", "Sneha", "Priya", "Rohit"],
    "Product": ["Laptop", "Mobile", "Keyboard", "Monitor", "Printer"],
    "Quantity": [2, 3, 5, 2, 4],
    "Price": [50000, 25000, 1500, 12000, 15000],
    "Discount": [5000, 3000, 500, 1000, 2000]
}

df = pd.DataFrame(data)

df["Final Amount"] = (df["Quantity"] * df["Price"]) - df["Discount"]

print("All Orders:")
print(df)

print("\nOrders above ₹5,000:")
print(df[df["Final Amount"] > 5000])

print("\nHighest-Value Order:")
print(df.loc[df["Final Amount"].idxmax()])

print("\nAverage Order Value:", df["Final Amount"].mean())

# 6. Create a student attendance dictionary, convert it into a Pandas DataFrame, calculate attendance percentage, and display students whose attendance is below 75%.
import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Rohit"],
    "Department": ["CSE", "IT", "CSE", "ENTC", "IT"],
    "Total_Classes": [100, 100, 120, 90, 110],
    "Classes_Attended": [85, 70, 90, 60, 80]
}

df = pd.DataFrame(data)

df["Attendance Percentage"] = (df["Classes_Attended"] / df["Total_Classes"]) * 100

print("Student Attendance DataFrame:")
print(df)

print("\nStudents with attendance below 75%:")
print(df[df["Attendance Percentage"] < 75])

# 7. Create a retail sales dictionary, convert it into a Pandas DataFrame, calculate total sales, display products with sales greater than 10000, find maximum sales, and calculate average sales.
import pandas as pd

data = {
    "Product_ID": [101, 102, 103, 104, 105],
    "Product_Name": ["Laptop", "Mobile", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Electronics"],
    "Price": [50000, 25000, 1500, 12000, 15000],
    "Quantity": [2, 3, 10, 2, 4]
}

df = pd.DataFrame(data)

df["Total_Sales"] = df["Price"] * df["Quantity"]

print("Sales DataFrame:")
print(df)

print("\nProducts with sales greater than ₹10,000:")
print(df[df["Total_Sales"] > 10000])

print("\nProduct with Maximum Sales:")
print(df.loc[df["Total_Sales"].idxmax()])

print("\nAverage Sales:", df["Total_Sales"].mean())

# 7. Create a Pandas Series using a dictionary containing student names and marks, and perform various operations on the Series.
import pandas as pd

marks = {
    "Amit": 85,
    "Rahul": 72,
    "Sneha": 90,
    "Priya": 68,
    "Rohit": 78
}

series = pd.Series(marks)

print("Student Marks Series:")
print(series)

print("\nMarks of Sneha:", series["Sneha"])

print("\nMaximum Marks:", series.max())

print("Minimum Marks:", series.min())

print("Average Marks:", series.mean())

print("\nStudents who scored more than 75:")
print(series[series > 75])

# 8. Create a Pandas Series using a dictionary containing employee names and salaries, and find the highest, lowest, average, and employees earning more than 50000.
import pandas as pd

salary = {
    "Amit": 55000,
    "Rahul": 48000,
    "Sneha": 65000,
    "Priya": 45000,
    "Rohit": 72000
}

series = pd.Series(salary)

print("Employee Salary Series:")
print(series)

print("\nHighest Salary:", series.max())

print("Lowest Salary:", series.min())

print("Average Salary:", series.mean())

print("\nEmployees earning more than ₹50,000:")
print(series[series > 50000])

# 9. Create a Pandas Series using a dictionary containing product names and prices, increase every price by 10%, find the most expensive product, and display products costing more than 1000.
import pandas as pd

prices = {
    "Laptop": 50000,
    "Mobile": 25000,
    "Keyboard": 1500,
    "Mouse": 800,
    "Printer": 12000
}

series = pd.Series(prices)

print("Products and Prices:")
print(series)

series = series * 1.10

print("\nPrices after 10% increase:")
print(series)

print("\nMost Expensive Product:")
print(series.idxmax(), ":", series.max())

print("\nProducts costing more than ₹1,000:")
print(series[series > 1000])

# 10. Create a Pandas Series using a dictionary where patient IDs are the index and patient ages are the values, and find the average, oldest, youngest, and patients above 60 years.
import pandas as pd

ages = {
    101: 65,
    102: 45,
    103: 72,
    104: 58,
    105: 67
}

series = pd.Series(ages)

print("Patient Ages:")
print(series)

print("\nAverage Age:", series.mean())

print("\nOldest Patient:")
print("Patient ID:", series.idxmax(), "Age:", series.max())

print("\nYoungest Patient:")
print("Patient ID:", series.idxmin(), "Age:", series.min())

print("\nPatients above 60 years:")
print(series[series > 60])

# 11. Create a Pandas Series using a dictionary where patient IDs are the index and patient ages are the values, and find the average, oldest, youngest, and patients above 60 years.
import pandas as pd

ages = {
    101: 65,
    102: 45,
    103: 72,
    104: 58,
    105: 67
}

series = pd.Series(ages)

print("Patient Ages:")
print(series)

print("\nAverage Age:", series.mean())

print("\nOldest Patient:")
print("Patient ID:", series.idxmax(), "Age:", series.max())

print("\nYoungest Patient:")
print("Patient ID:", series.idxmin(), "Age:", series.min())

print("\nPatients above 60 years:")
print(series[series > 60])

# 12 . Create a Pandas Series using a dictionary containing student names and attendance percentages, and find average, below 75%, above 90%, and highest attendance.
import pandas as pd

attendance = {
    "Amit": 85,
    "Rahul": 72,
    "Sneha": 95,
    "Priya": 68,
    "Rohit": 92
}

series = pd.Series(attendance)

print("Student Attendance:")
print(series)

print("\nAverage Attendance:", series.mean())

print("\nStudents with attendance below 75%:")
print(series[series < 75])

print("\nStudents with attendance above 90%:")
print(series[series > 90])

print("\nHighest Attendance:")
print(series.idxmax(), ":", series.max(), "%")

# 13. Read students.csv and display first 5 records, last 5 records, total and average marks, students with average above 75, highest average student, and subject-wise average marks.
import pandas as pd

df = pd.read_csv("students.csv")

print("First 5 records:")
print(df.head())

print("\nLast 5 records:")
print(df.tail())

df["Total"] = df[["Python", "DBMS", "Maths"]].sum(axis=1)
df["Average"] = df[["Python", "DBMS", "Maths"]].mean(axis=1)

print("\nTotal and Average Marks:")
print(df[["Student_ID", "Name", "Total", "Average"]])

print("\nStudents with average marks greater than 75:")
print(df[df["Average"] > 75])

print("\nStudent with highest average:")
print(df.loc[df["Average"].idxmax()])

print("\nAverage marks for each subject:")
print(df[["Python", "DBMS", "Maths"]].mean())


# 14. Read employees.csv and display CSE employees, average salary, highest and lowest salary, employees with salary above 50000, and department-wise average salary.
import pandas as pd

df = pd.read_csv("employees.csv")

print("Employees from CSE department:")
print(df[df["Department"] == "CSE"])

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nLowest Salary:")
print(df["Salary"].min())

print("\nEmployees having salary greater than ₹50,000:")
print(df[df["Salary"] > 50000])

print("\nDepartment-wise Average Salary:")
print(df.groupby("Department")["Salary"].mean())


# 15. Read patients.csv and display patients above 60 years, average medical expense, patient with highest expense, disease-wise patient count, and patients with expense above 50000.
import pandas as pd

df = pd.read_csv("patients.csv")

print("Patients above 60 years:")
print(df[df["Age"] > 60])

print("\nAverage Medical Expense:")
print(df["Medical_Expense"].mean())

print("\nPatient with highest medical expense:")
print(df.loc[df["Medical_Expense"].idxmax()])

print("\nPatient count for each disease:")
print(df["Disease"].value_counts())

print("\nPatients whose medical expense exceeds ₹50,000:")
print(df[df["Medical_Expense"] > 50000])


# 16. Read weather.csv and find maximum temperature, minimum temperature, average temperature, records above 35°C, and city-wise average temperature.
import pandas as pd

df = pd.read_csv("weather.csv")

print("Maximum Temperature:")
print(df["Temperature"].max())

print("\nMinimum Temperature:")
print(df["Temperature"].min())

print("\nAverage Temperature:")
print(df["Temperature"].mean())

print("\nRecords where temperature is above 35°C:")
print(df[df["Temperature"] > 35])

print("\nCity-wise Average Temperature:")
print(df.groupby("City")["Temperature"].mean())