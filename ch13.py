import time
import random
count = 1000
x = ["b", "f", "g", "r", "z", "w", "l"]
# random randrange takes three arguments (x, y, z)
# x and y are the two numbers which is the range, x is optional
# z is the increment, z is also optional
# the argument in range is how many elements are picked
y = [random.randrange(1, count, 1) for i in range(count)]
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

y = [random.randrange(1, count, 1) for i in range(count)]
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

y = [random.randrange(1, count, 1) for i in range(count)]
# print(y)
t1 = time.perf_counter()
insertionSort(y)
t2 = time.perf_counter()
t = (t2 - t1) * 1000
print(f"Insertion sort took {t}ms ")
# print(y)

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[],
    # if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

arr = [random.randrange(1, count, 1) for i in range(count)]

# print(arr)

t1 = time.perf_counter()
merge_sort(arr, 0, len(arr) - 1)
t2 = time.perf_counter()
t = (t2 - t1) * 1000
print(f"Merge sort took {t}ms ")

# print(arr)

