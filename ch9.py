velocities = [0.0, 9.81, 19.62, 29.43]
print(velocities[1])

print(len(velocities))

for i in range(len(velocities)):
    print(velocities[i])


for velocity in velocities:
    print(velocity)

names = ['James', "John", "Jimmothy", "Jennifer"]

for n in names:
    print(n)

for j in range(len(names)):
    print(names[j][0:3])

country = 'United States of America'

for ch in country:
    if ch.isupper():
        print("UPPER:", ch)
    else:
        print("LOWER:", ch)


for i in range(1, 4):
    print(i)

numbers = list(range(1,6))
# print(test)
total = 0
for num in numbers:
    total = total + num

print(total)

values = [4, 10, 3, 8, -6]
for val in values:
    val = val * 2

print(values)


for i in range(len(values)):
    values[i] = values[i] * 2

print(values)

metals = ['Li', 'Na', 'K', "H"]
weights = [6.941, 22.98976928, 39.0983, 1.00784]

for i in range(len(metals)):
    print(metals[i], weights[i])


outer = ['Li', 'Na', 'K']
inner = ['F', 'Cl', 'Br']
for metal in outer:
    for halogen in inner:
        print(metal + halogen)

# 1

print("-" * 15)

celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']

for cele in celegans_phenotypes:
    print(cele)

# 2

half_lives = [87.74, 24110.0, 6537.0, 14.4, 376000.0]

for i in range(len(half_lives)):
    print(half_lives[i])

#3

whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
more_whales = []
print(more_whales)
for wha in whales:
   w =  wha + 1
   more_whales.append(w)
print(more_whales) 

# 4

alkaline_earth_metals = [['beryllium', 4, 9.012], ['magnesium', 12, 24.305], ['calcium', 20, 40.078], ['strontium', 38, 87.62], ['barium', 56, 137.327], ['radium', 88, 226]]
for i in range(len(alkaline_earth_metals)):
    for j in range(len(alkaline_earth_metals[i])):
        print(alkaline_earth_metals[i][j])
print('->' * 10)
for alk in alkaline_earth_metals:
    for al in alk:
        print(al)
number_and_weight = []
for i in range(len(alkaline_earth_metals)):
    number_and_weight.append(alkaline_earth_metals[i][1:])
print(number_and_weight)

# 5
v = number_and_weight
def mystery_function(values):
    """ This function will go through each element in a list and adds the 
    first element in the sublist to a new list called result and will return it.
    """
    result = [] # create an empty list
    for sublist in values: # go through each element in values
        result.append([sublist[0]]) # adds the first element in sublist to result
        for i in sublist[1:]: # for each element in sublist from the second element to the end
            print("RESULT:", result, "RESULT[-1]:", result[-1])

            result[-1].insert(0, i) # inserting element i at the index 0 of the last element of result
    return result # returns the answer
print(mystery_function(values=v))

# 6
# text = ""
# while text.lower() != "quit": # checks if text is not the same as "quit" after converting text into lowercase
#     text = input("Please enter a chemical formula (or 'quit' to exit): ")
#     if text.lower() == "quit": # checks if text is the same as "quit" after converting text into lowercase
#         print("…exiting program")
#     elif text == "H2O":
#         print("Water")
#     elif text == "NH3":
#         print("Ammonia")
#     elif text == "CH4":
#         print("Methane")
#     else:
#         print("Unknown compound")

# 7
country_populations = [1295, 23, 7, 3, 47, 21]
print(sum(country_populations))

total = 0
for cp in country_populations:
    total = total + cp

print(total, "Total")

# 8
rat_1 = [2, 3, 3.5, 2.5, 3, 2, 1.5, 4, 3.5, 2]
rat_2 = [1.99, 2, 4.5, 1.5, 4, 1, 2.5, 5, 2.5, 3]

if rat_1[0] > rat_2[0]:
    print("Rat 1 weighed more than rat 2 on day 1.")
else:
    print("Rat 1 weighed less than rat 2 on day 1.")

if rat_1[0] > rat_2[0]:
    if rat_1[-1] > rat_2[-1]:
        print("Rat 1 remained heavier than Rat 2.")
    else:
        print("Rat 2 became heavier than Rat 1.")

if rat_1[0] > rat_2[0] and rat_1[-1] > rat_2[-1]:
    print("Rat 1 remained heavier than Rat 2.")
else:
    print("Rat 2 became heavier than Rat 1.")

# 9
for i in range(33, 50):
    print(i)

# 10
numbers = list(range(10, 0, -1))
print(numbers)

numbers2 = [str(n) for n in numbers]
# print(numbers2)
print(", ".join(numbers2))

# 11
sum = 0
numbers3 = list(range(2, 23))
for num in numbers3:
    # sum = num + sum
    sum += num

print(sum / len(numbers3))

# 12
from typing import List
def remove_neg(num_list: List[float]) -> None:
    """Remove the negative numbers from the list num_list.
    >>> numbers = [-5, 1, -3, 2]
    >>> remove_neg(numbers)
    >>> numbers
    [1, 2]
    """
    neg_nums = []
    for item in num_list:
        if item < 0:
            neg_nums.append(item)
    
    print("NEG_NUMS:", neg_nums)
    
    for neg in neg_nums:
        num_list.remove(neg)

numbers = [1, 2, 3, -3, 6, -1, -3, 1]
# remove_neg(numbers)
# print(numbers)

def remove_neg2(num_list: List[float]) -> List[float]:
    my_list = []    # creating a new list. we are going to add only positive numbers
                    # to this one.
    # how do I remove negative numbers from num_list?
    for item in num_list:
        if item >= 0:
            my_list.append(item)
    return my_list

print(remove_neg2(numbers))

# 13
def draw_t(rows, columns):
    for i in range(rows-1, -1, -1):
        for j in range(i, columns, 1):
            # print(f"{i} {j}")
            print("T", end="")
        print("")

print("-"*10)
draw_t(7, 7)
print("-"*10)

# 14
def draw_t2(rows, columns):
    for i in range(rows):
        for j in range(columns):
            # print(f"{i} {j}")
            if j >= (columns-1 - i):
                print("T", end="")
            else:
                print(" ", end="")
        print("")

draw_t2(7, 7)

# 15
print("-"*10)

def draw_t_w(rows, columns):
    i = rows -1
    while i > -1:
        j = i
        while j < columns:
            print("T", end="")
            j = j + 1
        print("")
        i = i - 1

draw_t_w(7, 7)

print("-"*10)

def draw_t2_w(rows, columns):
    for i in range(rows):
        for j in range(columns):
            # print(f"{i} {j}")
            if j >= (columns-1 - i):
                print("T", end="")
            else:
                print(" ", end="")
        print("")
draw_t2_w(3,3)


#########################################
# this is while loop practice.
# weight = 10

# weeks = 0
# while (weight < 100):
#     weeks += 1
#     print("10 lbs gained this week.")
#     weight = weight + 10

# print(f"It took {weeks} weeks.")
#########################################


# 16
rat_1_weight = 10
rat_2_weight = 15
rat_1_rate = 0.04
rat_2_rate = 0.04

twenty_five_pct_of_rat1 = rat_1_weight * 0.25
final_w = rat_1_weight + twenty_five_pct_of_rat1
weeks = 0

while rat_1_weight < final_w:
    weeks += 1
    rat_1_weight = rat_1_weight + (rat_1_weight*rat_1_rate)
    print(f"rat 1 weight after week 1: {rat_1_weight}")

print(f"rat 1 weight is {rat_1_weight}")
print(f"It took {weeks} weeks for rat 1 to become 25% heavier.")

weeks = 0
rat_1_weight = 10
rat_2_weight = 10
rat_1_rate = 0.02
rat_2_rate = 0.01

# print(rat_2_weight)
# print(rat_2_weight + rat_2_weight * .10)

while rat_1_weight <= (rat_2_weight + rat_2_weight * .10):
    weeks += 1
    rat_1_weight = rat_1_weight + (rat_1_weight * rat_1_rate)
    rat_2_weight = rat_2_weight + (rat_2_weight * rat_2_rate)
    print(f"Week {weeks}: rat_1_weight is {rat_1_weight} and rat_2_weight is {rat_2_weight}")

print(f"It took {weeks} weeks for rat 1 to be 10% heavier than rat 2.")

