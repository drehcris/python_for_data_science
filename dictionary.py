'Example: This example shows how a dictionary stores data using keys and values.
data = { "name": "Jake", "age": 22 }
print(data)

Output
{'name': 'Jake', 'age': 22}

----------------------------------------------------------

'Creating a Dictionary
a = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(a)
​
b = dict(a = "Geeks", b = "for", c = "Geeks")
print(b)

Output
{1: 'Geeks', 2: 'For', 3: 'Geeks'}
{'a': 'Geeks', 'b': 'for', 'c': 'Geeks'}

--------------------------------------------------------

'Accessing Dictionary Items
d = { "name": "Kat", 1: "Python", (1, 2): [1,2,4] }
​# Access using key
print(d["name"])
​# Access using get()
print(d.get("name"))

Output
Kat
Kat

-----------------------------------------------------

'Adding and Updating Dictionary Items
d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
​# Adding a new key-value pair
d["age"] = 22
​# Updating an existing value
d[1] = "Python dict"
print(d)

Output
{1: 'Python dict', 2: 'For', 3: 'Geeks', 'age': 22}

-----------------------------------------------------------

'Removing Dictionary Items
del: removes an item using its key
pop(): removes the item with the given key and returns its value
clear(): removes all items from the dictionary
popitem(): removes and returns the last inserted key-value pair


d = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age':22}
​# Using del 
del d["age"]
print(d)

​# Using pop() 
val = d.pop(1)
print(val)

​# Using popitem()
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")
​
# Using clear()
d.clear()
print(d)

Output
{1: 'Geeks', 2: 'For', 3: 'Geeks'}
Geeks
Key: 3, Value: Geeks
{}

------------------------------------------------------------

'Iterating Through a Dictionary
d = {1: 'Geeks', 2: 'For', 'age':22}
​
# Iterate over keys
for key in d:
    print(key)
​
# Iterate over values
for value in d.values():
    print(value)
​
# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")

Output
1
2
age
Geeks
For
22
1: Geeks
2: For
age: 22

-------------------------------------------------------------

'Nested Dictionaries
'Representation of Nested Dictionary
d = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
print(d)
Try It Yourself
redirect icon

Output
{1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}

-------------------------------------------------------------------
