
x = 5
name = "Samantha"  
print(x)
print(name)

Output
5
Samantha

----------------------------------------------------

'Below listed variable names are valid:
age = 21
_colour = "lilac"
total_score = 90

'Below listed variables names are invalid:
1name = "Error"  # Starts with a digit
class = 10       # 'class' is a reserved keyword
user-name = "Doe"  # Contains a hyphen

-------------------------------------------------

'Basic Assignment: Variables are assigned values using the = operator.
x = 5
y = 3.14
z = "Hi"

'Dynamic Typing: variables are dynamically typed, meaning the same variable can hold different types of values during execution.
x = 10
x = "Now a string"

-------------------------------------------------

'Assigning Same Value: allows assigning the same value to multiple variables in a single line, which can be useful for initializing variables with the same value.
a = b = c = 100
print(a, b, c)

Output
100 100 100

'Assigning Different Values: we can assign different values to multiple variables simultaneously, making the code concise and easier to read.
print(x, y, z)
x, y, z = 1, 2.5, "Python"
print(x, y, z)

Output
1 2.5 Python

---------------------------------------------------

'Understanding Variable Reassignment
'In this example, we check whether modifying one variable affects another when both initially reference the same object.
print(x)
x = 1
y = x
y = y + 1
​
print(x)
print(y)

Output
1
2

'Deleting a Variable
'We can remove a variable from the namespace using the del keyword. This deletes the variable and frees up the memory it was using.
x = 10
del x
print(x) 
Output

'ERROR!
'Traceback (most recent call last):
  'File "<main.py>", line 3, in <module>
'NameError: name 'x' is not defined

--------------------------------------------------------
'Practical Examples
'1. Swapping Two Variables: Using multiple assignments, we can swap the values of two variables without needing a temporary variable.
a, b = 5, 10
a, b = b, a
print(a, b)

Output
10 5

'2. Counting Characters in a String: Assign the results of multiple operations on a string to variables in one line.
print("Length of the word:", len
word = "Python"
length = len(word)
print("Length of the word:", length)

Output
Length of the word: 6

------------------------------------------------------
