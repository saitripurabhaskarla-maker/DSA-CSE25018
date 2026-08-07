# Insertion Sort

n = int(input("Please enter the number of elements in the array: "))
arr = []

for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

def insertion_sort(arr):
    a = len(arr)

    for i in range(1, a):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

insertion_sort(arr)
print("Sorted array:", arr)
