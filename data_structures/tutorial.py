# Defining a list

list_1 = [] 
print(list_1)
print(type(list_1))

print("\n-------------\n")

# Assigning values to a list

ip_address = ["1.1.1.1","2.2.2.2","3.3.3.3"]
print(ip_address)
print(len(ip_address))

print("\n-------------\n")

# List containing various data types

list_1 = [22, 7.5, "Hello"]
print(list_1) 

print("\n-------------\n")

# Indexing and Slicing in Lists

print(list_1[1])
print(list_1[1:3])
list_1[1] = 8.5
print(list_1)

print("\n-------------\n")

# Append method in Lists

list_1.append(90)
print(list_1)

print("\n-------------\n")

# Pop method in lists

list_1.pop(1)
print(list_1)

print("\n-------------\n")

# insert method in Lists

list_1.insert(2,"Something")
print(list_1)

print("\n-------------\n")

# sort method in lists

list_1 = [1,89,23,56,12]
list_1.sort()
print(list_1)

print("\n-------------\n")

# reverse method in lists

list_1.reverse()
print(list_1)

print("\n-------------\n")

# defining dictionary

dict_1 = {}
print(type(dict_1))

print("\n-------------\n")

# assigning values to dictionary

access_level = {"kunal": "standard", "mukul": "admin"}
print(access_level)
print(access_level["mukul"])

print("\n-------------\n")

# assigning new values to dictionaries

access_level["rithik"] = "standard"
print(access_level)

print("\n-------------\n")

# keys are unique

access_level["kunal"] = "admin"
print(access_level)

print("\n-------------\n")

# keys, values and items in dictionary

print(access_level.keys())
print(access_level.values())
print(access_level.items())

print("\n-------------\n")

# nested dictionaries

dict_2 = {'key1': "value1", "key2": {'k1':"v1","k2":"v2"}}
access_level = {"kunal": "standard", "mukul": "admin", "rithik": ["power","superadmin"]}
print(access_level["rithik"][1])
dict_1 = {'k1': 123, 'k2': [0,1,2], 'k3': {'inside_key':100}}
print(dict_1['k3']['inside_key'])

print("\n-------------\n")

# Defining tuples

tuple_1 = (1,2,3)
print(tuple_1)

print("\n-------------\n")

# Indexing and slicing in Tuple

print(tuple_1[1:])

print("\n-------------\n")

# Defining sets

set_1 = set([1,2,3,4,5,6,7])
print(type(set_1))
print(set_1)

print("\n-------------\n")

# Sets contain unique values

set_1 = set([1,2,2,3,3,4,5,6,7,7])
print(set_1)

print("\n-------------\n")

# defining other data structures in similar manner

list_1 = list((1,2,3,4))
print(list_1)

print("\n-------------\n")

# add method in sets

set_1 = set([1,2,2,3,3,4,5,6,7,7])
set_1.add(29)
print(set_1)

print("\n-------------\n")

# Mathematical operations on sets

set_1 = set([1,2,3,4,5])
set_2 = set([3,4,5,6,7])

print(set_1 - set_2)
print(set_1 | set_2)
print(set_1 & set_2)
print(set_1 ^ set_2)

print("\n-------------\n")