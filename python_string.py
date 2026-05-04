'Creating a String
s1 = 'GfG'  
s2 = "GfG"  
print(s1)
print(s2)

Output
GfG
GfG

----------------------------------------------------

'Multi-line Strings
#Use triple quotes ('''...''' ) or ( """...""") for strings that span multiple lines. Newlines are preserved.
s = """I am Learning
Python String on GeeksforGeeks"""
print(s)
​
s = '''I'm a 
Geek'''
print(s)

Output
I am Learning
Python String on GeeksforGeeks
I'm a 
Geek


'Accessing characters in String
'Example 1: Access specific characters through positive indexing.
s = "GeeksforGeeks"
print(s[0])   
print(s[4])

Output
G
s

'Example 2: Read characters from the end using negative indices.
s = "GeeksforGeeks"
print(s[-10])  
print(s[-5])

Output
k
G

----------------------------------------------------

'String Slicing
print(s[::-1]) 
s = "GeeksforGeeks"
print(s[1:4])    
print(s[:3])     
print(s[3:])    
print(s[::-1]) # Percorra a string de trás pra frente

Output
eek
Gee
ksforGeeks
skeeGrofskeeG

-----------------------------------------------------

'String Iteration
s = "Python"
for char in s:
    print(char)

Output
P
y
t
h
o
n

------------------------------------------------------

'String Immutability
s = "geeksforGeeks"
s = "G" + s[1:]  
print(s)

Output
GeeksforGeeks

------------------------------------------------------

'Deleting a String
s = "GfG"
del s

----------------------------------------------------

'Updating a String
s = "hello geeks"
s1 = "H" + s[1:]                  
s2 = s.replace("geeks", "GeeksforGeeks")  
print(s1)
print(s2)

Output
Hello geeks
hello GeeksforGeeks

-------------------------------------------------------

'Common String Methods
'1. len(): returns the total number of characters in a string (including spaces and punctuation).
s = "GeeksforGeeks"
print(len(s))

Output
13

'2. upper() and lower(): upper() method converts all characters to uppercase whereas, 
'lower() method converts all characters to lowercase.
s = "Hello World"
print(s.upper())
print(s.lower())

Output
HELLO WORLD
hello world

'3. strip() and replace(): strip() removes leading and trailing whitespace from the 
'string and replace() replaces all occurrences of a specified substring with another.
s = "   Gfg   "
print(s.strip())    
​
s = "Python is fun"
print(s.replace("fun", "awesome"))

Output
Gfg
Python is awesome

--------------------------------------------------------------

'Concatenating and Repeating Strings
'1. Strings can be combined by using + operator.
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

Output
Hello World

'2. We can repeat a string multiple times using * operator.
s = "Hello "
print(s * 3)

Output
Hello Hello Hello

-----------------------------------------------------------

'Formatting Strings
'1. Using f-strings: most preferred way to format strings is by using f-strings.
name = "Jake"
age = 22
print(f"Name: {name}, Age: {age}")

Output
Name: Jake, Age: 22

'2. Using format(): Another way to format strings is by using format() method.
s = "My name is {} and I am {} years old.".format( "Emily", 22)
print(s)

Output
My name is Emily and I am 22 years old.

--------------------------------------------------------------

'String Membership Testing
s = "GeeksforGeeks"
print("Geeks" in s)
print("GfG" in s)

Output
True
False

-------------------------------------------------------------
