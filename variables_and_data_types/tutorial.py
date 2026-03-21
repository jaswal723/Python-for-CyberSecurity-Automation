# variable assignment

login_failures = 5
print(login_failures)

print("\n--------------\n")

# mathematical operations on numbers

a = 5
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

print("\n--------------\n")

# booleans

is_admin = True
a = 4<5
print(a)
a = 4>5
print(a)

print("\n--------------\n")

# Strings assignments

my_string = "Hello World"
my_string_2 = 'Hello World 2'
my_string_3 = "Hello'World"
print(my_string)
print(my_string_2)
print(my_string_3)
print(len(my_string))

print("\n--------------\n")

# string property of ordered sequence

my_string = "Hello World"
print(my_string[2])
print(my_string[2:5])
print(my_string[2:7:2])

print("\n--------------\n")

# string property of immutability

name = "Sam"
last_chars = name[1:]
new_name = 'P' + last_chars
print(new_name)

print("\n--------------\n")

# capitalize method

my_string = "i am a hacker"
new_string = my_string.capitalize()
print(new_string)

print("\n--------------\n")

# endswith and startswith methods

check_ending = my_string.endswith("cker")
print(check_ending)
check_starting = my_string.startswith("abc")
print(check_starting)

print("\n--------------\n")

# islower and isupper methods

check_lower = my_string.islower()
print(check_lower)
check_upper = my_string.isupper()
print(check_upper)

print("\n--------------\n")

# lower and upper methods

convert_lower = my_string.lower()
print(convert_lower)
convert_upper = my_string.upper()
print(convert_upper)

print("\n--------------\n")

# replace method

my_string = "spam, spam, and more spam"
print(my_string)
new_string = my_string.replace("spam","fraud",1)
print(new_string)
new_string = my_string.replace("spam","fraud")
print(new_string)

print("\n--------------\n")

# split method

new_string = my_string.split(" ")
print(new_string)
new_string = my_string.split(",")
print(new_string)

print("\n--------------\n")

# strip method

my_string = "   Hello World    "
print(my_string)
print(len(my_string))
new_string = my_string.strip()
print(new_string)
print(len(new_string))

print("\n--------------\n")

# f strings

ip = "10.1.2.3"
port = 22
name = "Hacker"
print(f'User {name} logged in from {ip} using port {port}')