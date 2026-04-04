import csv

with open("file_handling_csv\\test.txt", mode ='r') as f:
    print(f.read())
    f.seek(5)
    print(f.read())

print("\n---------------\n")

with open("file_handling_csv\\test.txt", mode ='w') as f:
    f.write("This is new comment")

print("\n---------------\n")

with open("file_handling_csv\\test.txt", mode ='a') as f:
    f.write("\nThis is appended")

print("\n---------------\n")

lines = ["Line 1", "Line 2", "Line 3"]
with open("file_handling_csv\\test.txt", mode='a') as f:
    f.writelines(row + "\n" for row in lines)

print("\n---------------\n")

with open("file_handling_csv\\data.csv",mode='r') as file:
    reading_csv = csv.reader(file)
    for row in reading_csv:
        print(row)

print("\n---------------\n")

with open("file_handling_csv\\data.csv",mode='r') as file:
    reading_csv = csv.DictReader(file)
    for row in reading_csv:
        print(row)

print("\n---------------\n")

with open("file_handling_csv\\data.csv",mode='w',newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name","age"])
    writer.writeheader()
    writer.writerow({"name":"Rithik","age":30})
    writer.writerow({"name":"Mukul","age":24})

print("\n---------------\n")

new_data = []

with open("file_handling_csv\\data.csv", mode='r') as file:
    reading_csv = csv.DictReader(file)
    for row in reading_csv:
        if int(row['age']) > 20:
            new_data.append(row)

with open("file_handling_csv\\final.csv", mode='w',newline="") as file:
    writer = csv.DictWriter(file,fieldnames=["name","age"])
    writer.writeheader()

    writer.writerows(new_data)

print("\n---------------\n")    