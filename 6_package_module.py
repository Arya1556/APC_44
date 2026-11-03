# MODULE PROGRAMS


# 1. calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Cannot divide by zero"


# main.py

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))


# 2. student.py

def total_marks(marks):
    return sum(marks)

def percentage(marks):
    return sum(marks) / len(marks)

def grade(marks):
    p = percentage(marks)

    if p >= 90:
        return "A+"
    elif p >= 80:
        return "A"
    elif p >= 70:
        return "B"
    elif p >= 60:
        return "C"
    elif p >= 50:
        return "D"
    return "F"


# main.py

marks = [85, 90, 78, 88, 92]

print("Total:", total_marks(marks))
print("Percentage:", percentage(marks))
print("Grade:", grade(marks))


# 3. number_utils.py

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def is_armstrong(n):
    digits = str(n)
    total = sum(int(d) ** len(digits) for d in digits)
    return total == n


def is_perfect(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n


# main.py

n = int(input("Enter number: "))

print("Prime:", is_prime(n))
print("Palindrome:", is_palindrome(n))
print("Armstrong:", is_armstrong(n))
print("Perfect:", is_perfect(n))


# 4. string_utils.py

def count_vowels(text):
    return sum(1 for ch in text.lower() if ch in "aeiou")

def reverse_string(text):
    return text[::-1]

def is_palindrome(text):
    return text == text[::-1]

def count_words(text):
    return len(text.split())

def remove_spaces(text):
    return text.replace(" ", "")


# main.py

text = input("Enter string: ")

print("Vowels:", count_vowels(text))
print("Reverse:", reverse_string(text))
print("Palindrome:", is_palindrome(text))
print("Words:", count_words(text))
print("Without Spaces:", remove_spaces(text))


# 5. salary.py

def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    return basic + hra + da

def deductions(basic):
    return basic * 0.05

def net_salary(basic):
    return gross_salary(basic) - deductions(basic)


# main.py

basic = float(input("Enter basic salary: "))

print("Gross Salary:", gross_salary(basic))
print("Deductions:", deductions(basic))
print("Net Salary:", net_salary(basic))


# 6. recursive.py

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)


def binary(n):
    if n == 0:
        return ""
    return binary(n // 2) + str(n % 2)


# main.py

n = int(input("Enter number: "))

print("Factorial:", factorial(n))
print("Fibonacci:", fibonacci(n))
print("Sum of Digits:", sum_digits(n))
print("Binary:", binary(n))


# PACKAGE PROGRAMS




# mathutils/basic.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


# mathutils/number.py

def prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def armstrong(n):
    digits = str(n)
    return sum(int(d) ** len(digits) for d in digits) == n


def palindrome(n):
    return str(n) == str(n)[::-1]


# mathutils/statistics.py

def mean(numbers):
    return sum(numbers) / len(numbers)

def maximum(numbers):
    return max(numbers)

def minimum(numbers):
    return min(numbers)


# main.py

from mathutils.basic import add
from mathutils.number import prime, armstrong, palindrome
from mathutils.statistics import mean, maximum, minimum

numbers = [10, 20, 30, 40, 50]

print("Addition:", add(10, 20))
print("Prime:", prime(17))
print("Armstrong:", armstrong(153))
print("Palindrome:", palindrome(121))
print("Mean:", mean(numbers))
print("Maximum:", maximum(numbers))
print("Minimum:", minimum(numbers))


# 8. student package



# student/marks.py

def total(marks):
    return sum(marks)

def percentage(marks):
    return sum(marks) / len(marks)


# student/grade.py

def grade(percentage):
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
    return "F"


# student/attendance.py

def eligible(present, total):
    percentage = present / total * 100
    return percentage >= 75


# main.py

from student.marks import total, percentage
from student.grade import grade
from student.attendance import eligible

marks = [80, 85, 90, 75, 88]

p = percentage(marks)

print("Total:", total(marks))
print("Percentage:", p)
print("Grade:", grade(p))
print("Attendance Eligible:", eligible(80, 100))


# 9. banking package

# banking/account.py

class Account:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def display(self):
        print(self.account_no, self.name, self.balance)


# banking/transaction.py

def deposit(balance, amount):
    return balance + amount

def withdrawal(balance, amount):
    if amount <= balance:
        return balance - amount
    return balance


# banking/loan.py

def loan_amount(principal, rate, years):
    interest = principal * rate * years / 100
    return principal + interest


# main.py

from banking.account import Account
from banking.transaction import deposit, withdrawal
from banking.loan import loan_amount

account = Account(101, "Rahul", 10000)

account.balance = deposit(account.balance, 5000)
account.balance = withdrawal(account.balance, 2000)

account.display()

print("Loan Amount:", loan_amount(100000, 8, 2))


# 10. texttools package



# texttools/cleaning.py

import string

def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))

def remove_extra_spaces(text):
    return " ".join(text.split())


# texttools/tokenization.py

def tokenize(text):
    return text.split()


# texttools/frequency.py

def word_frequency(text):
    frequency = {}

    for word in text.split():
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


# main.py

from texttools.cleaning import remove_punctuation, remove_extra_spaces
from texttools.tokenization import tokenize
from texttools.frequency import word_frequency

text = "Python, is easy. Python is powerful."

text = remove_punctuation(text)
text = remove_extra_spaces(text)

print("Cleaned:", text)
print("Tokens:", tokenize(text))
print("Frequency:", word_frequency(text))


# 11. college_project directory



# student/details.py

def student_details():
    print("Student Name: Rahul")
    print("Roll Number: 101")


# student/marks.py

def student_marks():
    print("Marks: 85")


# faculty/details.py

def faculty_details():
    print("Faculty Name: Professor Sharma")
    print("Department: Computer Science")


# main.py

from student.details import student_details
from student.marks import student_marks
from faculty.details import faculty_details

student_details()
student_marks()
faculty_details()


# 12. Library application


# books/book.py

def add_book(book_id, title):
    return {
        "id": book_id,
        "title": title
    }


# members/member.py

def add_member(member_id, name):
    return {
        "id": member_id,
        "name": name
    }


# transactions/transaction.py

def issue_book(book, member):
    print(book["title"], "issued to", member["name"])


# main.py

from books.book import add_book
from members.member import add_member
from transactions.transaction import issue_book

book = add_book(101, "Python Programming")
member = add_member(1, "Rahul")

issue_book(book, member)


# 13. Ecommerce directory


# products/product.py

def product(name, price):
    return {
        "name": name,
        "price": price
    }


# products/category.py

def category(name):
    return name


# customers/customer.py

def customer(name, email):
    return {
        "name": name,
        "email": email
    }


# customers/address.py

def address(city):
    return city


# orders/order.py

def create_order(product, customer):
    return {
        "product": product,
        "customer": customer
    }


# orders/status.py

def order_status():
    return "Order Confirmed"


# payments/payment.py

def payment(amount):
    print("Payment of", amount, "successful.")


# payments/method.py

def payment_method():
    return "UPI"


# main.py

from products.product import product
from customers.customer import customer
from orders.order import create_order
from orders.status import order_status
from payments.payment import payment
from payments.method import payment_method

p = product("Laptop", 50000)
c = customer("Rahul", "rahul@example.com")

order = create_order(p, c)

print(order)
print(order_status())
print("Payment Method:", payment_method())
payment(p["price"])


# 14. Medical project
#
# medical_project/
#     main.py
#     patient/
#         __init__.py
#         patient.py
#     doctor/
#         __init__.py
#         doctor.py
#     billing/
#         __init__.py
#         bill.py
#     records/
#         __init__.py
#         record.py


# patient/patient.py

def patient_details(patient_id, name, age):
    return {
        "id": patient_id,
        "name": name,
        "age": age
    }


# doctor/doctor.py

def doctor_details(doctor_id, name, department):
    return {
        "id": doctor_id,
        "name": name,
        "department": department
    }


# billing/bill.py

def calculate_bill(consultation_fee, medicine_fee):
    return consultation_fee + medicine_fee


# records/record.py

def medical_record(patient_name, disease, treatment):
    return {
        "patient": patient_name,
        "disease": disease,
        "treatment": treatment
    }


# main.py

from patient.patient import patient_details
from doctor.doctor import doctor_details
from billing.bill import calculate_bill
from records.record import medical_record

patient = patient_details(101, "Rahul", 25)

doctor = doctor_details(
    501,
    "Dr. Sharma",
    "Cardiology"
)

record = medical_record(
    patient["name"],
    "Fever",
    "Medicine"
)

bill = calculate_bill(500, 1000)

print("Patient:", patient)
print("Doctor:", doctor)
print("Medical Record:", record)
print("Total Bill:", bill)