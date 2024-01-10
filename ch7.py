print("William".lower())
print("william".capitalize())
print("At my house I met tom, he was cooking tomatoes.".count("t"))

print('hello'.upper())
print('Happy Birthday!'.lower())
print('WeeeEEEEeeeEEEEeee'.swapcase())
print('ABC123'.isupper())
print('aeiouAEIOU'.count('a'))
print('hello'.endswith('o'))
print('hello'.startswith('H'))
print('Hello {0} {1} {2}{3}'.format('Python', 'from', 'me', '.'))
print('Hello {0}! Hello {1}!'.format('Python', 'World'))

print('tomato'.count('o'))
print('tomato'.find('o'))
print('tomato'.find('o', 'tomato'.find('o') + 1))
print('avocado'.find('o', 'avocado'.find('o') + 1))
print('runner'.replace('n', 'b'))

s = "  yes  "

print(s.strip())

fruit = "pineapple"

print(fruit.find('p', fruit.count('p')))
print(fruit.count(fruit.upper().swapcase()))
print(fruit.replace(fruit.swapcase(), fruit.lower()))

season = 'summer'
print('I love {0}!'.format(season))
print(f"I love {season}!")

side1 = 3
side2 = 4
side3 = 5
print('The sides have lengths {0}, {1}, {2}.'.format(side1, side2, side3))

print('boolean'.capitalize())

print('CO2 H2O'.find('2'))

print('CO2 H2O'.find('2', 'CO2 H2O'.find('2') + 1))

print('Boolean'.islower())

print('MoNDaY'.lower().capitalize())

print(' Monday'.lstrip())

def total_occurrences(s1: str, s2: str, ch: str) -> int:
    """Precondition: len(ch) == 1
    Return the total number of times that ch occurs in s1 and s2.
    >>> total_occurrences('color', 'yellow', 'l')
    3
    >>> total_occurrences('red', 'blue', 'l')
    >>> total_occurrences('green', 'purple', 'b')
    """
    a = s1.count(ch) + s2.count(ch)
    return a
print(total_occurrences('color', 'yellow', 'l'))
print(total_occurrences('Billy', 'Lilly lemonade', 'l'))