def scan_target():
    print("Scanning port 80")

scan_target()

print("\n ------------------- \n")

def scan_target(port):
    print(f'Scanning port {port}')

scan_target(22)

print("\n ------------------- \n")

def scan_target(port = 80):
    print(f'Scanning port {port}')

scan_target()

print("\n ------------------- \n")

def scan_target(port):
    if port == 22:
        return True
    else:
        return False

is_22 = scan_target(23)
print(is_22)

print("\n ------------------- \n")

def scan_port(*args):
    for x in args:
        print(x)
    print(args)

scan_port(22,80,443)

print("\n ------------------- \n")

def scan_port(**kwargs):
    print(kwargs)

scan_port(threshhold = 5, number_of_ports = 10)

print("\n ------------------- \n")

def sum_of_numbers(*args):
    sum = 0
    for x in args:
        sum = sum + x
    return sum

answer = sum_of_numbers(10,20,30,40)
print(answer)

print("\n ------------------- \n")