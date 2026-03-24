user = "Kunal"
is_admin = False

if is_admin == True:
    print(f'The user {user} is an admin. Treat carefully.')
else:
    print(f'The user {user} is not an admin. No concerns.')

print("\n-----------------\n")

access_level = "superuser"
#standard, poweruser, superuser

if access_level == "standard":
    pass
elif access_level == "poweruser":
    print("Power User")
else:
    print("Super User")

print("\n-----------------\n")

port = [1,21,22,80,443]

for x in port:
    print(f'Scanning Port - {x}.')

for x in port:
    if x == 22:
        print(f'Sensitive port - {x}')
    else:
        print(f'Normal port - {x}')

print("\n-----------------\n")

port = [1,21,22,80,443]

for x in port:
    if x == 22:
        print(f'We found it - Port number {x}')
        continue
    else:
        pass
    print(f"This is the rest of the code in the for loop which will run. {x}")

print("\n-----------------\n")

number = 0

while number <= 10:
    print(f"Number = {number}")
    number += 1