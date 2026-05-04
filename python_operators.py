'Arithmetic Operators
a = 15
b = 4

print("Addition:", a + b)  
print("Subtraction:", a - b) 
print("Multiplication:", a * b)  
print("Division:", a / b) 
print("Floor Division:", a // b)  
print("Modulus:", a % b) 
print("Exponentiation:", a ** b)  

Output
Addition: 19
Subtraction: 11
Multiplication: 60
Division: 3.75
Floor Division: 3
Modulus: 3
Exponentiation: 50625

-------------------------------------------------------

'Comparison Operators
a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b) 'diferente de
print(a >= b)
print(a <= b)

Output
False
True
False
True
False
True

-----------------------------------------------------

'Logical Operators
Logical not
logical and
logical or

a = True
b = False
print(a and b)
print(a or b)
print(not a)

Output
False
True
False

------------------------------------------------------

'Bitwise Operators
Bitwise NOT
Bitwise Shift
Bitwise AND
Bitwise XOR
Bitwise OR

a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

Output
0
14
-11
14
2
40

-----------------------------------------------------

'Assignment Operators
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

Output
10
20
10
100
102400

-----------------------------------------------------

'Identity Operators
a = 10
b = 20
c = a

print(a is not b)
print(a is c)

Output
True
True

----------------------------------------------------

'Membership Operators
x = 24
y = 20
my_list = [10, 20, 30, 40, 50]

if (x not in my_list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in my_list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

Output
x is NOT present in given list
y is present in given list

----------------------------------------------------

'Ternary Operator
Syntax :  [on_true] if [expression] else [on_false] 

a, b = 10, 20
min = a if a < b else b

print(min)

Output
10

-------------------------------------------------

'Precedence and Associativity of Operators
'Operator Precedence
expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")

Output
610
Hello! Welcome.'

  
'Operator Associativity
print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)

Output
100.0
6
0
512

--------------------------------------------------
