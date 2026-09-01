# Create a dictionary containing student details
student = {
    "roll_number": 44,
    "name": "Arya",
    "department": "Computer Science",
    "marks": 85
}

print("Student Details:")
print(student)

# Create a dictionary containing employee information
employee = {
    "id": 1001,
    "name": "Arya",
    "department": "IT",
    "salary": 50000
}

key = "salary"
print("Value of", key, ":", employee[key])


# Create a dictionary of five products and their prices
products = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Keyboard": 1500,
    "Mouse": 800,
    "Headphones": 2500
}

print("Products before adding:")
print(products)

products["Tablet"] = 15000

print("\nProducts after adding:")
print(products)

# Create a dictionary containing student marks and update the marks 
marks = {
    "Rahul": 85,
    "Amit": 90,
    "Priya": 78,
    "Sneha": 92
}


student = "Amit"

marks[student] = 95 
print("Updated Student Marks:")
print(marks)

# Create a dictionary of cities and their populations
cities = {
    "Mumbai": 20000000,
    "Delhi": 19000000,
    "Pune": 7000000,
    "Bangalore": 12000000
}


city = "Pune"

# Remove the city
del cities[city]

print("Cities after removal:")
print(cities)

# Problem Statement: Create a dictionary of employee IDs and names, ask the user for an employee ID, and check whether it exists.

employees = {
    101: "Rahul",
    102: "Amit",
    103: "Priya",
    104: "Sneha"
}

emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    print("Employee ID exists.")
    print("Employee Name:", employees[emp_id])
else:
    print("Employee ID does not exist.")


# Problem Statement: Create a dictionary containing student records and find the total number of key-value pairs.

students = {
    101: "Rahul",
    102: "Amit",
    103: "Priya",
    104: "Sneha",
    105: "Karan"

}

total = len(students)

print("Total number of key-value pairs:", total)

# Problem Statement: Create a dictionary and display all keys, all values, and all key-value pairs.

data = {
    "Name": "Rahul",
    "Age": 20,
    "Course": "BCA"
}

print("All Keys:", data.keys())
print("All Values:", data.values())
print("All Key-Value Pairs:", data.items())

# Problem Statement: Create a dictionary of programming languages and their creators and display each key and value using a loop.

languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C": "Dennis Ritchie",
    "JavaScript": "Brendan Eich"
}

for language, creator in languages.items():
    print(language, ":", creator)

    
# Problem Statement: Accept five student names and their marks from the user and store them in a dictionary.

students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

print("Student Records:", students)


# Problem Statement: Create a dictionary containing student names and marks and find the student who has scored the highest marks.

students = {
    "Rahul": 85,
    "Amit": 92,
    "Priya": 78,
    "Sneha": 95
}

highest = max(students, key=students.get)

print("Student with highest marks:", highest)
print("Marks:", students[highest])

# Problem Statement: Create a dictionary containing student names and marks and find the student who has scored the lowest marks.

students = {
    "Rahul": 85,
    "Amit": 92,
    "Priya": 78,
    "Sneha": 95
}

lowest = min(students, key=students.get)

print("Student with lowest marks:", lowest)
print("Marks:", students[lowest])


# Problem Statement: Create a dictionary containing student names and marks and calculate the average marks of all students.

students = {
    "Rahul": 85,
    "Amit": 92,
    "Priya": 78,
    "Sneha": 95
}

average = sum(students.values()) / len(students)

print("Average Marks:", average)

# Problem Statement: Accept a string from the user and create a dictionary containing each character and its frequency.

text = input("Enter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print("Character Frequency:", frequency)


# Problem Statement: Accept a sentence and create a dictionary containing each word and the number of times it occurs.

sentence = input("Enter a sentence: ")

words = sentence.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word Frequency:", frequency)


# Problem Statement: Accept a sentence and create a dictionary containing each word and the number of times it occurs.

sentence = input("Enter a sentence: ")

words = sentence.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word Frequency:", frequency)


# Problem Statement: Create two dictionaries and merge them into a single dictionary.

dict1 = {
    "A": 10,
    "B": 20
}

dict2 = {
    "C": 30,
    "D": 40
}

merged = {**dict1, **dict2}

print("Merged Dictionary:", merged)



# Problem Statement: Given two dictionaries, find the keys that are common to both dictionaries.

dict1 = {
    "A": 10,
    "B": 20,
    "C": 30
}

dict2 = {
    "B": 40,
    "C": 50,
    "D": 60
}

common_keys = dict1.keys() & dict2.keys()

print("Common Keys:", common_keys)


# Problem Statement: Given two dictionaries, identify the values that are common to both dictionaries.

dict1 = {
    "A": 10,
    "B": 20,
    "C": 30
}

dict2 = {
    "X": 20,
    "Y": 30,
    "Z": 40
}

common_values = set(dict1.values()) & set(dict2.values())

print("Common Values:", common_values)


# Problem Statement: Create a dictionary containing duplicate values and remove duplicate values while retaining the first corresponding key.

data = {
    "A": 10,
    "B": 20,
    "C": 10,
    "D": 30,
    "E": 20
}

unique_data = {}

for key, value in data.items():
    if value not in unique_data.values():
        unique_data[key] = value

print("Dictionary after removing duplicates:", unique_data)


# Problem Statement: Create a dictionary containing numbers from 1 to 10 as keys and their squares as values.

squares = {}

for num in range(1, 11):
    squares[num] = num ** 2

print(squares)


# Problem Statement: Create a dictionary containing numbers from 1 to 20 as keys and their squares as values, but include only even numbers.

squares = {}

for num in range(1, 21):
    if num % 2 == 0:
        squares[num] = num ** 2

print(squares)

# Problem Statement: Given a list of numbers, create a dictionary containing each unique number and its frequency.

numbers = [1, 2, 3, 2, 4, 1, 2, 5, 3, 1]

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print("Frequency:", frequency)


# Problem Statement: Create a dictionary containing integers from 1 to 10 and their cubes.

cubes = {}

for num in range(1, 11):
    cubes[num] = num ** 3

print(cubes)

# Problem Statement: Create a dictionary containing student names and marks and perform add, update, delete, search, display, highest marks, and average operations.

students = {
    "Rahul": 85,
    "Amit": 92,
    "Priya": 78
}

# Add a student
students["Sneha"] = 95

# Update marks
students["Rahul"] = 90

# Delete a student
del students["Priya"]

# Search for a student
name = "Amit"
if name in students:
    print("Marks of", name, ":", students[name])
else:
    print("Student not found")

# Display all students
print("All Students:")
for name, marks in students.items():
    print(name, ":", marks)

# Find highest marks
print("Highest Marks:", max(students.values()))

# Calculate average
average = sum(students.values()) / len(students)
print("Average Marks:", average)


# Problem Statement: Create a dictionary containing employee names and salaries and find the highest salary, lowest salary, average salary, and employees earning more than ₹50,000.

employees = {
    "Rahul": 45000,
    "Amit": 60000,
    "Priya": 55000,
    "Sneha": 70000,
    "Karan": 40000
}

print("\nHighest Salary:", max(employees.values()))
print("Lowest Salary:", min(employees.values()))

average = sum(employees.values()) / len(employees)
print("Average Salary:", average)

print("Employees earning more than ₹50,000:")
for name, salary in employees.items():
    if salary > 50000:
        print(name, ":", salary)


# Problem Statement: Create a dictionary containing product names and quantities and perform add, update, delete, search, and display products with quantity below 10.

products = {
    "Pen": 20,
    "Notebook": 8,
    "Pencil": 15,
    "Eraser": 5
}

# Add a product
products["Marker"] = 12

# Update quantity
products["Pen"] = 25

# Delete a product
del products["Pencil"]

# Search for a product
product = "Notebook"
if product in products:
    print("\nQuantity of", product, ":", products[product])
else:
    print("Product not found")

# Display products with quantity below 10
print("Products with quantity below 10:")
for product, quantity in products.items():
    if quantity < 10:
        print(product, ":", quantity)


# Problem Statement: Create a dictionary containing names and phone numbers and perform add, search, update, delete, and display operations.

contacts = {
    "Rahul": "9876543210",
    "Amit": "9876501234",
    "Priya": "9123456780"
}

# Add contact
contacts["Sneha"] = "9988776655"

# Search contact
name = "Amit"
if name in contacts:
    print("\nPhone Number:", contacts[name])
else:
    print("Contact not found")

# Update contact
contacts["Rahul"] = "9999999999"

# Delete contact
del contacts["Priya"]

# Display all contacts
print("All Contacts:")
for name, phone in contacts.items():
    print(name, ":", phone)


# Problem Statement: Create a dictionary containing book IDs and book names and perform add, search, remove, display, and count operations.

books = {
    101: "Python Programming",
    102: "Data Structures",
    103: "Computer Networks"
}

# Add a book
books[104] = "Database Management"

# Search a book
book_id = 102
if book_id in books:
    print("\nBook Name:", books[book_id])
else:
    print("Book not found")

# Remove a book
del books[103]

# Display all books
print("All Books:")
for book_id, book_name in books.items():
    print(book_id, ":", book_name)

# Count total books
print("Total Books:", len(books))


# Problem Statement: Take a dictionary containing student names and departments and create a new dictionary that groups students according to their department.

students = {
    "Rahul": "Computer Science",
    "Amit": "Mechanical",
    "Priya": "Computer Science",
    "Sneha": "Electronics",
    "Karan": "Mechanical"
}

groups = {}

for student, department in students.items():
    if department not in groups:
        groups[department] = []
    groups[department].append(student)

print("\nStudents grouped by department:")
print(groups)


#  Problem Statement: Take a list of words and create a dictionary where the key is the word length and the value is a list of words having that length.

words = ["cat", "dog", "apple", "bat", "mango", "sun"]

word_groups = {}

for word in words:
    length = len(word)

    if length not in word_groups:
        word_groups[length] = []

    word_groups[length].append(word)

print("\nWords grouped by length:")
print(word_groups)


#  Problem Statement: Take a list of integers and a target value and find two numbers whose sum is equal to the target using a dictionary.

numbers = [2, 7, 11, 15, 3, 6]
target = 9

seen = {}
found = False

for num in numbers:
    required = target - num

    if required in seen:
        print("\nTwo numbers whose sum is", target, ":", required, "and", num)
        found = True
        break

    seen[num] = True

if not found:
    print("No two numbers found")


#. Problem Statement: Take a string and use a dictionary to find the first character that occurs only once.

text = input("\nEnter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

for char in text:
    if frequency[char] == 1:
        print("First non-repeating character:", char)
        break
else:
    print("No non-repeating character found")


# Problem Statement: Take a string and use a dictionary to find the first character that occurs more than once.

text = input("\nEnter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

for char in text:
    if frequency[char] > 1:
        print("First repeating character:", char)
        break
else:
    print("No repeating character found")


# Problem Statement: Accept a paragraph and create a dictionary where the key is word length and the value is the number of words having that length.

paragraph = input("\nEnter a paragraph: ")

words = paragraph.split()
length_count = {}

for word in words:
    length = len(word)
    length_count[length] = length_count.get(length, 0) + 1

print("Word Length Frequency:")
for length, count in length_count.items():
    print(length, ":", count)


