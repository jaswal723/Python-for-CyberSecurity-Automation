x = 5
y = 0

# z = x/y

# print(f"The value of x/y is {z}")
# print("Execution Complete")

print("\n-----------------------\n")

x = 5
y = 0

try:
    z = x/y
except:
    print("The division by Zero generated an error.")
else:
    print("There was no error and the execution was successful.")
finally:
    print("Irrespective of what happened in try block, this code will execute.")


print("\n-----------------------\n")


while True:
    try:
        result = int(input("Enter an integer\n"))
    except:
        print("Invalid input. Please enter a valid integer.")
        continue
    else:
        print(f"The Integer is {result}")
        break

print("\n-----------------------\n")