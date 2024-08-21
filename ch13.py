import time
import random
x = ["b", "f", "g", "r", "z", "w", "l"]
# random randrange takes three arguments (x, y, z)
# x and y are the two numbers which is the range, x is optional
# z is the increment, z is also optional
# the argument in range is how many elements are picked
y = [random.randrange(1, 1000, 1) for i in range(1000)]
y.sort()
target = 456
def linear_search(l, target):
    for i in range(len(l)):
        # print(i)
        # print(l[i])
        if target == l[i]:
            return i
    return -1

t1 = time.perf_counter()
print(f'ANSWER: {linear_search(y, target)}')
t2 = time.perf_counter()
t = (t2 - t1) * 1000
print(f"The code took {t}ms ")

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1

t1 = time.perf_counter()
print(binary_search(y, target))
t2 = time.perf_counter()
t = (t2 - t1) * 1000
print(f"The code took {t}ms ")

# selection sort

def selectionSort(array):
    size = len(array)
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])

y = [random.randrange(1, 1000, 1) for i in range(1000)]
# print(y)
t1 = time.perf_counter()
selectionSort(y)
t2 = time.perf_counter()
t = (t2 - t1) * 1000
print(f"Selection sort took {t}ms ")
# print(y)

# insertion sort

def insertionSort(arr):
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position

y = [random.randrange(1, 1000, 1) for i in range(1000)]
# print(y)
t1 = time.perf_counter()
insertionSort(y)
t2 = time.perf_counter()
t = (t2 - t1) * 1000
print(f"Insertion sort took {t}ms ")
# print(y)

