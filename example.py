#Number is zero or Nonzero
num=int(input("enter a number: "))
if num==0:
    print("number is zero")
else:
    print("number is non zero")

#largest number from two numbers

num1=int(input("enter first number : "))
num2=int(input("enter second number: "))  

if num1>num2:
    print(" largest number is: ",num1)
else:
  print(" largest number is: ",num2)


#number is positive or negative
num=int(input("enter a number: "))
if num<0:
    print("number is positive")
else:
    print("number is negative")

#check whether character is vowel or consonant
character =input("enter a character: ")

if character=="a" or character=="e" or character=="i" or character=="o" or character=="u":
    print("character is vowel")
else:
    print("character is consonant")


#evaluate student performance
score=int(input("enter the score"))
if score >= 90:
    print("Grade:Excellent ")
elif score >= 80:
    print("Grade:very good ")
elif score >= 70:
    print("Grade:good ")
elif score >= 60:
    print("Grade:average ")
else:
    print("Grade:poor ")

# Find largest and smallest from three numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Find the largest number
if num1 > num2 and num1 > num3:
    largest = num1
elif num2 > num1 and num2 > num3:
    largest = num2
else:
    largest = num3

# Find the smallest number
if num1 < num2 and num1 < num3:
    smallest = num1
elif num2 < num1 and num2 < num3:
    smallest = num2
else:
    smallest = num3

print("Largest number is:", largest)
print("Smallest number is:", smallest)

#number ids even or odd
num=int(input("enter the number: "))
if num%2==0:
   print("number is even")
else:
   print("number id odd")

year=int(input("enter the year: "))
if year%4==0:
   print("year is leap year")
else:
   print("year is not leap year")

# Find largest and smallest from three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1>num2:
   if num1>num3:
      print("largest is",num1)
   else:
      print("largest is",num2)
else:
   if num2>num3:
      print("largest is",num2)
   else:
      print("largest is",num3)

if num1<num2:
   if num1<num3:
      print("smallest is",num1)
   else:
      print("smallest is",num2)
else:
   if num2<num3:
      print("smallest is",num2)
   else:
      print("smallest is",num3)
   

