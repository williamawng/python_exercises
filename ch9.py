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