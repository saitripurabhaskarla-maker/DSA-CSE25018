# factorial of a given number
def fact(n):
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

n = int(input("Enter a number: "))

result = fact(n)

print(fact(n))

