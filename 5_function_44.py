"""# 1. Factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

num=int(input("enter a  number"))
print(factorial(num))

#num is even or odd
def evev_odd(n):
    if num%2==0:
        return "even" 
    else:
        return "odd"
num =int(input("enter a number: "))
print(evev_odd(num))

#accepts two numbers and returns the greater number.
def greater(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
num1=int(input("enter a num1: "))
num2=int(input("enter a num2: "))
print(greater(num1,num2))

#⦁	Create a function simple_interest(p, r, t) to calculate simple interest
def simple_interest(p,r,t):
    return (p*r*t)/100
p=int(input("enter p:"))
r=int(input("enter r:"))
t=int(input("enter t:"))
print(simple_interest(p,r,t))


#⦁	Write a function is_prime(n) that returns True if a number is prime; otherwise, returns False.
def prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return 'prime number'
n=int(input("enter a number: "))
print(prime(n))

#⦁	Define a function to calculate the area of a circle using its radius.
def area(rad):
    return 3.14*rad*rad
r=int(input("enter a radius:"))
print(area(r))

#⦁	Write a function that accepts n and returns the sum of the first n natural numbers.
def sum(num):
    result = 0
    for i in range(1, num + 1):
            result = result +i
    return result
num=int(input("enter a number: "))
print(sum(num))

#⦁	Create a function power(base, exponent) to calculate the value of base raised to exponent.
def power(b,e):
    return b**e
b=int(input("enter base: "))
e=int(input("enter a exponent: "))
print(power(b,e))

#Find the largest element
def largest_number(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Largest number:", largest_number(numbers))

#Count vowels in a string

def count_vowels(text):
    count = 0

    for ch in text:
        if ch in "aeiouAEIOU":
            count += 1

    return count

text = input("Enter a string: ")

print("Number of vowels:", count_vowels(text))


#Reverse a string
def reverse_string(text):
    reverse = ""

    for ch in text:
        reverse = ch + reverse

    return reverse


text = input("Enter a string: ")

print("Reverse:", reverse_string(text))


#check pallimdrome
def is_palindrome(value):
    value = str(value)

    reverse = ""

    for ch in value:
        reverse = ch + reverse

    if value == reverse:
        return True
    else:
        return False


value = input("Enter a string or number: ")

if is_palindrome(value):
    print("It is a palindrome")
else:
    print("It is not a palindrome")

#average of list
def count_element(my_list, element):
    count = 0

    for item in my_list:
        if item == element:
            count += 1

    return count

my_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
element = int(input("Enter the element to count: "))

print("Number of occurrences:", count_element(my_list, element))


#count occurence of element
def count_element(my_list, element):
    count = 0

    for item in my_list:
        if item == element:
            count += 1

    return count


my_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
element = int(input("Enter the element to count: "))

print("Number of occurrences:", count_element(my_list, element))


#unique elements
def unique_elements(my_list):
    unique = []

    for item in my_list:
        if item not in unique:
            unique.append(item)

    return unique


my_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Unique elements:", unique_elements(my_list))


# . Create a function to find the second-largest number in a list.

def second_largest(numbers):
    largest = numbers[0]
    second = numbers[0]

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second


numbers = list(map(int, input("Enter numbers: ").split()))
print("Second largest:", second_largest(numbers))


#  Write a function that accepts n and returns the first n Fibonacci numbers.

def fibonacci(n):
    a = 0
    b = 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result


n = int(input("\nEnter n: "))
print("Fibonacci numbers:", fibonacci(n))


# . Create a function that accepts marks in five subjects and returns percentage and grade.

def calculate_grade(marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade


marks = []

for i in range(5):
    mark = float(input("Enter marks for subject " + str(i + 1) + ": "))
    marks.append(mark)

percentage, grade = calculate_grade(marks)

print("Percentage:", percentage, "%")
print("Grade:", grade)


#  Write a function to calculate the electricity bill according to predefined slabs.

def electricity_bill(units):
    if units <= 100:
        bill = units * 1.50
    elif units <= 200:
        bill = (100 * 1.50) + ((units - 100) * 2.50)
    elif units <= 300:
        bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)
    else:
        bill = (100 * 1.50) + (100 * 2.50) + (100 * 4.00)
        bill = bill + ((units - 300) * 5.00)

    return bill


units = float(input("\nEnter electricity units: "))
print("Electricity Bill: Rs.", electricity_bill(units))


# Write a function to calculate gross salary after adding HRA and DA.

def gross_salary(basic_salary):
    hra = basic_salary * 20 / 100
    da = basic_salary * 10 / 100
    gross = basic_salary + hra + da

    return gross


basic_salary = float(input("\nEnter basic salary: "))
print("Gross Salary: Rs.", gross_salary(basic_salary))


# 6. Create a function to calculate total bill after applying a discount.

def total_bill(prices, quantities):
    total = 0

    for i in range(len(prices)):
        total = total + prices[i] * quantities[i]

    if total >= 5000:
        discount = total * 10 / 100
    elif total >= 2000:
        discount = total * 5 / 100
    else:
        discount = 0

    final_bill = total - discount

    return total, discount, final_bill


n = int(input("\nEnter number of items: "))

prices = []
quantities = []

for i in range(n):
    price = float(input("Enter price of item " + str(i + 1) + ": "))
    quantity = int(input("Enter quantity of item " + str(i + 1) + ": "))

    prices.append(price)
    quantities.append(quantity)

total, discount, final_bill = total_bill(prices, quantities)

print("Total:", total)
print("Discount:", discount)
print("Final Bill:", final_bill)


# 7. Write a function to return minimum, maximum, sum, and average of a list.

def number_operations(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    total = 0

    for num in numbers:
        if num < minimum:
            minimum = num

        if num > maximum:
            maximum = num

        total = total + num

    average = total / len(numbers)

    return minimum, maximum, total, average


numbers = list(map(int, input("\nEnter numbers: ").split()))

minimum, maximum, total, average = number_operations(numbers)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Sum:", total)
print("Average:", average)


# 8. Write a program to process student records and calculate total, percentage, grade, class average, highest and lowest scorer.

def calculate_total(marks):
    return sum(marks)


def calculate_percentage(marks):
    return sum(marks) / 5


def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def display_student(student):
    print("\nName:", student["name"])
    print("Roll Number:", student["roll"])
    print("Total:", student["total"])
    print("Percentage:", student["percentage"], "%")
    print("Grade:", student["grade"])


def class_average(students):
    total = 0

    for student in students:
        total = total + student["percentage"]

    return total / len(students)


def highest_scorer(students):
    highest = students[0]

    for student in students:
        if student["percentage"] > highest["percentage"]:
            highest = student

    return highest


def lowest_scorer(students):
    lowest = students[0]

    for student in students:
        if student["percentage"] < lowest["percentage"]:
            lowest = student

    return lowest


students = []

number_of_students = int(input("\nEnter number of students: "))

for i in range(number_of_students):
    print("\nStudent", i + 1)

    name = input("Enter name: ")
    roll = input("Enter roll number: ")

    marks = []

    for j in range(5):
        mark = float(input("Enter marks for subject " + str(j + 1) + ": "))
        marks.append(mark)

    total = calculate_total(marks)
    percentage = calculate_percentage(marks)
    grade = get_grade(percentage)

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)


print("\n========== STUDENT DETAILS ==========")

for student in students:
    display_student(student)

print("\nClass Average:", class_average(students), "%")

highest = highest_scorer(students)
print("\nHighest Scorer:")
display_student(highest)

lowest = lowest_scorer(students)
print("\nLowest Scorer:")
display_student(lowest)


# 9. Create functions for deposit, withdrawal, balance enquiry, and transaction history.

balance = 0
transactions = []


def deposit(amount):
    global balance

    if amount > 0:
        balance = balance + amount
        transactions.append("Deposited Rs. " + str(amount))
        print("Amount deposited successfully.")
    else:
        print("Invalid amount.")


def withdrawal(amount):
    global balance

    if amount <= 0:
        print("Invalid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance = balance - amount
        transactions.append("Withdrawn Rs. " + str(amount))
        print("Amount withdrawn successfully.")


def balance_enquiry():
    print("Current Balance: Rs.", balance)


def transaction_history():
    print("\nTransaction History:")

    if len(transactions) == 0:
        print("No transactions found.")
    else:
        for transaction in transactions:
            print(transaction)


while True:
    print("\n========== BANK MENU ==========")
    print("1. Deposit")
    print("2. Withdrawal")
    print("3. Balance Enquiry")
    print("4. Transaction History")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        deposit(amount)

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        withdrawal(amount)

    elif choice == 3:
        balance_enquiry()

    elif choice == 4:
        transaction_history()

    elif choice == 5:
        print("Thank you for using the bank system.")
        break

    else:
        print("Invalid choice.")


# Create functions to add books, issue books, return books, search books, and display available books using dictionaries.

books = {}


def add_book(book_id, book_name):
    books[book_id] = {"name": book_name, "available": True}
    print("Book added successfully.")


def issue_book(book_id):
    if book_id in books:
        if books[book_id]["available"]:
            books[book_id]["available"] = False
            print("Book issued successfully.")
        else:
            print("Book is already issued.")
    else:
        print("Book not found.")


def return_book(book_id):
    if book_id in books:
        if books[book_id]["available"] == False:
            books[book_id]["available"] = True
            print("Book returned successfully.")
        else:
            print("Book is already available.")
    else:
        print("Book not found.")


def search_book(name):
    found = False

    for book_id in books:
        if name.lower() in books[book_id]["name"].lower():
            print("Book ID:", book_id)
            print("Book Name:", books[book_id]["name"])
            print("Available:", books[book_id]["available"])
            found = True

    if found == False:
        print("Book not found.")


def display_books():
    print("\nAvailable Books:")

    for book_id in books:
        if books[book_id]["available"]:
            print(book_id, "-", books[book_id]["name"])


while True:
    print("\n1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book_id = input("Enter book ID: ")
        book_name = input("Enter book name: ")
        add_book(book_id, book_name)

    elif choice == 2:
        book_id = input("Enter book ID: ")
        issue_book(book_id)

    elif choice == 3:
        book_id = input("Enter book ID: ")
        return_book(book_id)

    elif choice == 4:
        name = input("Enter book name: ")
        search_book(name)

    elif choice == 5:
        display_books()

    elif choice == 6:
        break

    else:
        print("Invalid choice.")


#  Develop a modular program to calculate electricity bills using slabs, fixed charges, taxes, and discounts.

def unit_charge(units):
    if units <= 100:
        return units * 1.50
    elif units <= 200:
        return 100 * 1.50 + (units - 100) * 2.50
    elif units <= 300:
        return 100 * 1.50 + 100 * 2.50 + (units - 200) * 4
    else:
        return 100 * 1.50 + 100 * 2.50 + 100 * 4 + (units - 300) * 5


def fixed_charge():
    return 100


def discount(amount):
    if amount >= 5000:
        return amount * 10 / 100
    elif amount >= 2000:
        return amount * 5 / 100
    else:
        return 0


def tax(amount):
    return amount * 5 / 100


def electricity_bill(units):
    charge = unit_charge(units)
    fixed = fixed_charge()

    subtotal = charge + fixed
    disc = discount(subtotal)
    amount = subtotal - disc
    gst = tax(amount)

    final = amount + gst

    return charge, fixed, disc, gst, final


units = float(input("\nEnter electricity units: "))

charge, fixed, disc, gst, final = electricity_bill(units)

print("Unit Charge:", charge)
print("Fixed Charge:", fixed)
print("Discount:", disc)
print("Tax:", gst)
print("Final Bill:", final)


# Create functions for consultation, laboratory, medicine, room charges, and final bill with patient category discount.

def consultation():
    return 500


def laboratory():
    return 1000


def medicine():
    return 1500


def room(days):
    return days * 2000


def category_discount(category, amount):
    if category.lower() == "senior":
        return amount * 10 / 100
    elif category.lower() == "child":
        return amount * 5 / 100
    else:
        return 0


def hospital_bill(days, category):
    c = consultation()
    l = laboratory()
    m = medicine()
    r = room(days)

    total = c + l + m + r
    disc = category_discount(category, total)
    final = total - disc

    return c, l, m, r, disc, final


days = int(input("\nEnter number of room days: "))
category = input("Enter patient category (senior/child/normal): ")

c, l, m, r, disc, final = hospital_bill(days, category)

print("Consultation Charges:", c)
print("Laboratory Charges:", l)
print("Medicine Charges:", m)
print("Room Charges:", r)
print("Discount:", disc)
print("Final Bill:", final)


#  Implement functions to add/remove products, calculate subtotal, coupon discount, GST, and final invoice.

products = []


def add_product(name, price, quantity):
    products.append([name, price, quantity])


def remove_product(name):
    for product in products:
        if product[0].lower() == name.lower():
            products.remove(product)
            print("Product removed.")
            return

    print("Product not found.")


def subtotal():
    total = 0

    for product in products:
        total = total + product[1] * product[2]

    return total


def coupon_discount(total, coupon):
    if coupon.upper() == "SAVE10":
        return total * 10 / 100
    elif coupon.upper() == "SAVE5":
        return total * 5 / 100
    else:
        return 0


def gst(amount):
    return amount * 18 / 100


def invoice(coupon):
    total = subtotal()
    discount = coupon_discount(total, coupon)
    amount = total - discount
    tax = gst(amount)
    final = amount + tax

    print("\n========== INVOICE ==========")

    for product in products:
        print(product[0], "-", product[1] * product[2])

    print("Subtotal:", total)
    print("Discount:", discount)
    print("GST:", tax)
    print("Final Amount:", final)


while True:
    print("\n1. Add Product")
    print("2. Remove Product")
    print("3. Generate Invoice")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        add_product(name, price, quantity)

    elif choice == 2:
        name = input("Enter product name: ")
        remove_product(name)

    elif choice == 3:
        coupon = input("Enter coupon code: ")
        invoice(coupon)

    elif choice == 4:
        break

    else:
        print("Invalid choice.")


# . Write a recursive function to search for an element in a sorted list using binary search.

def binary_search(numbers, target, low, high):
    if low > high:
        return -1

    middle = (low + high) // 2

    if numbers[middle] == target:
        return middle

    elif target < numbers[middle]:
        return binary_search(numbers, target, low, middle - 1)

    else:
        return binary_search(numbers, target, middle + 1, high)


numbers = list(map(int, input("\nEnter sorted numbers: ").split()))
target = int(input("Enter element to search: "))

result = binary_search(numbers, target, 0, len(numbers) - 1)

if result == -1:
    print("Element not found.")
else:
    print("Element found at index:", result)


# Convert a decimal number into binary using recursion without built-in conversion functions.

def decimal_to_binary(n):
    if n == 0:
        return ""

    return decimal_to_binary(n // 2) + str(n % 2)


number = int(input("\nEnter decimal number: "))

if number == 0:
    print("Binary: 0")
else:
    print("Binary:", decimal_to_binary(number))


#  Check whether a string is a palindrome using recursion.

def is_palindrome(text, start, end):
    if start >= end:
        return True

    if text[start] != text[end]:
        return False

    return is_palindrome(text, start + 1, end - 1)


text = input("\nEnter a string: ")

if is_palindrome(text, 0, len(text) - 1):
    print("Palindrome")
else:
    print("Not a palindrome")


#  Create separate functions for arithmetic operations and pass them as arguments to calculate().

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def calculate(operation, a, b):
    return operation(a, b)


a = float(input("\nEnter first number: "))
b = float(input("Enter second number: "))

print("\n1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Result:", calculate(addition, a, b))

elif choice == 2:
    print("Result:", calculate(subtraction, a, b))

elif choice == 3:
    print("Result:", calculate(multiplication, a, b))

elif choice == 4:
    if b != 0:
        print("Result:", calculate(division, a, b))
    else:
        print("Cannot divide by zero")

else:
    print("Invalid choice.")


# Write a lambda function to calculate the square of a given number.

square = lambda n: n * n

n = int(input("Enter a number: "))
print("Square:", square(n))


# Create a lambda function that returns the cube of a number.

cube = lambda n: n * n * n

n = int(input("\nEnter a number: "))
print("Cube:", cube(n))


# Write a lambda function that returns True if a number is even and False otherwise.

even = lambda n: n % 2 == 0

n = int(input("\nEnter a number: "))
print("Even:", even(n))


# Use a lambda function to find the maximum of two numbers.

maximum = lambda a, b: a if a > b else b

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

print("Maximum:", maximum(a, b))


#  Create a lambda function to calculate simple interest using principal, rate, and time.

simple_interest = lambda p, r, t: (p * r * t) / 100

p = float(input("\nEnter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print("Simple Interest:", simple_interest(p, r, t))


# Use map() and lambda to generate a list containing squares.

numbers = list(map(int, input("\nEnter numbers: ").split()))

squares = list(map(lambda n: n * n, numbers))

print("Squares:", squares)


#. Use map() with lambda to calculate the cube of every element in a list.

numbers = list(map(int, input("\nEnter numbers: ").split()))

cubes = list(map(lambda n: n * n * n, numbers))

print("Cubes:", cubes)


# Use map() and lambda to create a list containing the sum of corresponding elements.

list1 = list(map(int, input("\nEnter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

result = list(map(lambda a, b: a + b, list1, list2))

print("Sum of corresponding elements:", result)


# . Use filter() and lambda to extract all even numbers.

numbers = list(map(int, input("\nEnter integers: ").split()))

even_numbers = list(filter(lambda n: n % 2 == 0, numbers))

print("Even numbers:", even_numbers)


#  Use filter() with lambda to identify prime numbers.

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


numbers = list(map(int, input("\nEnter integers: ").split()))

prime_numbers = list(filter(lambda n: is_prime(n), numbers))

print("Prime numbers:", prime_numbers)


# . Use filter() and lambda to extract positive numbers.

numbers = list(map(int, input("\nEnter numbers: ").split()))

positive_numbers = list(filter(lambda n: n > 0, numbers))

print("Positive numbers:", positive_numbers)


#  Use filter() and lambda to find numbers greater than 50.

numbers = list(map(int, input("\nEnter numbers: ").split()))

greater_numbers = list(filter(lambda n: n > 50, numbers))

print("Numbers greater than 50:", greater_numbers)


#. Use filter() and lambda to find words having more than five characters.

words = input("\nEnter words separated by spaces: ").split()

long_words = list(filter(lambda word: len(word) > 5, words))

print("Words having more than five characters:", long_words)


#  Sort a list of words according to their length using lambda.

words = input("\nEnter words separated by spaces: ").split()

sorted_words = sorted(words, key=lambda word: len(word))

print("Words sorted by length:", sorted_words)


# . Sort students according to their marks using lambda.

students = []

n = int(input("\nEnter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students.append((name, marks))

students = sorted(students, key=lambda student: student[1])

print("Students sorted by marks:")

for student in students:
    print(student[0], "-", student[1])


# Sort employee records according to salary using lambda.

employees = []

n = int(input("\nEnter number of employees: "))

for i in range(n):
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))
    employees.append((name, salary))

employees = sorted(employees, key=lambda employee: employee[1])

print("Employees sorted by salary:")

for employee in employees:
    print(employee[0], "-", employee[1])


#  Use functions and lambda expressions to calculate average, filter students above 75, and sort students by marks.

def calculate_average(students):
    marks = list(map(lambda student: student[1], students))
    return sum(marks) / len(marks)


students = []

n = int(input("\nEnter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students.append((name, marks))

average = calculate_average(students)

above_75 = list(filter(lambda student: student[1] > 75, students))

sorted_students = sorted(students, key=lambda student: student[1])

print("Average marks:", average)

print("Students scoring above 75:")
for student in above_75:
    print(student[0], "-", student[1])

print("Students sorted according to marks:")
for student in sorted_students:
    print(student[0], "-", student[1])


#  Use filter(), map(), and sorted() with lambda for employee records.

employees = []

n = int(input("\nEnter number of employees: "))

for i in range(n):
    name = input("Enter employee name: ")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))

    employees.append((name, department, salary))


# Find employees earning more than 50000
high_salary = list(filter(lambda employee: employee[2] > 50000, employees))

print("Employees earning more than 50000:")
for employee in high_salary:
    print(employee[0], employee[1], employee[2])


# Increase salaries by 10%
increased_salary = list(
    map(lambda employee: (employee[0], employee[1], employee[2] * 1.10), employees)
)

print("\nSalaries after 10% increase:")
for employee in increased_salary:
    print(employee[0], employee[1], employee[2])


# Sort employees according to salary
sorted_employees = sorted(employees, key=lambda employee: employee[2])

print("\nEmployees sorted by salary:")
for employee in sorted_employees:
    print(employee[0], employee[1], employee[2])


#  Use functions and lambda expressions to calculate product value, filter products above 1000, and sort by total value.

products = []

n = int(input("\nEnter number of products: "))

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    products.append((name, price, quantity))


# Calculate total value of each product
product_values = list(
    map(lambda product: (product[0], product[1] * product[2]), products)
)

print("Total value of each product:")
for product in product_values:
    print(product[0], "-", product[1])


# Filter products costing more than 1000
expensive_products = list(
    filter(lambda product: product[1] > 1000, product_values)
)

print("\nProducts costing more than 1000:")
for product in expensive_products:
    print(product[0], "-", product[1])


# Sort products according to total value
sorted_products = sorted(product_values, key=lambda product: product[1])

print("\nProducts sorted by total value:")
for product in sorted_products:
    print(product[0], "-", product[1])


# Use functions, map(), filter(), and lambda to process a list of words.

words = input("\nEnter words separated by spaces: ").split()


# Find length of every word
word_lengths = list(map(lambda word: len(word), words))

print("Length of every word:", word_lengths)


# Extract words having more than five characters
long_words = list(filter(lambda word: len(word) > 5, words))

print("Words having more than five characters:", long_words)


# Sort words according to their length
sorted_words = sorted(words, key=lambda word: len(word))

print("Words sorted according to length:", sorted_words)
"""