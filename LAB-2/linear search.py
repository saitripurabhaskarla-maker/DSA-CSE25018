# write a python program to perform linear search on the given input

# taking input
n = int(input("Please enter no of elements you want to search: "))
arr = []

for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)


# linear search function
def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


target = int(input("Enter the number to search for: "))
result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")
