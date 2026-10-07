# Program to count vowels, consonants, digits, spaces, and special characters in a string
string = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in string:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)




# Program to read a CSV file, handle missing values, and perform basic statistics
import pandas as pd
df = pd.read_csv("students.csv")

print("Original Data:")
print(df)


print("\nMissing Values:")
print(df.isnull().sum())

marks_columns = ["Maths", "Science", "English"]

for col in marks_columns:
    df[col] = df[col].fillna(df[col].mean())

print("\nData after replacing missing marks with mean:")
print(df)

print("\nStatistics:")
print(df[marks_columns].describe())

df["Total"] = df[marks_columns].sum(axis=1)
df["Average"] = df[marks_columns].mean(axis=1)
   
print(df)


# Program to print a pyramid pattern of numbers
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()