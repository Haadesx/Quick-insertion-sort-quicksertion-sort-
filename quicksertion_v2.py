import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quick_insertion_sort(arr, threshold=10):
    if len(arr) <= threshold:
        insertion_sort(arr)
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        quick_insertion_sort(left)
        quick_insertion_sort(right)
        
        arr[:] = left + middle + right

# CHOICE
data_type = input("Enter 'i' for integers or 'f' for floating-point numbers: ")

if data_type == 'i':
    # INT RANGE
    min_range = int(input("Enter the minimum value for random integers: "))
    max_range = int(input("Enter the maximum value for random integers: "))

    # NUMBER OF RANDOM INTEGERS
    num_random_data = int(input("Enter the number of random integers to sort: "))

    # GENERATION
    random_data = [random.randint(min_range, max_range) for _ in range(num_random_data)]

    #Quick-Insertion Sort.
    quick_insertion_sort(random_data)

    # Display
    print("Sorted Random Integers:", random_data)
elif data_type == 'f':
    #RANGE FOR FLOATING POINT NUMBERS
    min_range = float(input("Enter the minimum value for random floating-point numbers: "))
    max_range = float(input("Enter the maximum value for random floating-point numbers: "))

    # NUMBER OF FLOATING POINT NUMBERS
    num_random_data = int(input("Enter the number of random floating-point numbers to sort: "))

    # GENERATION
    random_data = [random.uniform(min_range, max_range) for _ in range(num_random_data)]

    #  Quick-Insertion Sort.
    quick_insertion_sort(random_data)

    # Display
    print("Sorted Random Floating-Point Numbers:", random_data)
else:
    print("Invalid choice. Please enter 'i' for integers or 'f' for floating-point numbers.")
