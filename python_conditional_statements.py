age = 20
if age >= 18:
    print("Eligible to vote.")

Output
Eligible to vote.'

'Short Hand if
age = 19
if age > 18: print("Eligible to Vote.")

Output
Eligible to Vote.

--------------------------------------------------

'If else Conditional Statement
age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")

Output
Travel for free.'

'Short Hand if-else
marks = 45
res = "Pass" if marks >= 40 else "Fail"
print(f"Result: {res}")

Output
Result: Pass

------------------------------------------------

'elif Statement
age = 25
​if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

Output
Young adult.

------------------------------------------------

'Nested if-else Conditional Statement
age = 70
is_member = True
​
if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")

Output
30% senior discount!

-------------------------------------------------

'Ternary Conditional Statement
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)

Output
Adult

-------------------------------------------------

'Match-Case Statement
number = 2
​
match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")
Output:

Two or Three

-------------------------------------------------
