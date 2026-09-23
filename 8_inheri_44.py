# Create Employee and Manager classes to display employee/manager details and calculate the manager's annual salary.

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)

    def annual_salary(self):
        return self.salary * 12


manager = Manager(101, "Rahul", 50000, "IT")
manager.display()
print("Annual Salary:", manager.annual_salary())


# Create Vehicle and Car classes to display vehicle details and calculate the car's discounted price.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def display(self):
        super().display()
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)

    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)


car = Car("Toyota", "Fortuner", "Diesel", 4000000)
car.display()
print("Discounted Price:", car.discounted_price(10))


# Create Academic, Sports, and Student classes using multiple inheritance to calculate the student's overall performance.

class Academic:
    def __init__(self, marks):
        self.marks = marks


class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points


class Student(Academic, Sports):
    def __init__(self, marks, sports_points):
        Academic.__init__(self, marks)
        Sports.__init__(self, sports_points)

    def overall_performance(self):
        return self.marks + self.sports_points


student = Student(85, 15)
print("Academic Marks:", student.marks)
print("Sports Points:", student.sports_points)
print("Overall Performance:", student.overall_performance())

## Create PersonalDetails, ProfessionalDetails, and Employee classes using multiple inheritance to display complete employee information.

class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary


class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Designation:", self.designation)
        print("Salary:", self.salary)


employee = Employee("Rahul", 25, 101, "Software Engineer", 50000)
employee.display()


# Create Person, Student, and ResearchStudent classes using multilevel inheritance to display complete details.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.research_topic)
        print("Guide Name:", self.guide_name)


research_student = ResearchStudent(
    "Priya",
    24,
    102,
    "M.Sc Computer Science",
    "Artificial Intelligence",
    "Dr. Sharma"
)

research_student.display()


# Create BankAccount, SavingsAccount, and PremiumSavingsAccount classes using multilevel inheritance to calculate interest and display account details.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_number, balance, interest_rate, benefits):
        super().__init__(account_number, balance, interest_rate)
        self.benefits = benefits

    def display(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        print("Interest Rate:", self.interest_rate, "%")
        print("Interest:", self.calculate_interest())
        print("Benefits:", self.benefits)


account = PremiumSavingsAccount(
    123456,
    100000,
    6,
    "Free ATM transactions and priority banking"
)

account.display()


# Create a Shape base class and derived Circle, Rectangle, and Triangle classes to calculate their respective areas.

import math

class Shape:
    def display_name(self):
        print("Shape:", self.__class__.__name__)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle = Circle(7)
rectangle = Rectangle(10, 5)
triangle = Triangle(8, 6)

circle.display_name()
print("Area:", circle.area())

rectangle.display_name()
print("Area:", rectangle.area())

triangle.display_name()
print("Area:", triangle.area())

## Create Employee as a base class and Manager, Developer, and Tester as derived classes to calculate salaries using different allowances.

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)


class Manager(Employee):
    def calculate_salary(self):
        allowance = self.basic_salary * 0.40
        return self.basic_salary + allowance

    def display(self):
        super().display()
        print("Manager Allowance: 40%")
        print("Total Salary:", self.calculate_salary())


class Developer(Employee):
    def calculate_salary(self):
        allowance = self.basic_salary * 0.30
        return self.basic_salary + allowance

    def display(self):
        super().display()
        print("Developer Allowance: 30%")
        print("Total Salary:", self.calculate_salary())


class Tester(Employee):
    def calculate_salary(self):
        allowance = self.basic_salary * 0.20
        return self.basic_salary + allowance

    def display(self):
        super().display()
        print("Tester Allowance: 20%")
        print("Total Salary:", self.calculate_salary())


manager = Manager(101, "Rahul", 50000)
developer = Developer(102, "Priya", 45000)
tester = Tester(103, "Amit", 40000)

manager.display()
print()

developer.display()
print()

tester.display()


# Create Person as a base class with Student and Faculty derived from it and TeachingAssistant inheriting from both Student and Faculty.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class Faculty(Person):
    def __init__(self, name, age, faculty_id, department):
        super().__init__(name, age)
        self.faculty_id = faculty_id
        self.department = department


class TeachingAssistant(Student, Faculty):
    def __init__(self, name, age, roll_no, course, faculty_id, department):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        self.course = course
        self.faculty_id = faculty_id
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)
        print("Faculty ID:", self.faculty_id)
        print("Department:", self.department)


student = Student("Amit", 21, 101, "Computer Science")
faculty = Faculty("Dr. Sharma", 45, 501, "Computer Science")

teaching_assistant = TeachingAssistant(
    "Rahul",
    24,
    102,
    "MCA",
    502,
    "Computer Science"
)

print("Student Details:")
print(student.name, student.age, student.roll_no, student.course)

print("\nFaculty Details:")
print(faculty.name, faculty.age, faculty.faculty_id, faculty.department)

print("\nTeaching Assistant Details:")
teaching_assistant.display()


# Create Vehicle as a base class with Car and Bike derived from it and SportsCar and ElectricBike further derived from Car and Bike.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def car_info(self):
        print("Fuel Type:", self.fuel_type)


class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def bike_info(self):
        print("Engine:", self.engine_cc, "cc")


class SportsCar(Car):
    def __init__(self, brand, model, fuel_type, top_speed):
        super().__init__(brand, model, fuel_type)
        self.top_speed = top_speed

    def display_sports_car(self):
        self.display()
        self.car_info()
        print("Top Speed:", self.top_speed, "km/h")


class ElectricBike(Bike):
    def __init__(self, brand, model, engine_cc, battery_capacity):
        super().__init__(brand, model, engine_cc)
        self.battery_capacity = battery_capacity

    def display_electric_bike(self):
        self.display()
        self.bike_info()
        print("Battery Capacity:", self.battery_capacity, "kWh")


sports_car = SportsCar("Ferrari", "488", "Petrol", 340)
electric_bike = ElectricBike("Revolt", "RV400", 5, 4.5)

print("Sports Car Details:")
sports_car.display_sports_car()

print("\nElectric Bike Details:")
electric_bike.display_electric_bike()


# Create Student as a base class and Result as a derived class to calculate total marks, percentage, and grade.

class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course


class Result(Student):
    def __init__(self, roll_no, name, course, marks):
        super().__init__(roll_no, name, course)
        self.marks = marks

    def total_marks(self):
        return sum(self.marks)

    def percentage(self):
        return self.total_marks() / len(self.marks)

    def grade(self):
        percentage = self.percentage()

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

    def display(self):
        print("Roll Number:", self.roll_no)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Marks:", self.marks)
        print("Total Marks:", self.total_marks())
        print("Percentage:", self.percentage())
        print("Grade:", self.grade())


result = Result(
    101,
    "Rahul",
    "BCA",
    [85, 90, 78]
)

result.display()

# Create Product and ElectronicProduct classes to calculate the final price after applying a discount.

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def final_price(self, discount):
        return self.price - (self.price * discount / 100)

    def display(self, discount):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)
        print("Final Price:", self.final_price(discount))


product = ElectronicProduct(101, "Laptop", 60000, "Dell", "2 Years")
product.display(10)


# Create Printer and Scanner classes and a MultifunctionDevice class using multiple inheritance.

class Printer:
    def print_document(self):
        print("Printing document...")


class Scanner:
    def scan_document(self):
        print("Scanning document...")


class MultifunctionDevice(Printer, Scanner):
    def display(self):
        print("Multifunction device supports printing and scanning.")


device = MultifunctionDevice()
device.display()
device.print_document()
device.scan_document()


# Create Camera and Phone classes and a Smartphone class using multiple inheritance.

class Camera:
    def take_photo(self):
        print("Photograph taken.")


class Phone:
    def make_call(self, number):
        print("Calling:", number)


class Smartphone(Camera, Phone):
    def display(self):
        print("Smartphone supports camera and calling features.")


smartphone = Smartphone()
smartphone.display()
smartphone.take_photo()
smartphone.make_call("9876543210")


# Create Person, Student, and ResearchStudent classes using multilevel inheritance.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.research_topic)
        print("Guide Name:", self.guide_name)


research_student = ResearchStudent(
    "Rahul", 24, 101, "MCA",
    "Artificial Intelligence", "Dr. Sharma"
)

research_student.display()


