#Write a Python program using regular expressions to extract all digits from a given string.

import re

string = input("Enter a string: ")

digits = re.findall(r'\d', string)

print("Digits:", digits)

#Accept a sentence and display all words beginning with the letter A or a.
import re

sentence = input("Enter a sentence: ")

words = re.findall(r'\b[Aa]\w*', sentence)

print("Words beginning with A or a:", words)

#Write a program to count the occurrences of vowels in a given string using regular expressions
import re

string = input("Enter a string: ")

vowels = re.findall(r'[aeiouAEIOU]', string)

print("Vowels:", vowels)
print("Total vowels:", len(vowels))

#Write a program to extract all uppercase letters from a given string.
import re

string = input("Enter a string: ")

uppercase = re.findall(r'[A-Z]', string)

print("Uppercase letters:", uppercase)

#Write a program to identify all spaces, tabs, and newline characters in a text.
import re

text = "Hello World\tPython\nProgramming is fun"

characters = re.findall(r'[ \t\n]', text)

print("Whitespace characters:", characters)
print("Total whitespace characters:", len(characters))

#Write a program to replace multiple consecutive spaces with a single space
import re

string = input("Enter a string: ")

result = re.sub(r' {2,}', ' ', string)

print("Result:", result)

#Accept a sentence and display all words containing exactly five characters
import re

sentence = input("Enter a sentence: ")

words = re.findall(r'\b[A-Za-z]{5}\b', sentence)

print("Five-character words:", words)

#Write a program to identify all words ending with the letter s.
import re

sentence = input("Enter a sentence: ")

words = re.findall(r'\b[A-Za-z]*s\b', sentence, re.IGNORECASE)

print("Words ending with s:", words)

#Write a program to remove all special characters from a given string while retaining letters, digits, and spaces.
import re

string = input("Enter a string: ")

result = re.sub(r'[^A-Za-z0-9 ]', '', string)

print("Result:", result)

#Write a program to count the number of words in a sentence using regular expressions.
import re

sentence = input("Enter a sentence: ")

words = re.findall(r'\b\w+\b', sentence)

print("Number of words:", len(words))

#Write a program to validate a 10-digit Indian mobile number using a regular expression.
import re

mobile = input("Enter mobile number: ")

if re.fullmatch(r'[6-9]\d{9}', mobile):
    print("Valid Indian mobile number")
else:
    print("Invalid Indian mobile number")

#Accept an email address and check whether it follows a reasonable email format.
import re

email = input("Enter email address: ")

pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

if re.fullmatch(pattern, email):
    print("Valid email format")
else:
    print("Invalid email format")
    
#Write a program to extract dates in DD-MM-YYYY format from a given paragraph.
import re

paragraph = input("Enter a paragraph: ")

dates = re.findall(
    r'\b(?:0[1-9]|[12]\d|3[01])-(?:0[1-9]|1[0-2])-\d{4}\b',
    paragraph
)

print("Dates found:", dates)

import re

# 1. Identify web addresses beginning with http:// or https://
text = "Visit http://example.com and https://google.com"
urls = re.findall(r'https?://[^\s]+', text)
print("1. Web addresses:", urls)


# 2. Extract all hashtags from a social media post
post = "Learning #Python and #Matplotlib is fun! #Coding123"
hashtags = re.findall(r'(?<!\w)#[A-Za-z0-9_]+', post)
print("2. Hashtags:", hashtags)


# 3. Check password strength
password = "Python@123"

# At least 8 characters, uppercase, lowercase, digit, special character
pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9\s])\S{8,}'

if re.fullmatch(pattern, password):
    print("3. Strong password")
else:
    print("3. Weak password")


# 4. Identify consecutive repeated words, ignoring case
sentence = "This is is a test TEST sentence"
repeated = re.findall(
    r'\b([A-Za-z]+)\s+\1\b',
    sentence,
    re.IGNORECASE
)
print("4. Repeated words:", repeated)


# 5. Extract six-digit Indian PIN codes
paragraph = "My PIN is 411001 and another PIN is 110001."
pins = re.findall(r'(?<!\d)[1-9]\d{5}(?!\d)', paragraph)
print("5. PIN codes:", pins)


# 6. Validate common Indian vehicle registration format
vehicle = "MH12AB1234"

# Example: MH12AB1234
pattern = r'^[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}$'

if re.fullmatch(pattern, vehicle):
    print("6. Vehicle number format is valid")
else:
    print("6. Invalid vehicle number format")


# 7. Extract file extensions from filenames
text = "Files: report.pdf, photo.jpg, notes.txt, program.py"
extensions = re.findall(
    r'\b[\w-]+\.(\w+)\b',
    text
)
print("7. File extensions:", extensions)


# 8. Remove HTML tags, extra whitespace, and unwanted punctuation
html = "<p>Hello!!!   World,   welcome to <b>Python</b>.</p>"

# Remove HTML tags
cleaned = re.sub(r'<[^>]*>', ' ', html)

# Remove punctuation except basic word characters and whitespace
cleaned = re.sub(r'[^\w\s]', '', cleaned)

# Replace multiple whitespace characters with one space
cleaned = re.sub(r'\s+', ' ', cleaned).strip()

print("8. Cleaned text:", cleaned)


# 9. Extract invoice numbers, dates, and monetary amounts
invoice = """
Invoice No: INV-2025-123
Date: 15-08-2025
Total Amount: Rs. 12,500.50
"""

invoice_no = re.findall(
    r'Invoice\s*No\s*:\s*([A-Z0-9-]+)',
    invoice,
    re.IGNORECASE
)
dates = re.findall(
    r'\b\d{2}-\d{2}-\d{4}\b',
    invoice
)
amounts = re.findall(
    r'(?:Rs\.?|INR|₹)\s*[\d,]+(?:\.\d{2})?',
    invoice,
    re.IGNORECASE
)

print("9. Invoice numbers:", invoice_no)
print("   Dates:", dates)
print("   Amounts:", amounts)


# 10. Identify single-line comments in Python source code
source = '''
# This is a comment
x = 10  # This is another comment
print("# Not necessarily a comment")
'''

# Simple pattern: finds # through the end of each line.
# Limitation: also matches # inside strings.
comments = re.findall(r'#.*', source)
print("10. Possible comments:", comments)

# Note:
# Regex alone cannot reliably distinguish comments from # inside
# string literals, especially triple-quoted or multiline strings.
# Python's tokenize module is better for accurately identifying comments.


# 11. Validate product codes in ABC-1234-XY format
product_code = "ABC-1234-XY"
pattern = r'^[A-Z]{3}-\d{4}-[A-Z]{2}$'

if re.fullmatch(pattern, product_code):
    print("11. Valid product code")
else:
    print("11. Invalid product code")


# 12. Extract student names, roll numbers, and marks
students = """
Name: Rahul, Roll: 101, Marks: 85
Name: Priya, Roll: 102, Marks: 92
Name: Amit, Roll: 103, Marks: 78
"""

pattern = (
    r'Name:\s*([A-Za-z ]+),\s*'
    r'Roll:\s*(\d+),\s*'
    r'Marks:\s*(\d+(?:\.\d+)?)'
)

records = re.findall(pattern, students)

print("12. Student records:")
for name, roll, marks in records:
    print("Name:", name.strip(),
          "| Roll:", roll,
          "| Marks:", marks)


# 13. Extract DOI identifiers, publication years, email addresses,
#     and URLs from research paper references
references = """
Research Paper (2023). DOI: 10.1000/xyz123.
Contact: author@example.com
Available at https://example.org/paper
Another study (2021). DOI: 10.1234/abcd.5678
"""

# Extract DOI identifiers
dois = re.findall(
    r'\b10\.\d{4,9}/[^\s<>"\'\,;]+',
    references
)

# Extract four-digit publication years (basic pattern)
years = re.findall(
    r'\b(?:19|20)\d{2}\b',
    references
)

# Extract email addresses (reasonable basic pattern)
emails = re.findall(
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
    references
)

# Extract HTTP and HTTPS URLs
urls = re.findall(
    r'https?://[^\s<>"\']+',
    references
)

print("13. DOI identifiers:", dois)
print("    Publication years:", years)
print("    Email addresses:", emails)
print("    URLs:", urls)