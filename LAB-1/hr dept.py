def search_id(ids, target, i=0):
    if i == len(ids):          # reached end, not found
        return -1
    if ids[i] == target:       # found it
        return i
    return search_id(ids, target, i+1)   # check next one


# Employee ID list
employee_ids = [101, 102, 103, 104, 105]

target = int(input("Enter Employee ID to search: "))
position = search_id(employee_ids, target)

if position != -1:
    print("Found at position:", position + 1)
else:
    print("Not Found")
