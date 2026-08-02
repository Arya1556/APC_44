#Write a program to input a string and display its length without using the len() function. 

str1=input("Enter a string: ")
count=0
for i in str1:
    count+=1
print("Length of the string is:",count)


#Count the number of vowels, consonants, digits, spaces, and special characters in a given string
str1=input("Enter a string: ")
vowels=0
consonants=0
digits=0
spaces=0
special_characters=0
for i in str1:
    if i in "aeiouAEIOU":
        vowels+=1
    elif i.isalpha():
        consonants+=1
    elif i.isdigit():
        digits+=1
    elif i.isspace():
        spaces+=1
    else:
        special_characters+=1
print("Vowels:",vowels)
print("Consonants:",consonants)
print("Digits:",digits)
print("Spaces:",spaces)
print("Special Characters:",special_characters)

#	Reverse the given string without using built-in reverse functions. 
str1=input("Enter a string: ")
reversed_str=""
for i in str1:
    reversed_str=i+reversed_str
print("Reversed string is:",reversed_str)

#•Check whether the entered string is a palindrome
str1=input("Enter a string: ")
reversed_str=""
for i in str1:
    reversed_str=i+reversed_str
if str1==reversed_str:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#	Count the number of uppercase and lowercase letters in a string
str1=input("Enter a string: ")
uppercase=0
lowercase=0
for i in str1:
    if i.isupper():
        uppercase+=1
    elif i.islower():
        lowercase+=1
print("Uppercase letters:",uppercase)
print("Lowercase letters:",lowercase)

# Replace all occurrences of a given character with another character. 
str1=input("Enter a string: ")
old=input("Enter the character to be replaced: ")  
new=input("Enter the new character: ")
new_str=""
for i in str1:
    if i==old:
        new_str+=new
    else:
        new_str+=i
print("New string is:",new_str)

#	Remove all spaces from the input string. 
str1=input("Enter a string: ")
new_str=""
for i in str1:
    if i!=" ":
        new_str+=i
print("String after removing spaces:",new_str)

#	Find the number of times a specified character appears in a string. 
str1=input("enter a string: ")
checked=""
for i in str1:
    if i not in checked:
      count=0
      for j in str1:
         if i==j:
             count+=1
      print(i,"appears",count,"times")
      checked+=i

#	Print the first and last character of a string
str1=input("Enter a string: ")
if len(str1) > 0:
    first_char = str1[0]
    last_char = str1[-1]
    print("First character:", first_char)
    print("Last character:", last_char)

#Display each character of a string along with its ASCII value.
str1=input("Enter a string: ")
for i in str1:
    print(f"Character: {i}, ASCII Value: {ord(i)}")

#	Count the total number of words in a sentence.
str1=input("Enter a sentence: ")
count=0
for i in str1:
    if i==" ":
        count+=1
print("Total number of words in the sentence is:",count+1) 


#Find the longest word in a given sentence

str1=input("Enter a sentence: ")
words = str1.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("The longest word in the sentence is:", longest_word)


#Find the shortest word in a sentence. 
str1=input("Enter a sentence: ")
words = str1.split()
shortest_word = ""
for word in words:
    if shortest_word == "" or len(word) < len(shortest_word):
        shortest_word = word
print("The shortest word in the sentence is:", shortest_word)

#	Convert the first letter of every word to uppercase. 
str1=input("Enter a sentence: ")
str2=str1.title()
print("The sentence after converting the first letter of every word to uppercase is:",str2)

#	Print all duplicate characters in a string. 
s = input("Enter a string: ")
duplicates = []

for ch in s:
    if s.count(ch) > 1 and ch not in duplicates:
        duplicates.append(ch)

print("Duplicate characters:", " ".join(duplicates))


#	Display the frequency of every character in a string. 
s = input("Enter a string: ")

for ch in sorted(set(s)):
    print(ch, ":", s.count(ch))
 
#	Check whether two strings are anagrams. 
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower()):
    print("Anagram")
else:
    print("Not Anagram")

#	Remove duplicate characters while maintaining the original order. 
    s = input("Enter a string: ")
result = ""

for ch in s:
    if ch not in result:
        result += ch

print("Result:", result)

#	Check whether a given substring exists in the main string. 
main = input("Enter main string: ")
sub = input("Enter substring: ")

if sub in main:
    print("Substring found")
else:
    print("Substring not found")


#	Count how many times a specific word appears in a sentence. 
sentence = input("Enter a sentence: ")
word = input("Enter word to search: ")

count = sentence.split().count(word)

print("Occurrences:", count)

#	Password Validator
import string

password = input("Enter password: ")

if (len(password) >= 8 and
    any(c.isupper() for c in password) and
    any(c.islower() for c in password) and
    any(c.isdigit() for c in password) and
    any(c in string.punctuation for c in password)):
    print("Valid Password")
else:
    print("Invalid Password")


#.	Run-Length Encoding
s = input("Enter string: ")

result = ""
count = 1

for i in range(len(s)):
    if i < len(s)-1 and s[i] == s[i+1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

print(result)

#	String Compression 
s = input("Enter string: ")

compressed = ""
count = 1

for i in range(len(s)):
    if i < len(s)-1 and s[i] == s[i+1]:
        count += 1
    else:
        compressed += s[i] + str(count)
        count = 1

if len(compressed) < len(s):
    print(compressed)
else:
    print(s)


#	Most Frequent Character 
s = input("Enter string: ")

max_char = ""
max_count = 0

for ch in set(s):
    if s.count(ch) > max_count:
        max_count = s.count(ch)
        max_char = ch

print("Most frequent character:", max_char)


#	Second Most Frequent Character 
s = input("Enter string: ")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

if len(sorted_freq) >= 2:
    print("Second most frequent character:", sorted_freq[1][0])
else:
    print("Not enough unique characters")


#	Caesar Cipher 
text = input("Enter message: ")
shift = int(input("Enter shift: "))

result = ""

for ch in text:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        result += chr((ord(ch)-base+shift)%26+base)
    else:
        result += ch

print("Encrypted:", result)

#Decreption
text = input("Enter encrypted message: ")
shift = int(input("Enter shift: "))

result = ""

for ch in text:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        result += chr((ord(ch)-base-shift)%26+base)
    else:
        result += ch

print("Decrypted:", result)

#Email Validation
import re

email = input("Enter email: ")

pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")


#.	Word Frequency Dictionary 
text = input("Enter encrypted message: ")
shift = int(input("Enter shift: "))

result = ""

for ch in text:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        result += chr((ord(ch)-base-shift)%26+base)
    else:
        result += ch

print("Decrypted:", result)


#	Sentence Reversal 
sentence = input("Enter sentence: ")

words = sentence.split()

print(" ".join(words[::-1]))


#	String Rotation 

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Yes")
else:
    print("No")

