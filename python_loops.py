'For Loop
n = 4
for i in range(0, n):
    print(i)

Output
0
1
2
3

----------------------------------------------------

'Example: Iterating Over List, Tuple, String and Dictionary Using for Loops in Python
d = dict({'x':123, 'y':354})
for x in d:
    print("%s  %d" % (x, d[x]))
li = ["geeks", "for", "geeks"]
for x in li:
    print(x)
    
tup = ("geeks", "for", "geeks")
for x in tup:
    print(x)
    
s = "abc"
for x in s:
    print(x)
    
d = dict({'x':123, 'y':354}) # criando um dicionário com chave e valor
for x in d: # o for percorre as CHAVES do dicionário (não os valores)
    print("%s  %d" % (x, d[x])) 
    # d[x] pega o valor correspondente à chave
    # %s = string (chave)
    # %d = número inteiro (valor)
    
set1 = {10, 30, 20}
for x in set1:
    print(x),

Output
geeks
for
geeks
geeks
for
geeks
a
b
c
x  123
y  354
10
20
30

-----------------------------------------------------

'Iterating by Index of Sequences
li = ["geeks", "for", "geeks"] #Para cada índice da lista, pegue o elemento naquela posição e imprima
for index in range(len(li)):
    print(li[index])

Output
geeks
for
geeks

---------------------------------------------------

'While Loop
cnt = 0 # Enquanto cnt for menor que 3, continue repetindo
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")
cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")

Hello Geek
Hello Geek
Hello Geek

Output
Hello Geek
Hello Geek
Hello Geek

'Infinite While Loop
while (True):
    print("Hello Geek")
while (True):
    print("Hello Geek")

-------------------------------------------------

'Nested Loops
from __future__ import print_function
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()

Output
1 
2 2 
3 3 3 
4 4 4 4 

----------------------------------------------

'Loop Control Statements
'Continue Statement
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)

Output
Current Letter : g
Current Letter : k
Current Letter : f
Current Letter : o
Current Letter : r
Current Letter : g
Current Letter : k

'Break Statement
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break
​
print('Current Letter :', letter)

Output
Current Letter : e

'Pass Statement
for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)

Output
Last Letter : s

-----------------------------------------------------
  
