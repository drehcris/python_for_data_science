'Creating a List
'1. Using Square Brackets: Square brackets [] are used to create a list directly.
a = [1, 2, 3, 4, 5] # List of integers
b = ['apple', 'banana', 'cherry'] # List of strings
c = [1, 'hello', 3.14, True] # Mixed data types
​
print(a)
print(b)
print(c)

Output
[1, 2, 3, 4, 5]
['apple', 'banana', 'cherry']
[1, 'hello', 3.14, True]


'2. Using list() Constructor: A list can also be created by passing an iterable 
'(such as tuple, string or another list) to the list() constructor.
a = list((1, 2, 3, 'apple', 4.5))  
print(a)
​
b = list("GFG")
print(b)

Output
[1, 2, 3, 'apple', 4.5]
['G', 'F', 'G']

'3. Creating List with Repeated Elements: A list with repeated elements can be created using the multiplication (*) operator.
a = [2] * 5
b = [0] * 7
​
print(a)
print(b)

Output
[2, 2, 2, 2, 2]
[0, 0, 0, 0, 0, 0, 0]

-------------------------------------------------------

'Internal Representation of Lists
a = [10, 20, "GfG", 40, True]
print(a)        
print(a[0])     
print(a[1])  
print(a[2])

Output
[10, 20, 'GfG', 40, True]
10
20
GfG

-----------------------------------------------------

'Accessing List Elements
a = [10, 20, 30, 40, 50]
print(a[0])    
print(a[-1])
print(a[1:4])   # elements from index 1 to 3

Output
10
50
[20, 30, 40]

--------------------------------------------------

'Adding Elements into List
append(): Adds an element at the end of the list.
extend(): Adds multiple elements to the end of the list.
insert(): Adds an element at a specific position.
clear(): removes all items.

a = []
​a.append(10)  
print("After append(10):", a)  
​a.insert(0, 5)
print("After insert(0, 5):", a) 
​a.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", a) 
​a.clear()
print("After clear():", a)

Output
After append(10): [10]
After insert(0, 5): [5, 10]
After extend([15, 20, 25]): [5, 10, 15, 20, 25]
After clear(): []

------------------------------------------------

'Updating Elements into List
a = [10, 20, 30, 40, 50]
a[1] = 25 
print(a)

Output
[10, 25, 30, 40, 50]

-----------------------------------------------

'Removing Elements from List
remove(): Removes the first occurrence of an element.
pop(): Removes the element at a specific index or the last element if no index is specified.
del statement: Deletes an element at a specified index.

a = [10, 20, 30, 40, 50]
​a.remove(30)  
print("After remove(30):", a)
​popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 
​del a[0]  
print("After del a[0]:", a)

Output
After remove(30): [10, 20, 40, 50]
Popped element: 20
After pop(1): [10, 40, 50]
After del a[0]: [40, 50]

--------------------------------------------------

'Iterating Over Lists
a = ['apple', 'banana', 'cherry']
for item in a:
    print(item)

Output
apple
banana
cherry

-----------------------------------------------

'Nested Lists
matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]
print(matrix[1][2])

Output
6

----------------------------------------------

'List Comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)

Output
[1, 4, 9, 16, 25]

Explanation:
for x in range(1, 6): loops through each number from 1 to 5 (excluding 6).
x**2: squares each number x.
[ ]: collects all the squared numbers into a new list.
  
-----------------------------------------------
