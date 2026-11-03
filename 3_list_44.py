# 1. Create and Display a List of Five Fruits

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print("Fruits:", fruits)


# 2. Display First, Last and Third Element

numbers = [10, 20, 30, 40, 50]

print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Third element:", numbers[2])


# 3. Replace the Third Color

colors = ["Red", "Blue", "Green", "Yellow", "Black"]

colors[2] = "Purple"

print("Updated colors:", colors)


# 4. Add Elements at End, Beginning and Specified Position

numbers = [10, 20, 30, 40]

numbers.append(50)
numbers.insert(0, 5)
numbers.insert(3, 25)

print("Updated list:", numbers)


# 5. Remove First, Last and Specific Student

students = ["Amit", "Rahul", "Sneha", "Priya", "Rohit"]

students.pop(0)
students.pop()
students.remove("Sneha")

print("Remaining students:", students)


# 6. Find Largest and Smallest Without max() and min()

numbers = [25, 10, 45, 5, 30]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)


# 7. Accept 10 Numbers and Calculate Sum and Average

numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)


# 8. Count Even and Odd Numbers

numbers = []

for i in range(15):
    num = int(input("Enter integer: "))
    numbers.append(num)

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)


# 9. Check Whether City Exists in List

cities = ["Kolhapur", "Pune", "Mumbai", "Nashik", "Satara"]

city = input("Enter city name: ")

if city in cities:
    print("City exists in the list.")
else:
    print("City does not exist in the list.")


# 10. Reverse a List Without reverse()

numbers = [10, 20, 30, 40, 50]

reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Original list:", numbers)
print("Reversed list:", reversed_list)


# 11. List Slicing Operations

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("First 5 elements:", numbers[:5])
print("Last 5 elements:", numbers[5:])
print("Middle 4 elements:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse list:", numbers[::-1])


# 12. Display Elements at Even Index Positions

numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print("Elements at even index positions:")

for i in range(0, len(numbers), 2):
    print(numbers[i])


# 13. Sort 10 Numbers in Ascending and Descending Order

numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Ascending order:", ascending)
print("Descending order:", descending)


# 14. Display Only Unique Elements

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Unique elements:", unique)


# 15. Find Second Largest Element

numbers = [10, 50, 30, 80, 40, 80]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

unique.sort()

if len(unique) >= 2:
    print("Second largest element:", unique[-2])
else:
    print("Second largest element does not exist.")


# 16. Nested List for Student Details

students = [
    ["Amit", 101, 85],
    ["Rahul", 102, 90],
    ["Sneha", 103, 88],
    ["Priya", 104, 92]
]

print("Student Details:")

for student in students:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Marks:", student[2])
    print()


# 17. Addition of Two 3 x 3 Matrices

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = []

for i in range(3):
    row = []

    for j in range(3):
        row.append(matrix1[i][j] + matrix2[i][j])

    result.append(row)

print("Matrix Addition:")

for row in result:
    print(row)


# 18. Shopping Cart Operations

cart = []

item = input("Enter item to add: ")
cart.append(item)

item = input("Enter another item to add: ")
cart.append(item)

print("Cart:", cart)

item = input("Enter item to search: ")

if item in cart:
    print("Item found.")
else:
    print("Item not found.")

item = input("Enter item to remove: ")

if item in cart:
    cart.remove(item)
    print("Item removed.")
else:
    print("Item not found.")

print("Final cart:", cart)
print("Total items:", len(cart))


# 19. Student Attendance Management

students = ["Amit", "Rahul", "Sneha", "Priya"]

print("Total students:", len(students))

name = input("Enter student name to search: ")

if name in students:
    print(name, "is present.")
else:
    print(name, "is absent.")

name = input("Enter new student name: ")
students.append(name)

name = input("Enter absent student name to remove: ")

if name in students:
    students.remove(name)
    print("Student removed.")
else:
    print("Student not found.")

print("Final student list:", students)


# 20. Book Management System

books = ["Python", "Java", "C++", "HTML"]

book = input("Enter book to add: ")
books.append(book)

book = input("Enter book to search: ")

if book in books:
    print("Book found.")
else:
    print("Book not found.")

book = input("Enter book to remove: ")

if book in books:
    books.remove(book)
    print("Book removed.")
else:
    print("Book not found.")

print("All books:", books)
print("Total books:", len(books))


# 21. Merge Two Lists

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

merged = list1 + list2

print("First list:", list1)
print("Second list:", list2)
print("Merged list:", merged)


# 22. Find Common Elements Between Two Lists

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = []

for num in list1:
    if num in list2 and num not in common:
        common.append(num)

print("Common elements:", common)


# 23. Count Frequency of Each Element

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency of elements:")

for key, value in frequency.items():
    print(key, ":", value)


# 24. Rotate List Left and Right by One Position

numbers = [1, 2, 3, 4, 5]

left = numbers[1:] + numbers[:1]
right = numbers[-1:] + numbers[:-1]

print("Original list:", numbers)
print("Left rotation:", left)
print("Right rotation:", right)


# 25. Remove Duplicates While Preserving Original Order

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original list:", numbers)
print("List without duplicates:", unique)


# 26. Student Marks Analysis

marks = [
    85, 72, 90, 65, 78,
    92, 55, 88, 76, 95,
    68, 81, 73, 89, 60,
    94, 70, 83, 58, 87
]

highest = marks[0]
lowest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

average = sum(marks) / len(marks)

above_average = 0
below_average = 0

for mark in marks:
    if mark > average:
        above_average += 1
    elif mark < average:
        below_average += 1

print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Students above average:", above_average)
print("Students below average:", below_average)


# 27. Employee Salary Analysis

salaries = [25000, 35000, 55000, 60000, 45000, 75000, 28000, 52000]

highest = salaries[0]
lowest = salaries[0]

for salary in salaries:
    if salary > highest:
        highest = salary

    if salary < lowest:
        lowest = salary

average = sum(salaries) / len(salaries)

above_50000 = 0
below_30000 = 0

for salary in salaries:
    if salary > 50000:
        above_50000 += 1

    if salary < 30000:
        below_30000 += 1

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)
print("Employees earning above Rs. 50,000:", above_50000)
print("Employees earning below Rs. 30,000:", below_30000)


# 28. Batsman Score Analysis

scores = [45, 78, 102, 56, 120, 34, 89, 67, 150, 42]

highest = scores[0]
lowest = scores[0]

for score in scores:
    if score > highest:
        highest = score

    if score < lowest:
        lowest = score

total_runs = sum(scores)
average = total_runs / len(scores)

centuries = 0
half_centuries = 0

for score in scores:
    if score >= 100:
        centuries += 1
    elif score >= 50:
        half_centuries += 1

print("Highest score:", highest)
print("Lowest score:", lowest)
print("Total runs:", total_runs)
print("Average runs:", average)
print("Number of centuries:", centuries)
print("Number of half-centuries:", half_centuries)


# 29. Temperature Analysis for 30 Days

temperatures = [
    28, 30, 32, 29, 31,
    35, 34, 33, 30, 29,
    27, 26, 28, 31, 32,
    36, 37, 35, 34, 33,
    30, 29, 28, 27, 31,
    32, 34, 36, 33, 30
]

hottest = temperatures[0]
coldest = temperatures[0]

for temp in temperatures:
    if temp > hottest:
        hottest = temp

    if temp < coldest:
        coldest = temp

average = sum(temperatures) / len(temperatures)

above_average = 0
below_average = 0

for temp in temperatures:
    if temp > average:
        above_average += 1
    elif temp < average:
        below_average += 1

print("Hottest temperature:", hottest)
print("Coldest temperature:", coldest)
print("Average temperature:", average)
print("Days above average:", above_average)
print("Days below average:", below_average)


# 30. Patient Management System

patient_names = ["Amit", "Rahul", "Sneha"]
patient_ages = [20, 25, 22]

name = input("Enter patient name to add: ")
age = int(input("Enter patient age: "))

patient_names.append(name)
patient_ages.append(age)

print("Patient added.")

name = input("Enter patient name to search: ")

if name in patient_names:
    index = patient_names.index(name)
    print("Patient found.")
    print("Name:", patient_names[index])
    print("Age:", patient_ages[index])
else:
    print("Patient not found.")

name = input("Enter patient name to delete: ")

if name in patient_names:
    index = patient_names.index(name)
    patient_names.pop(index)
    patient_ages.pop(index)
    print("Patient deleted.")
else:
    print("Patient not found.")

print("\nAll Patients:")

for i in range(len(patient_names)):
    print("Name:", patient_names[i], "Age:", patient_ages[i])

print("Total patients:", len(patient_names))