import os

names_list = ["Kuda", "Jabu", "Matipa", "Kundai"]
file_name = "names.txt"

# Writing to the file
with open(file_name, "w") as file:
    for name in names_list:
        file.write(name + "\n")

print("Names have been written to names.txt")

# Reading from the file
print("\nReading names from names.txt:")
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        for line in file:
            print(line.strip())
else:
    print("File not found.")
