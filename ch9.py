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

#Exercise 1

print("-" * 15)

celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']

for cele in celegans_phenotypes:
    print(cele)

half_lives = [87.74, 24110.0, 6537.0, 14.4, 376000.0]

for i in range(len(half_lives)):
    print(half_lives[i])

whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
more_whales = []
print(more_whales)
for wha in whales:
   w =  wha + 1
   more_whales.append(w)
print(more_whales) 

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

text = ""
while text.lower() != "quit": # checks if text is not the same as "quit" after converting text into lowercase
    text = input("Please enter a chemical formula (or 'quit' to exit): ")
    if text.lower() == "quit": # checks if text is the same as "quit" after converting text into lowercase
        print("…exiting program")
    elif text == "H2O":
        print("Water")
    elif text == "NH3":
        print("Ammonia")
    elif text == "CH4":
        print("Methane")
    else:
        print("Unknown compound")
