# selection sort

n = int(input("Please enter the number of elements in the array: "))
arr = []

for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

def selection_sort(arr):
    a = len (arr)
    for i in range (a-1):
        min_index= i
        for j in range (i +1, a):
            if arr[j]<arr[min_index]:
                min_index  = j
                arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

selection_sort(arr)
print("sorted array is ", arr)
