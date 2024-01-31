from operator import itemgetter
my_list = ['W', 'i', 'l', 'l', 'i', 'a', 'm']

my_list2 = ["*"]

values = [0, 1, 2]
kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']


def main():
    
    for i in range(len(my_list)):
        print(f'{my_list[i]}')

    for i in range(len(my_list2)):
        print(f'{my_list2[i]}')

    for i in range(len(my_list)):
        for j in range(len(my_list2)):
            print(f'{my_list[i], my_list2[j]}')

    
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
    appointments = ['9:00', '10:30', '14:00', '15:00', '15:30']
    print(appointments)
    # appointments.append('16:30')
    print(appointments)
    appointments = appointments + ['16:30']
    print(appointments)
    """The second method is the one that created a new list due to the fact that if you remove 'appointments = ' the function doesn't work."""
    ids = [4353, 2314, 2956, 3382, 9362, 3900]
    # ids.remove(3382)
    # print(ids)
    print(ids.index(9362))
    ids.insert(5, 4499)
    print(ids)
    ids.extend([5566, 1830])
    print(ids)
    ids.reverse()
    print(ids)
    ids.sort(reverse=False)
    print(ids)
    alkaline_earth_metals = [['beryllium', 4], ['magnesium', 12], ['calcium', 20], ['strontium', 38], ['barium', 56], ['radium', 88]]
    print(alkaline_earth_metals)
    print(alkaline_earth_metals[5][1])
    print(len(alkaline_earth_metals))
    alkaline_earth_metals2 = sorted(alkaline_earth_metals, key=itemgetter(1), reverse=True)
    print(alkaline_earth_metals2[0][1])
    temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
    print(temps)
    temps.sort()
    print(temps)
    low_temps = temps[0:2]
    print(low_temps)
    warm_temps = temps [2:]
    print(warm_temps)
    temps_in_celsius = low_temps + warm_temps
    print(temps_in_celsius)

    def same_first_last(L:list) -> bool:
        if L[0] == L[-1]:
            return True
        else:
            return False

    print(same_first_last([3, 4, 2, 8, 4]))

    for elem in temps_in_celsius:
        print(elem)

    text = ""
    for i in range(5):
        for j in range(5):
            text += "*"
        text += "\n"
    print(text)

    def is_longer(L1: list, L2: list) -> bool:
        if len(L1) > len(L2):
            return True
        else:
            return False

    print(is_longer([1, 2, 3], [2, 3]))
    print(is_longer([1, 2, 3], [4, 5, 6]))


    
    print(values)
    values[1] = values
    print("[0]", values[0])
    print("[1]", values[1])
    print("[2]", values[2])
    for curr in values[1]:
        print("CURRENT:", curr)

    units = [['km', 'miles', 'league'], ['kg','pound', 'stone']]
    print(units[0])
    print(units[1])
    print(units[0][0])
    print(units[1][0])
    print(units[0][1:])
    print(units[1][:2])

    print("-"*10)

    print(units[-2])
    print(units[-1])
    print(units[-2][-3])
    print(units[-1][-3])
    print(units[-2][-2:])
    print(units[-1][:-1])


if __name__ == "__main__":
    print("HELLO")
    main()