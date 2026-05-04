def fun():
    print("Welcome to GFG")

No Output 

def fun():
    print("Welcome to GFG")
    
fun()

Output 
Welcome to GFG

-----------------------------------------

'Function Arguments
def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))

Output 
Even
Odd

---------------------------------------

'Types of Function Arguments
'1. Default Arguments:
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)

Output
x:  10
y:  50

'2. Keyword Arguments:
def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')

Output
Geeks Practice
Geeks Practice

'3. Positional
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Olivia", 27)

print("\nCase-2:")
nameAge(27, "Olivia")

Output
Case-1:
Hi, I am Olivia
My age is  27

Case-2:
Hi, I am 27
My age is  Olivia

'4. Arbitrary Arguments
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')
//*args: recebe argumentos posicionais (sem nome), como uma tupla.
//**kwargs: recebe argumentos nomeados (com chave=valor), como um dicionário.

  Output
Non-Keyword Arguments (*args):
Hey
Welcome

Keyword Arguments (**kwargs):
first == Geeks
mid == for
last == Geeks

'Function within Functions
def f1():
    s = 'I love GeeksforGeeks'
    def f2():
        print(s)
        
    f2()
f1()


Output
I love GeeksforGeeks

'Anonymous Functions
def c1(x): return x*x*x   
c2 = lambda x : x*x*x  //A palavra-chave é usada para criar funções anônimas.

print(c1(7))
print(c2(7))

Output 
343
343

'Return Statement
def sq_value(num):
    """This function returns the square
    value of the entered number"""
    return num**2

print(sq_value(2))
print(sq_value(-4))

Output 
4
16

'Pass by Reference and Pass by Value
'Mutable objects: Changes inside the function affect the original object.
'Immutable objects: The original value remains unchanged.

def myFun(x):
    x[0] = 20

lst = [10, 11, 12, 13]
myFun(lst)
print(lst)   

def myFun2(x):
    x = 20

a = 10
myFun2(a)
print(a)

Output
[20, 11, 12, 13]
10


'Recursive Functions
def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
print(factorial(4))

Output 
24



