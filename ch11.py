numbers = {1,1,2}
print(numbers)

vowels = {'a', 'e', 'i', 'o', 'u'}
print(vowels)

vowels2 = {'a', 'e', 'a', 'a', 'i', 'o', 'u', 'u'}
print(vowels2)
print(vowels == vowels2)

print({'a', 'e', 'i', 'o', 'u'} == {'a', 'e', 'a', 'a', 'i', 'o', 'u', 'u'})

print(type(vowels))
print(type(vowels2))

number_list = [1, 1, 2, 3]
print(number_list)
number_set = set(number_list)
print(number_set)

vowels.add('y')
print(vowels)

lows = {0, 1, 2, 3, 4}
odds = {1, 3, 5, 7, 9}
ten = set(range(10))
print(ten)
lows_minus_odds = lows.difference(odds)
print(lows_minus_odds)
lows_intersection_odds = lows.intersection(odds)
print(lows_intersection_odds)
lows_subset_ten = lows.issubset(ten)
print(lows_subset_ten)
lows_superset_odds = lows.issuperset(odds)
print(lows_superset_odds)
lows_union_odds = lows.union(odds)
print(lows_union_odds)
lows_sym_diff_odds = lows.symmetric_difference(odds)
print(lows_sym_diff_odds)
print(lows - odds) # Equivalent to lows.difference(odds)
print(lows & odds) # Equivalent to lows.intersection(odds)
print(lows <= odds) # Equivalent to lows.issubset(odds)
print(lows >= odds) # Equivalent to lows.issuperset(odds)
print(lows | odds) # Equivalent to lows.union(odds)
print(lows ^ odds) # Equivalent to lows.symmetric_difference(odds)

life = (['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]) #Tuple
print(life)
print(life[2][0])

(x, y) = (10, 20)
print(x)
print(y)

# 1

def find_dups(l):
    my_set = set()
    for item in l:
        if l.count(item) > 1:
            my_set.add(item)
    return my_set


m = find_dups([1, 2, 3, 4,4,4,4,5,5,6,7,8,9,9])
print(m)

# 2