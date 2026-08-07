n = int(input("Please enter no of elements you want to search: "))
arr = []

for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

def binary_search(arr, target):
   left, right = 0, len(arr) - 1
   while left <= right:
       mid = (left + right) // 2
       if arr[mid] == target:
           return mid 
       elif arr[mid] < target:
           left = mid + 1 
       else:
           right = mid - 1 
   return -1

target = int(input("please enter the element you want to search in the above array"))

binary_search(arr , target)
