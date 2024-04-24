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

with open('topics.txt', 'w') as output_file:
    output_file.write("Computer Science\n")
    output_file.write('Arithmatic is good\n')

# import urllib.request
# url = 'https://robjhyndman.com/tsdldata/ecology1/hopedale.dat'

# with urllib.request.urlopen(url) as webpage:
#     for line in webpage:
#         line = line.strip()
#         # line = line.decode('utf-8')
#         print(line)
i = 0
he = "hello"
# while i < 10:
# while (True):
#     i += 1
#     print(he)
#     if (i > 100):
#         break
#         # continue

from typing import TextIO
from io import StringIO

def sum_number_pairs(input_file: TextIO, output_file: TextIO) -> None:
   """Read the data from input_file, which contains two floats per line
    separated by a space. output_file for writing and, for each line in
    input_file, write a line to output_file that contains the two floats from
    the corresponding line of input_file plus a space and the sum of the two
    floats.
    """
   for number_pair in input_file:
        number_pair = number_pair.strip()
        operands = number_pair.split()
        total = float(operands[0]) + float(operands[1])
        new_line = '{0} {1}\n'.format(number_pair, total)
        output_file.write(new_line)

if __name__ == '__main__':
    with open('number_pairs.txt', 'r') as input_file, \
        open('number_pair_sums.txt', 'w') as output_file:
        sum_number_pairs(input_file, output_file)