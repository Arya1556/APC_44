# 1. Create a set containing five integers and display all its elements.
numbers = {10, 20, 30, 40, 50}
print(numbers)

# 2. Create a list with duplicate values, convert it into a set and display the result.
numbers = [10, 20, 10, 30, 20, 40]
result = set(numbers)
print(result)

# 3. Create a set of five fruits, add two new fruits and display the updated set.
fruits = {"Apple", "Mango", "Banana", "Orange", "Grapes"}
fruits.add("Papaya")
fruits.add("Pineapple")
print(fruits)

# 4. Create a set of numbers and remove a specified number from the set.
numbers = {10, 20, 30, 40, 50}
n = int(input("Enter number to remove: "))
numbers.remove(n)
print(numbers)

# 5. Create a set of student names and check whether the entered name exists.
students = {"Rahul", "Amit", "Sneha", "Priya", "Rohit"}
name = input("Enter student name: ")
if name in students:
    print("Student exists")
else:
    print("Student does not exist")

# 6. Create a set of cities and find the total number of cities.
cities = {"Pune", "Mumbai", "Delhi", "Kolhapur", "Nashik"}
print("Total cities:", len(cities))

# 7. Create a set of programming languages and display each language using a for loop.
languages = {"Python", "Java", "C", "C++", "JavaScript"}
for language in languages:
    print(language)

# 8. Create a list containing duplicate numbers and remove duplicates using a set.
numbers = [10, 20, 10, 30, 20, 40, 30]
unique_numbers = set(numbers)
print(unique_numbers)

# 9. Create two sets of integers and find their union.
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
print("Union:", set1.union(set2))

# 10. Create two sets and find the elements common to both sets.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Common elements:", set1.intersection(set2))

# 11. Create two sets and find elements present only in each set.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Only in first set:", set1 - set2)
print("Only in second set:", set2 - set1)

# 12. Create two sets and find elements present in either set but not both.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Symmetric difference:", set1.symmetric_difference(set2))

# 13. Create two sets and check whether the first set is a subset of the second.
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print("Is subset:", set1.issubset(set2))

# 14. Create two sets and check whether the first set is a superset of the second.
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
print("Is superset:", set1.issuperset(set2))

# 15. Create two sets and check whether they have no elements in common.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print("Are disjoint:", set1.isdisjoint(set2))

# 16. Create two sets and check whether they are equal.
set1 = {1, 2, 3, 4}
set2 = {4, 3, 2, 1}
print("Are equal:", set1 == set2)

# 17. Create two sets of subjects and find the subjects studied by both students.
student1 = {"Python", "Java", "DBMS", "Maths"}
student2 = {"Java", "DBMS", "OS", "C++"}
print("Common subjects:", student1.intersection(student2))

# 18. Accept a sentence and display all unique words using a set.
sentence = input("Enter a sentence: ")
words = set(sentence.split())
print("Unique words:", words)

# 19. Create morning and afternoon session sets and find common, unique and all students.
morning = {"Rahul", "Amit", "Sneha", "Priya"}
afternoon = {"Sneha", "Priya", "Rohit", "Neha"}
print("Both sessions:", morning & afternoon)
print("Only morning:", morning - afternoon)
print("Only afternoon:", afternoon - morning)
print("At least one session:", morning | afternoon)

# 20. Create sets representing students enrolled in Python and Java.
python_students = {"Rahul", "Amit", "Sneha", "Priya"}
java_students = {"Sneha", "Priya", "Rohit", "Neha"}
print("Python students:", python_students)
print("Java students:", java_students)

# 21. Find students enrolled in both courses and students enrolled in only one course.
python_students = {"Rahul", "Amit", "Sneha", "Priya"}
java_students = {"Sneha", "Priya", "Rohit", "Neha"}
print("Both courses:", python_students & java_students)
print("Only one course:", python_students ^ java_students)

# 22. Create technical skill sets for two employees and find common, unique and all skills.
employee1 = {"Python", "Java", "SQL", "Git"}
employee2 = {"Java", "Python", "HTML", "CSS"}
print("Common skills:", employee1 & employee2)
print("Unique to Employee 1:", employee1 - employee2)
print("Unique to Employee 2:", employee2 - employee1)
print("All skills:", employee1 | employee2)

# 23. Create available and requested book sets and find which requested books are available.
available_books = {"Python", "Java", "C++", "DBMS", "OS"}
requested_books = {"Python", "DBMS", "HTML"}
print("Available requested books:", available_books & requested_books)

# 24. Store visitor IDs from two days and find unique, returning and day-specific visitors.
day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 105, 106, 107}
print("Unique visitors:", day1 | day2)
print("Returning visitors:", day1 & day2)
print("Only first day:", day1 - day2)
print("Only second day:", day2 - day1)

# 25. Create two sets of friends and find mutual, unique and total unique friends.
user1 = {"Rahul", "Amit", "Sneha", "Priya"}
user2 = {"Sneha", "Priya", "Rohit", "Neha"}
print("Mutual friends:", user1 & user2)
print("Unique to User 1:", user1 - user2)
print("Unique to User 2:", user2 - user1)
print("Total unique friends:", user1 | user2)