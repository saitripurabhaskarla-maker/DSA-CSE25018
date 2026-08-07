n = int(input("please enter the number of terms of fibonacci series required to be printed"))
# fibonacci series - 0,1,1,2,3,5,8,13,...........
# should only use the recursions instead of loops we need to write the functions
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(n):
    print(fibonacci(i), end=" ")

fibonacci(n)

