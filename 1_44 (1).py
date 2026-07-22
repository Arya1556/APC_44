Python 3.15.0b3 (tags/v3.15.0b3:cf16a33, Jun 23 2026, 10:03:50) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
x="Hello world"
print(type(x))
<class 'str'>
x='Hello world'
print(type(x))
SyntaxError: multiple statements found while compiling a single statement
x='hello'
print(type(x))
<class 'str'>
x=100
print(type(x))
<class 'int'>
x=3.14
print(type(x))
<class 'float'>

x=ij
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x=ij
NameError: name 'ij' is not defined. Did you mean: 'id'?
x=1j
print(type(x))
<class 'complex'>
x=["apple","banana","cherry']
   
SyntaxError: unterminated string literal (detected at line 1)
x=["apple","banana","cherry"]
   
print(type(x))
   
<class 'list'>
x=("apple","banana","cherry")
   
print(type(x))
   
<class 'tuple'>
x=range(0)
   
print(type(x))
   
<class 'range'>
x={"name":"john","age":20}
   
print(type(x))
   
<class 'dict'>
x={"apple","banana"}
   
print(type(x))
   
<class 'set'>
x=frozenset({"apple","banana"})
   
print(type(x))
   
<class 'frozenset'>
x=true
   
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    x=true
NameError: name 'true' is not defined. Did you mean: 'True'?
x=True
   
print(type(x))
   
<class 'bool'>
x=b"arya"
   
print(type(x))
   
<class 'bytes'>
x=bytearray(s)
   
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    x=bytearray(s)
NameError: name 's' is not defined
x=bytearray
   
print(type(x))
   
<class 'type'>
 x=bytearray(5)
   
SyntaxError: unexpected indent
x=bytearray(5)
   
print(type(x))
   
<class 'bytearray'>
x=memoryview(bytes(5))
   
print(type(x))
   
<class 'memoryview'>
x=None
   
print(type(x))
   
<class 'NoneType'>
x=10
   
y=5
   
x+y
   
15
x-y
   
5
x*y
   
50
x/y
   
2.0
x%y
   
0
x**y
   
100000
x//y
   
2
x=5
   
x+=3
   
print(x)
   
8
x-=3
   
print(x)
   
5
x*=3
   
print(x)
   
15
x/=3
   
print(x)
   
5.0
x%=3
   
print(x)
   
2.0
x=10
   
x//=3
   
print(x)
...    
3
>>> x**=3
...    
>>> print(x)
...    
27
>>> x=10
...    
>>> y=5
...    
>>> x==y
...    
False
>>> x!=y
...    
True
>>> x>y
...    
True
>>> x<y
...    
False
>>> x>=y
...    
True
>>> x<=y
...    
False
>>> x<5 & x<10
...    
False
>>> x=3
...    
>>> x<5 & x<10
...    
False
>>> x<5 and x<10
...    
True
>>> x<5 or x<10
...    
True
>>> x>5 or x>10
...    
False
>>> not (x<5 and x<10)
...    
False

#if statement
num=int(input("enter the number: "))
if num%2==0:
   print("number is even")


#if-else statement
age=int(input("enter your age: "))
if age>18:
   print("eligible for voting")
else:
   print("not eligible")


#elif statement
score=int(input("enter the score"))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
