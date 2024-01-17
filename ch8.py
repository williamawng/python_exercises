my_list = ['W', 'i', 'l', 'l', 'i', 'a', 'm']

my_list2 = ["*"]

for i in range(len(my_list)):
    print(f'{my_list[i]}')

for i in range(len(my_list2)):
    print(f'{my_list2[i]}')

for i in range(len(my_list)):
    for j in range(len(my_list2)):
        print(f'{my_list[i], my_list2[j]}')

kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
print(kingdoms[0])
print(kingdoms[5])
print(kingdoms[:3])
print(kingdoms[2:5])
print(kingdoms[4:])
print([])
print(kingdoms[-6])
print(kingdoms[-1])
print(kingdoms[:-3])
print(kingdoms[-4:-1])
print(kingdoms[-2:])
