from ssl import enum_certificates


file_name = input("Enter the file name: ")
pattern = input("Enter the pattern to search: ")

file = open(file_name, 'r')
lines = file.readlines()
file.close()
for i, line in enumerate():
    if pattern in line:
        print(file_name,i+1, line.strip())

