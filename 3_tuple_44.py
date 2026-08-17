# 1. Create and Display a Tuple of Five Integers

numbers = (10, 20, 30, 40, 50)
print("Tuple:", numbers)


# 2. Display First, Last and Third City

cities = ("Pune", "Mumbai", "Kolhapur", "Nashik", "Satara")

print("First city:", cities[0])
print("Last city:", cities[-1])
print("Third city:", cities[2])


# 3. Display Total Number of Students

students = ("Amit", "Rahul", "Sneha", "Priya", "Rohit")

print("Total students:", len(students))


# 4. Check Whether Color Exists in Tuple

colors = ("Red", "Blue", "Green", "Yellow", "Black")

color = input("Enter color to search: ")

if color in colors:
    print("Color exists in the tuple.")
else:
    print("Color does not exist in the tuple.")


# 5. Display Each Fruit Using a Loop

fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")

for fruit in fruits:
    print(fruit)


# 6. Count Occurrences of a Number

numbers = (10, 20, 10, 30, 10, 40, 20, 10)

num = int(input("Enter number: "))

print("Number of occurrences:", numbers.count(num))


# 7. Find Index of Employee ID

employee_ids = (101, 102, 103, 104, 105)

id = int(input("Enter employee ID: "))

if id in employee_ids:
    print("Index:", employee_ids.index(id))
else:
    print("Employee ID not found.")


# 8. Concatenate Two Tuples

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

result = tuple1 + tuple2

print("First tuple:", tuple1)
print("Second tuple:", tuple2)
print("Concatenated tuple:", result)


# 9. Repeat a Tuple Four Times

numbers = (1, 2, 3)

result = numbers * 4

print("Repeated tuple:", result)


# 10. Tuple Slicing Operations

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("First five elements:", numbers[:5])
print("Last five elements:", numbers[5:])
print("Middle four elements:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse tuple:", numbers[::-1])


# 11. Convert Tuple into List and Add Element

numbers = (10, 20, 30, 40, 50)

numbers_list = list(numbers)
numbers_list.append(60)

numbers = tuple(numbers_list)

print("Updated tuple:", numbers)


# 12. Accept Five Numbers and Convert List into Tuple

numbers = []

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)

numbers = tuple(numbers)

print("Tuple:", numbers)


# 13. Modify Tuple Using List

numbers = (10, 20, 30, 40, 50)

numbers_list = list(numbers)

numbers_list[2] = 100

numbers = tuple(numbers_list)

print("Modified tuple:", numbers)


# 14. Delete a Tuple Completely

numbers = (10, 20, 30, 40, 50)

print("Tuple before deletion:", numbers)

del numbers

print("Tuple deleted successfully.")


# 15. Nested Tuple of Student Details

students = (
    ("Amit", 101, 85),
    ("Rahul", 102, 90),
    ("Sneha", 103, 88),
    ("Priya", 104, 92)
)

for student in students:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Marks:", student[2])
    print()


# 16. Calculate Sum of Ten Numbers

numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

total = sum(numbers)

print("Sum:", total)


# 17. Find Largest and Smallest Without max() and min()

numbers = (25, 10, 45, 5, 30)

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)


# 18. Calculate Average of Tuple Elements

numbers = (10, 20, 30, 40, 50)

total = sum(numbers)
average = total / len(numbers)

print("Average:", average)


# 19. Count Even and Odd Numbers

numbers = (
    10, 15, 20, 25, 30,
    35, 40, 45, 50, 55,
    60, 65, 70, 75, 80
)

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)


# 20. Check Whether Number Exists in Tuple

numbers = (10, 20, 30, 40, 50)

num = int(input("Enter number to search: "))

if num in numbers:
    print("Number exists in the tuple.")
else:
    print("Number does not exist in the tuple.")


# 21. Display Student Details

student = (101, "Amit", "CSE", 85)

print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])


# 22. Display Employee Information

employees = (
    (101, "Amit", 45000),
    (102, "Rahul", 55000),
    (103, "Sneha", 60000),
    (104, "Priya", 50000)
)

for employee in employees:
    print("Employee ID:", employee[0])
    print("Name:", employee[1])
    print("Salary:", employee[2])
    print()


# 23. Item Price Analysis

prices = (100, 250, 150, 500, 300)

total_bill = sum(prices)
average_price = total_bill / len(prices)

highest = prices[0]
lowest = prices[0]

for price in prices:
    if price > highest:
        highest = price

    if price < lowest:
        lowest = price

print("Total bill:", total_bill)
print("Average price:", average_price)
print("Highest price:", highest)
print("Lowest price:", lowest)


# 24. Temperature Analysis

temperatures = (28, 32, 30, 35, 31, 29, 33)

maximum = temperatures[0]
minimum = temperatures[0]

for temp in temperatures:
    if temp > maximum:
        maximum = temp

    if temp < minimum:
        minimum = temp

average = sum(temperatures) / len(temperatures)

print("Maximum temperature:", maximum)
print("Minimum temperature:", minimum)
print("Average temperature:", average)


# 25. Runs Scored in 10 Matches

runs = (45, 78, 102, 56, 120, 34, 89, 67, 150, 42)

total_runs = sum(runs)

highest = runs[0]
lowest = runs[0]

for score in runs:
    if score > highest:
        highest = score

    if score < lowest:
        lowest = score

average = total_runs / len(runs)

print("Total runs:", total_runs)
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Average score:", average)


# 26. Find Common Elements Between Two Tuples

tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)

common = []

for num in tuple1:
    if num in tuple2 and num not in common:
        common.append(num)

common = tuple(common)

print("Common elements:", common)


# 27. Merge Two Tuples and Remove Duplicates

tuple1 = (10, 20, 30, 40)
tuple2 = (30, 40, 50, 60)

merged = tuple1 + tuple2

unique = []

for num in merged:
    if num not in unique:
        unique.append(num)

result = tuple(unique)

print("Merged tuple:", result)


# 28. Count Frequency of Each Element

numbers = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

for key, value in frequency.items():
    print(key, ":", value)


# 29. Sort Tuple in Ascending and Descending Order

numbers = (50, 20, 40, 10, 30)

ascending = tuple(sorted(numbers))
descending = tuple(sorted(numbers, reverse=True))

print("Ascending order:", ascending)
print("Descending order:", descending)


# 30. Patient Records Management

patients = (
    (101, "Amit", 25, "A+"),
    (102, "Rahul", 30, "B+"),
    (103, "Sneha", 22, "O+"),
    (104, "Priya", 28, "A+")
)

print("All Patient Records:")

for patient in patients:
    print("Patient ID:", patient[0])
    print("Name:", patient[1])
    print("Age:", patient[2])
    print("Blood Group:", patient[3])
    print()

patient_id = int(input("Enter patient ID to search: "))

found = False

for patient in patients:
    if patient[0] == patient_id:
        print("Patient Found")
        print("Patient ID:", patient[0])
        print("Name:", patient[1])
        print("Age:", patient[2])
        print("Blood Group:", patient[3])
        found = True
        break

if not found:
    print("Patient not found.")

print("Total patients:", len(patients))

blood_group = input("Enter blood group to search: ")

print("Patients with", blood_group, "blood group:")

for patient in patients:
    if patient[3] == blood_group:
        print("ID:", patient[0], "Name:", patient[1], "Age:", patient[2])