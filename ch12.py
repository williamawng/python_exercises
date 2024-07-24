import time
#an algorithm is a solution to a problem
counts = [809, 834, 477, 478, 307, 102, 96, 177, 324, 702]
a = min(counts)
print(counts.index(a))

def find_two_smallest(l):
    smallest = min(l)
    smallest_index = l.index(smallest)
    l.remove(smallest)
    next_smallest = min(l)
    next_smallest_index = l.index(next_smallest)
    l.insert(smallest_index, smallest)
    if smallest_index <= next_smallest_index:
        next_smallest_index += 1
    return (smallest_index, next_smallest_index)

t1 = time.perf_counter()
print(find_two_smallest(counts))
t2 = time.perf_counter()
t = (t2 - t1) * 1000
print(f"The code took {t}ms ")
def sim_find2smallest(l):
    l2 = l.copy()
    l2.sort()
    min1 = l2[0]
    min2 = l2[1]
    min1_index = l.index(min1)
    min2_index = l.index(min2)
    return (min1_index, min2_index)
t1 = time.perf_counter()
print(sim_find2smallest(counts))
t2 = time.perf_counter()
t = (t2 - t1) * 1000
print(f"The code took {t}ms ")
print("-"*20)
# 1

print("1")

DNA_sequence = "AATTGCCGTAATTGCCGTAATTGCCGTAATTGCCGTAATTGCCGTAATTGCCGTAATTGCCGTAATTGCCGT"

print(f"DNA_sequence: {DNA_sequence}")
def get_dna_complement(dna):
    complement_seq = ""
    for x in dna:
        if x == "A":
            x = "T"
        elif x == "T":
            x = "A"
        elif x == "G":
            x = "C"
        elif x == "C":
            x = "G"
        complement_seq += x
    return complement_seq
t1 = time.perf_counter()
print(f'ANSWER: {get_dna_complement(DNA_sequence)}')
t2 = time.perf_counter()
t = (t2 - t1) * 1000
print(f"The code took {t}ms ")
def get_dna_complement2(dna):
    dna = dna.replace("A", "X")
    dna = dna.replace("T", "Y")
    dna = dna.replace("G", "Z")
    dna = dna.replace("C", "W")
    dna = dna.replace("X", "T")
    dna = dna.replace("Y", "A")
    dna = dna.replace("Z", "C")
    dna = dna.replace("W", "G")
    return dna
t1 = time.perf_counter()
print(f'ANSWER2: {get_dna_complement2(DNA_sequence)}')
t2 = time.perf_counter()
t = (t2 - t1) * 1000
print(f"The code took {t}ms ")
print("-"*20)
# 2

print("2")

counts = [809, 834, 477, 478, 307, 102, 96, 177, 324, 702]

# def min_index(l):
#     l2 = l.copy()
#     l2.sort()
#     min1 = l2[0]
#     min1_index = l.index(min1)
#     return (min1, min1_index)
# t1 = time.perf_counter()
# print(min_index(counts))
# t2 = time.perf_counter()
# t = (t2 - t1) * 1000
# print(f"The code took {t}ms ")

def min_or_max_index(l, min = True):
    if min:
        l2 = l.copy()
        l2.sort()
        min1 = l2[0]
        min1_index = l.index(min1)
        return (min1, min1_index)
    else:
        l2 = l.copy()
        l2.sort(reverse = True)
        max1 = l2[0]
        max1_index = l.index(max1)
        return (max1, max1_index)
t1 = time.perf_counter()
print(f'ANSWER MIN:{min_or_max_index(counts, min = True)}')
print(f'ANSWER MAX:{min_or_max_index(counts, min = False)}')
t2 = time.perf_counter()
t = (t2 - t1) * 1000
print(f"The code took {t}ms ")