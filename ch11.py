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
print("EXCERSISES")
print("-"*20)
# 1
print("1")
def find_dups(l):
    my_set = set()
    for item in l:
        if l.count(item) > 1:
            my_set.add(item)
    return my_set


m = find_dups([1, 2, 3, 4,4,4,4,5,5,6,7,8,9,9])
print(m)
print("-"*20)
# 2
print("2")
print("Refer to Multimol2.py")
print("-"*20)
# 3
print("3")
males = {"James", "Juilian", "Jared", "Jack", "Jeremy"}
females = {"Julia", "Jasmine", "Juliet", "Jane", "Joy"}
def pairs (x, y):
    all_pairs = []
    for i in range(5):
        male = x.pop()
        female = y.pop()
        tmp_tuple = (male, female)
        all_pairs.append(tmp_tuple)
    return all_pairs

p = pairs(males, females)
print(p)
print("-"*20)
# 4
print("4")

print("SKIP")

print("-"*20)
# 5

print("5")

colours = {'red': 1, 'green': 1, 'blue': 2, 'white': 7}
def count_values (x):
    count = set()
    for k, v in x.items():
        print(f"KEY:{k}; VALUE:{v}")
        count.add(v)
    return len(count)

c = count_values(colours)
print(f"ANSWER: {c}")

print("-"*20)
# 6

print("6")

particles = {'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07, 'neutrino': 0.14}
def least_likely_obsv(x):
    # Using min() + list comprehension + values()
    # Finding min value keys in dictionary
    # print(x.values()) # this will give you all the values in the dictionary
    # print(min(x.values())) # find the min of all the values.
    temp = min(x.values())
    res = [k for k in x if x[k] == temp] # get the key of the min.
    return res
least_likely = least_likely_obsv(particles)
print(least_likely)

print("-"*20)
# 7

print("7")

students = {'student1': 'James', 'student2': 'William', 'student3': 'William', 'student4': 'James', 'student5': 'Cecilia', 'student6': 'Cecilia', 'student7': 'Andrew', 'student8': 'Andrew'}
def count_duplicates(x):
    seen = {}
    cnt = 0
    for k, v in x.items():
        # print(f"KEY:{k}; VALUE:{v}")
        if seen.get(v): # I have seen this item
            # hence, increment the count
            cnt += 1
        else:
            # I haven't seen this item. So set the dictionary value to 1 (for seen{})
            seen[v] = 1

    return cnt


print(f'ANSWER: {count_duplicates(students)}')

print("-"*20)
# 8

print("8")

balanced_colour = {'R': 0.2, 'G': 0.5, 'B': 0.3}
def is_balanced(colour):
    total = 0
    for k, v in colour.items():
        print(k, v)
        total += v
    if total == 1:
        return True
    else:
        return False

print(is_balanced(balanced_colour))

print("-"*20)
# 9

print("9")

colour = {'R': 0.2, 'G': 0.5, 'B': 0.3, 'green': 1}
colours = {'R': 0.2, 'green': 1, 'blue': 2, 'white': 7}
def dict_intersect(x, y):
    z = {}
    for k, v in x.items():
        # print(k,v)
        if y.get(k):
            y_val = y.get(k)
            if v == y_val:
                z[k] = v

    return z

print(f'ANSWER: {dict_intersect(colour, colours)}')

print("-"*20)
# 10

print("10")

scientists = {
    'jgoodall' :    {
                        'surname' : 'Goodall',
                        'forename' : 'Jane',
                        'born' : 1934,
                        'died' : None,
                        'notes' : 'primate researcher',
                        'author' : ['In the Shadow of Man',
                        'The Chimpanzees of Gombe']
                    },
    'rfranklin' :   {
                        'surname' : 'Franklin',
                        'forename' : 'Rosalind',
                        'born' : 1920,
                        'died' : 1957,
                        'notes' : 'contributed to discovery of DNA',
                        # 'author' : ['hi']
                    },
    'rcarson' :     {
                        'surname' : 'Carson',
                        'forename' : 'Rachel',
                        'born' : 1907,
                        'died' : 1964,
                        'notes' : 'raised awareness of effects of DDT',
                        'author' : ['Silent Spring'],
                    }
}

def db_headings(d):
    headings = set()
    for k,v in d.items():
        # print(k,v)
        for i, j in v.items():
            # print(i, j)
            headings.add(i)
    return headings

print(f'ANSWER: {db_headings(scientists)}')

print("-"*20)
# 11

print("11")

def db_consistent(d):
    previous = set()
    for k,v in d.items():
        # print(k,v)
        for i, j in v.items():
            # print(i, j)
            if not previous:
                previous = set(v)
            else:
                current = set(v)
                diff = previous - current
                if diff:
                    return False
    return True

print(f'ANSWER: {db_consistent(scientists)}')

print("-"*20)
# 12

print("12")

A = {0:1, 6:3}
B = {0:4, 6:1}

def sparse_add(a,b):
    answer = {}
    for key in set(list(a.keys()) + list(b.keys())):
        # print(f'key: {key}')
        a_val = a.get(key) or 0
        b_val = b.get(key) or 0
        answer[key] = a_val + b_val

    return answer


print(f'ANSWER A: {sparse_add(A,B)}')

def sparse_mul(a,b):
    total = 0
    answer = {}
    for key in set(list(a.keys()) + list(b.keys())):
        # print(f'key: {key}')
        a_val = a.get(key) or 0
        b_val = b.get(key) or 0
        answer[key] = a_val * b_val
    for k, v in answer.items():
        total += v
    return total


print(f'ANSWER B: {sparse_mul(A,B)}')

print(f'ANSWER C: I would need to ask her what are the dimensions/length of the vector. ')