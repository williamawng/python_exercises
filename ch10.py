path = "."
my_file = f"{path}/planets.txt"

file = open(my_file, 'r')
contents = file.read()
file.close()
print(contents)

with open(my_file, 'r') as file:
    contents = file.read()
print(contents)


import os
# get current working directory
path = os.getcwd()
print("PATH:", path)

# change directory
# os.chdir('../')
# path = os.getcwd()
# print("PATH:", path)

with open(my_file, 'r') as example_file:
    first_ten_chars = example_file.read(10)
    the_rest = example_file.read()
print("The first 10 characters:", first_ten_chars)
print("The rest of the file:", the_rest)

with open(my_file, 'r') as example_file:
    lines = example_file.readlines()
print(lines)

for planet in reversed(lines):
    print(planet.strip())

with open(my_file, 'r') as data_file:
    for line in data_file:
        print(f"{line.strip()} has {len(line)} characters.")