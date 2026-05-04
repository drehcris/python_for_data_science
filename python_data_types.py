*Numeric: int, float, complex
Sequence Type: string, list, tuple
Mapping Type: dict
Boolean: bool
Set Type: set, frozenset
Binary Types: bytes, bytearray, memoryview*

x = 50  # int
x = 60.5  # float
x = "Hello World"  # string
x = ["geeks", "for", "geeks"]  # list 
x = ("geeks", "for", "geeks")  # tuple


-------------------------------------------------------

a = 5
print(type(a))
​
b = 5.0
print(type(b))
​
c = 2 + 4j
print(type(c))

Output
<class 'int'>
<class 'float'>
<class 'complex'>


--------------------------------------------------

'String Data Type
print(s)
s = 'Welcome to the Geeks World'
print(s)
​
# check data type 
print(type(s))
​
# access string with index
print(s[1])
print(s[2])
print(s[-1]) # -1 refers to the last character, -2 is second last, and so on

Output
Welcome to the Geeks World
<class 'str'>
e
l
d

--------------------------------------------------

'List Data Type
# Empty list
a = []
​
# list with int values
a = [1, 2, 3]
print(a)
​
# list with mixed values int and String
b = ["Geeks", "For", "Geeks", 4, 5]
print(b)

Output
[1, 2, 3]
['Geeks', 'For', 'Geeks', 4, 5]

'Access List Items: 
a = ["Geeks", "For", "Geeks"]
print("Accessing element from the list")
print(a[0])
print(a[2])
​
print("Accessing element using negative indexing")
print(a[-1])
print(a[-3])

Output
Accessing element from the list
Geeks
Geeks
Accessing element using negative indexing
Geeks
Geeks

---------------------------------------------------

'Tuple Data Type
# initiate empty tuple
tup1 = ()
​
tup2 = ('Geeks', 'For')
print("\nTuple with the use of String: ", tup2)

Output
Tuple with the use of String:  ('Geeks', 'For')

'Access Tuple Items:
tup1 = (1, 2, 3, 4, 5)
​
# access tuple items
print(tup1[0])
print(tup1[-1])
print(tup1[-3])

Output
1
5
3

------------------------------------------------

'3. Boolean Data Type
print(type(True))
print(type(False))
print(type(true))

Output:
<class 'bool'>
<class 'bool'>
Hangup (SIGHUP)
Traceback (most recent call last):
  File "/home/guest/sandbox/Solution.py", line 3, in <module>
    print(type(true))
               ^^^^
NameError: name 'true' is not defined. Did you mean: 'True'?

'Truthy and Falsy Values
if 1:
    print("1 is truthy")
​
if not 0:
    print("0 is falsy")

Output
1 is truthy
0 is falsy

-----------------------------------------------------------

'4. Set Data Type
# initializing empty set
s1 = set()
​
s1 = set("GeeksForGeeks")
print("Set with the use of String: ", s1)
​
s2 = set(["Geeks", "For", "Geeks"])
print("Set with the use of List: ", s2)

Output
Set with the use of String:  {'k', 'e', 's', 'o', 'G', 'F', 'r'}
Set with the use of List:  {'Geeks', 'For'}

'Access Set Items
heck if item exist in s
set1 = set(["Geeks", "For", "Geeks"]) #Duplicates are removed automatically
print(set1) 
​
# loop through set
for i in set1:
   print(i, end=" ") #prints elements one by one
  
# check if item exist in set   
print("Geeks" in set1)

Output
{'Geeks', 'For'}
Geeks For True

-------------------------------------------------------------

'5. Dictionary Data Type
# initialize empty dictionary
d = {}

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)
# initialize empty dictionary
d = {}
​
d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)
​
# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)

Output
{1: 'Geeks', 2: 'For', 3: 'Geeks'}
{1: 'Geeks', 2: 'For', 3: 'Geeks'}


'Accessing Key-value in Dictionary
d = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
​
# Accessing an element using key
print(d['name'])
​
# Accessing a element using get
print(d.get(3))

Output
For
Geeks

---------------------------------------------------------

